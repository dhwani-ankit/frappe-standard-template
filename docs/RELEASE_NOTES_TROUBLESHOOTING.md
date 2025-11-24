# Release Notes Troubleshooting

If release notes are not being published, follow this troubleshooting guide.

## Common Issues

### 1. Release Created But No Notes

**Symptoms**: Release exists on GitHub but release notes are empty.

**Causes**:
- Release notes generator not configured properly
- Commits don't have enough information
- Plugin order issue in `.releaserc`

**Solutions**:
1. Check `.releaserc` has `@semantic-release/release-notes-generator` plugin
2. Verify plugin order: notes generator should come before GitHub plugin
3. Ensure commits have descriptive messages
4. Check workflow logs for errors

### 2. No Release Created At All

**Symptoms**: Workflow runs but no release appears on GitHub.

**Causes**:
- No conventional commits detected
- All commits already released
- Workflow permissions issue
- Branch not matching (must be `main` or `master`)

**Solutions**:
1. Verify commits follow conventional format (`feat:`, `fix:`, etc.)
2. Check if commits are on `main` or `master` branch
3. Verify `GITHUB_TOKEN` has `contents: write` permission
4. Review workflow logs for "no release" messages

### 3. Release Created as Draft

**Symptoms**: Release exists but is marked as draft.

**Causes**:
- Configuration issue with GitHub plugin
- Permission restrictions

**Solutions**:
1. Check `.releaserc` GitHub plugin configuration
2. Verify workflow permissions
3. Manually publish draft release if needed

### 4. Release Notes Are Empty

**Symptoms**: Release created but notes section is blank.

**Causes**:
- No commits with release-worthy changes
- Only `chore:`, `docs:`, `style:` commits (don't trigger releases)
- Release notes generator not working

**Solutions**:
1. Ensure commits include `feat:`, `fix:`, or `perf:` types
2. Check release notes generator configuration
3. Verify commit messages are descriptive
4. Review workflow logs for generator errors

## Verification Steps

### Step 1: Check Workflow Logs

1. Go to **Actions** → **Generate Semantic Release**
2. Open the latest workflow run
3. Check the "Create Release and Tag" step
4. Look for:
   - `✅ Published release X.X.X`
   - `📝 Generated release notes`
   - Any error messages

### Step 2: Check GitHub Releases

1. Go to repository → **Releases**
2. Check if latest release exists
3. Verify release notes are present
4. Check if release is published (not draft)

### Step 3: Check Commit Messages

```bash
# Check recent commits
git log --oneline -10

# Should see format like:
# feat(user): add profile page
# fix(api): resolve authentication issue
```

### Step 4: Verify Configuration

Check `.releaserc` has correct plugin order:

```json
{
  "plugins": [
    "@semantic-release/commit-analyzer",
    "@semantic-release/release-notes-generator",  // Must be before GitHub plugin
    "@semantic-release/exec",
    "@semantic-release/git",
    "@semantic-release/github"  // Creates release with notes
  ]
}
```

## Manual Fix

If release was created without notes:

1. Go to **Releases** → Edit release
2. Generate notes manually from commits
3. Or copy from PR descriptions
4. Save release

## Testing

To test release notes generation:

1. Create a test commit:
   ```bash
   git commit -m "feat(test): add test feature for release notes"
   ```

2. Merge to `main` or `master`

3. Check workflow runs and creates release

4. Verify release notes include the test commit

## Best Practices

1. **Write descriptive commit messages** - Better release notes
2. **Use conventional commits** - Ensures proper categorization
3. **Include scope** - Helps organize changes (e.g., `feat(api):`)
4. **Review before merging** - Ensure commits follow format
5. **Check workflow after merge** - Verify release was created

## Configuration Reference

### Required Plugins

```json
{
  "plugins": [
    ["@semantic-release/commit-analyzer", { ... }],
    ["@semantic-release/release-notes-generator", { ... }],
    ["@semantic-release/github", {
      "generateNotes": true  // Ensure this is set
    }]
  ]
}
```

### Plugin Order Matters

The order of plugins in `.releaserc` is important:
1. `commit-analyzer` - Analyzes commits first
2. `release-notes-generator` - Generates notes
3. `github` - Publishes release with notes

---

**Powered by [Dhwani RIS](https://dhwaniris.in)**

