const { test, expect } = require('@playwright/test');
const config = require('./config');

test.describe('LuminSmart Homepage UI Tests', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto(config.baseUrl);
  });

  test.describe('Basic UI Elements', () => {
    test('Check page title', async ({ page }) => {
      await expect(page).toHaveTitle(config.titles.pageTitle);
    });

    test('Check header is visible', async ({ page }) => {
      const header = page.locator(config.selectors.header);
      await expect(header).toBeVisible();
    });

    test('Check main navigation links', async ({ page }) => {
      for (const link of config.links.nav) {
        const locator = page.locator(config.selectors.navLinks.replace('${text}', link.text));
        await expect(locator).toHaveAttribute('href', link.href);
      }
    });

    test('Check "Get Lumin" button', async ({ page }) => {
      const getLuminButton = page.locator(config.selectors.getLuminButton);
      await expect(getLuminButton).toBeVisible();
      await expect(getLuminButton).toHaveAttribute('href', config.urls.getLuminButton);
    });

    test('Check sections are present', async ({ page }) => {
      for (const section of config.sections) {
        const locator = section.id ? page.locator(`#${section.id}`) : page.locator(`.${section.class}`);
        const elementCount = await locator.count();
        console.log(`Found ${elementCount} elements for ${section.description}`);
        expect(elementCount).toBeGreaterThan(0); // Ensures the section exists in the DOM
      }
    });

    test('Check first section title', async ({ page }) => {
      const firstSectionTitle = page.locator(config.selectors.firstSectionTitle);
      await expect(firstSectionTitle).toHaveText('Empowering every home to');
    });

    test('Check video links are present', async ({ page }) => {
      for (const link of config.videoLinks) {
        const locator = page.locator(`a[href="${link}"]`);
        await expect(locator).toBeVisible();
      }
    });
  });

  test.describe('Navigation Menu Tests', () => {
    test('Check social media links', async ({ page }) => {
      for (const link of config.links.socialMedia) {
        const locator = page.locator(`a[href="${link.href}"]`);
        await locator.scrollIntoViewIfNeeded(); // Scroll to the element before checking visibility
        await expect(locator).toBeVisible();
      }
    });

    test('Check App Store links', async ({ page }) => {
      for (const link of config.links.appStores) {
        const locator = page.locator(`a[href="${link.href}"]`);
        await locator.scrollIntoViewIfNeeded(); // Scroll to the element before checking visibility
        await expect(locator).toBeVisible();
      }
    });

    test('Check footer links', async ({ page }) => {
      for (const link of config.links.footer) {
        const locator = page.locator(config.selectors.footerLinks.replace('${text}', link.text));
        await expect(locator).toHaveAttribute('href', link.href);
      }
    });

    test('Check navigation drop-down menu items', async ({ page }) => {
      const menuParent = page.locator(config.selectors.navMenuParent);
      await menuParent.hover();
      for (const item of config.links.navMenu) {
        const locator = page.locator(config.selectors.navMenuItems.replace('${text}', item.text));
        await expect(locator).toHaveAttribute('href', item.href);
        await expect(locator).toBeVisible();
      }
    });
  });
});