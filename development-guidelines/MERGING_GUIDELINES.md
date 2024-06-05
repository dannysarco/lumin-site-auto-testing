
### Merging Best Practices

**Recommended Workflow:**

#### Feature Branches
- **Creation:**
  - Create feature branches from the `dev` branch.
- **Integration:**
  - Once a feature is complete, thoroughly test it and then merge it back into `dev`.
- **Main Branch:**
  - After thorough testing and review, merge `dev` into `main`.

#### Bug Fix Branches
- **Creation:**
  - Bug fix branches should also be based on `dev`.
- **Hotfixes:**
  - For urgent production bugs:
    - Create a bug fix branch directly from `main`.
    - Apply the fix and merge it back into `main`.
  - Ensure that `dev` is updated to reflect these hotfixes from `main`.

#### Release Branches (Optional)
- **Purpose:**
  - Use release branches to stabilize the project for production releases.
- **Creation:**
  - Create a release branch from `dev` before merging into `main`.
- **Quality Assurance:**
  - Perform final testing and quality assurance on the release branch.
  - Once everything is verified:
    - Merge the release branch into `main`.
    - Tag the release with the version number.

**General Guidelines:**

1. **Always Test in `dev`:**
   - Ensure changes are thoroughly tested in the `dev` branch before merging into `main`.

2. **Merge Order:**
   - `Feature branches` → `dev`
   - `dev` → `release` (optional)
   - `release` → `main` or
   - `dev` → `main`

3. **Update Branches Regularly:**
   - Keep `dev` in sync with `main` regularly to avoid conflicts.

### Recommended Process for Release Branch

1. **Create Release Branch:**
   ```bash
   # From the dev branch
   git checkout dev
   git pull origin dev
   git checkout -b release/v1.0.0
   ```

2. **Test and QA:**
   - Perform final testing and quality assurance on the release branch.

3. **Merge Release Branch to Main:**
   ```bash
   # After QA is complete
   git checkout main
   git pull origin main
   git merge release/v1.0.0
   ```

4. **Tag the Release:**
   ```bash
   git tag -a v1.0.0 -m "Release version 1.0.0"
   git push origin v1.0.0
   ```

5. **Merge Release Branch to Dev:**
   ```bash
   git checkout dev
   git merge release/v1.0.0
   git push origin dev
   ```

6. **Delete the Release Branch:**
   ```bash
   git branch -d release/v1.0.0
   git push origin --delete release/v1.0.0
   ```

**Example Commands for Regular Updates:**

- **Update `dev` with `main`:**
  ```bash
  git checkout dev
  git pull origin dev
  git merge main
  git push origin dev
  ```

- **Merge Feature Branch to `dev`:**
  ```bash
  git checkout dev
  git pull origin dev
  git merge feature/branch_name
  git push origin dev
  ```

- **Merge `dev` to `main`:**
  ```bash
  git checkout main
  git pull origin main
  git merge dev
  git push origin main
  ```
