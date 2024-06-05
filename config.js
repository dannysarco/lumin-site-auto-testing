const config = {
    baseUrl: 'https://www.luminsmart.com/',
    titles: {
      pageTitle: 'Lumin - Control What Matters',
    },
    selectors: {
      header: 'header.header',
      getLuminButton: 'a.b-button:has-text("Get Lumin")',
      cookiesBar: '#sg-cookiesBar',
      sliderCard: '.b-slider__card',
      footer: 'footer',
      firstSectionTitle: 'section.s-section_100vh h1',
      navLinks: 'nav a:has-text("${text}")',
      footerLinks: 'footer a:has-text("${text}")',
      navMenuParent: 'nav a:has-text("Products")',
      navMenuItems: 'nav .w-dropdown-list a:has-text("${text}")',
    },
    urls: {
      luminAppStore: 'https://apps.apple.com/us/app/lumin-smart/id1472704942',
      luminGooglePlay: 'https://play.google.com/store/apps/details?id=com.luminsmart.morse&hl=en_US&gl=US',
      getLuminButton: 'https://nndvjzdqqmf.typeform.com/to/IK1v1FOH',
    },
    links: {
      nav: [
        { text: 'Installers', href: 'https://www.luminsmart.com/partners' },
        { text: 'Homeowners', href: 'https://www.luminsmart.com/homeowners' },
        { text: 'Products', href: 'https://www.luminsmart.com/products' },
        { text: 'Lumin Resources', href: 'https://www.luminsmart.com/resources' },
        { text: 'App Login', href: 'https://app.luminsmart.com/login' },
      ],
      socialMedia: [
        { platform: 'LinkedIn', href: 'https://www.linkedin.com/company/11249694' },
        { platform: 'Facebook', href: 'https://www.facebook.com/luminsmartcircuits' },
        { platform: 'YouTube', href: 'https://youtube.com/luminsmart' },
        { platform: 'Instagram', href: 'https://www.instagram.com/luminsmart/' },
        { platform: 'Twitter', href: 'https://twitter.com/luminsmart' },
      ],
      appStores: [
        { platform: 'App Store', href: 'https://apps.apple.com/us/app/lumin-smart/id1472704942' },
        { platform: 'Google Play', href: 'https://play.google.com/store/apps/details?id=com.luminsmart.morse&hl=en_US&gl=US' },
      ],
      footer: [
        { text: 'Terms of use', href: '/consent-documentation' },
        { text: 'Privacy Policy', href: '/privacy-policy' },
      ],
      navMenu: [
        { text: 'Lumin Smart Panel', href: 'https://www.luminsmart.com/platform/smart-electrical-panel' },
        { text: 'Lumin Edge', href: 'https://www.luminsmart.com/lumin-edge' },
      ],
    },
    sections: [
      { id: 'sg-cookiesBar', description: 'Cookies Bar' },
      { class: 'b-slider__card', description: 'Slider Card Section' },
      { class: 'footer', description: 'Footer Section' },
      // Add other sections you want to check
    ],
    videoLinks: [
      'https://youtu.be/ssPQ8QhfEWs',
      'https://youtu.be/ivjgrzSB1_g',
      'https://youtu.be/Df9BHKuQfaI',
      'https://youtu.be/PU-eb_jkqdo',
      'https://youtu.be/ykq4V1hmvnA',
      'https://youtu.be/h_MMH4pziN0',
    ],
  };
  
  module.exports = config;