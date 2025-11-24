# Release Tags and Versioning

This document explains how release tags are automatically created using semantic-release.

## How It Works

When code is merged to `main` or `master` branch, the release workflow automatically:

1. **Analyzes commits** - Checks for conventional commit messages (feat:, fix:, etc.)
2. **Determines version** - Calculates next version based on commit types:
   - `feat:` → Minor version bump (1.0.0 → 1.1.0)
   - `fix:` → Patch version bump (1.0.0 → 1.0.1)
   - `BREAKING CHANGE:` → Major version bump (1.0.0 → 2.0.0)
3. **Creates Git Tag** - Creates a tag in format `v1.0.0`
4. **Creates GitHub Release** - Creates a release on GitHub with release notes
5. **Updates Version Files** - Updates `__init__.py` files with new version

## Commit Message Format

For tags to be created, commits must follow [Conventional Commits](https://www.conventionalcommits.org/) format:

```
<type>(<scope>): <subject>

[optional body]

[optional footer(s)]
```

### Valid Commit Types

- `feat:` - New feature (minor version)
- `fix:` - Bug fix (patch version)
- `perf:` - Performance improvement (patch version)
- `refactor:` - Code refactoring (no version bump)
- `docs:` - Documentation changes (no version bump)
- `style:` - Code style changes (no version bump)
- `test:` - Test additions/changes (no version bump)
- `chore:` - Maintenance tasks (no version bump)
- `ci:` - CI/CD changes (no version bump)
- `build:` - Build system changes (no version bump)
- `revert:` - Revert previous commit (patch version)

### Breaking Changes

To trigger a major version bump, include `BREAKING CHANGE:` in the commit footer:

```
feat(api): add new authentication method

BREAKING CHANGE: Old authentication method is deprecated
```

## Examples

### Example 1: Feature Release
```bash
git commit -m "feat(user): add user profile page"
# Merged to main → Creates tag v1.1.0 (if current is v1.0.0)
```

### Example 2: Bug Fix Release
```bash
git commit -m "fix(api): resolve authentication token expiry issue"
# Merged to main → Creates tag v1.0.1 (if current is v1.0.0)
```

### Example 3: Major Release
```bash
git commit -m "feat(api): redesign authentication system

BREAKING CHANGE: API authentication endpoints changed"
# Merged to main → Creates tag v2.0.0 (if current is v1.0.0)
```

## Troubleshooting

### Tags Not Created

**Issue**: Workflow runs but no tags are created.

**Possible Causes**:
1. **No conventional commits** - Commits don't follow the format
2. **No changes detected** - All commits already released
3. **Workflow failed** - Check workflow logs for errors

**Solutions**:
1. Check commit messages follow conventional format
2. Review workflow logs in Actions tab
3. Verify `GITHUB_TOKEN` has `contents: write` permission
4. Ensure commits are on `main` or `master` branch

### Version Not Bumping

**Issue**: Tags created but version doesn't increment correctly.

**Solutions**:
1. Check `.releaserc` configuration
2. Verify commit types match release rules
3. Check if commits are being analyzed correctly

### Release Notes Empty

**Issue**: Release created but notes are empty.

**Solutions**:
1. Ensure commit messages have proper format
2. Check if commits have meaningful messages
3. Review release notes generator configuration

## Manual Tag Creation

If you need to create a tag manually (not recommended):

```bash
# Create and push tag
git tag -a v1.0.0 -m "Release v1.0.0"
git push origin v1.0.0

# Create GitHub release
gh release create v1.0.0 --title "Release v1.0.0" --notes "Release notes here"
```

**Note**: Manual tags may interfere with semantic-release. Use conventional commits instead.

## Configuration

Release configuration is in `.releaserc`:

- **Branches**: `main`, `master` (only these branches trigger releases)
- **Plugins**: 
  - `@semantic-release/commit-analyzer` - Analyzes commits
  - `@semantic-release/release-notes-generator` - Generates release notes
  - `@semantic-release/exec` - Updates version files
  - `@semantic-release/git` - Commits version changes
  - `@semantic-release/github` - Creates GitHub release and tags

## Verification

After merging to main/master:

1. Check **Actions** tab → **Generate Semantic Release** workflow
2. Verify workflow completed successfully
3. Check **Releases** tab for new release
4. Check **Tags** tab for new tag
5. Verify version updated in `__init__.py` files

## Best Practices

1. **Always use conventional commits** - Ensures proper versioning
2. **Write clear commit messages** - Better release notes
3. **Use scopes** - Helps organize changes (e.g., `feat(api):`)
4. **Document breaking changes** - Use `BREAKING CHANGE:` footer
5. **Review before merging** - Ensure commits follow format

---

**Powered by [Dhwani RIS](https://dhwaniris.in)**

