# GitHub Integrations Setup Guide

This guide explains how to set up and use the GitHub integrations configured in this repository.

## 🤖 All Contributors Bot

### What It Does

The All Contributors bot recognizes all types of contributions to your project, not just code. It automatically updates your README with a contributors table showing everyone who has contributed.

### Installation

1. Go to [All Contributors GitHub App](https://github.com/apps/allcontributors)
2. Click **Install**
3. Select your repository
4. Grant necessary permissions

### Usage

To add a contributor, comment on any issue or PR:

```
@all-contributors please add @username for code, docs, design
```

**Contribution Types**:
- `code` - Code contributions
- `doc` - Documentation
- `bug` - Bug reports
- `design` - Design work
- `review` - Code reviews
- `test` - Tests
- `ideas` - Ideas and planning
- And [many more](https://allcontributors.org/docs/en/emoji-key)

### Configuration

The bot uses [`.all-contributorsrc`](../.all-contributorsrc) for configuration. You can customize:
- Contributors per line
- Sort order
- Contribution types
- Badge template

### Example

```
@all-contributors please add @johndoe for code, docs, and @janedoe for design, review
```

The bot will automatically:
1. Add contributors to `.all-contributorsrc`
2. Update the README with contributor table
3. Commit the changes

---

## 🚀 Kodiak Auto-Merge Bot

### What It Does

Kodiak automatically updates and merges pull requests when all checks pass, keeping your PRs up-to-date with the base branch.

### Installation

1. Go to [Kodiak GitHub App](https://github.com/apps/kodiak)
2. Click **Install**
3. Select your repository
4. Grant necessary permissions

### Configuration

Kodiak uses [`.kodiak.toml`](../.kodiak.toml) for configuration. Key settings:

```toml
[merge]
auto_merge = true          # Enable auto-merge
method = "squash"          # Merge method
update_branch = true       # Update PR before merging

[merge.labels]
auto_merge = ["auto-merge"]  # Labels that enable auto-merge
block = ["wip"]             # Labels that block auto-merge
```

### Usage

#### Auto-Merge a PR

1. Ensure all checks pass
2. Get required approvals
3. Add `auto-merge` label to PR
4. Kodiak will automatically merge when ready

#### Block Auto-Merge

Add `wip` or `do-not-merge` label to prevent auto-merge.

#### Manual Control

- Remove `auto-merge` label to disable
- Kodiak will keep PR updated with base branch automatically

### Features

- ✅ **Auto-update**: Keeps PR branch up-to-date with base branch
- ✅ **Auto-merge**: Merges when all checks pass
- ✅ **Smart scheduling**: Updates PRs on schedule
- ✅ **Label-based control**: Use labels to control behavior

### Merge Methods

- `merge` - Standard merge commit
- `squash` - Squash all commits into one
- `rebase` - Rebase commits onto base branch

---

## 📊 Codecov Coverage

### What It Does

Codecov provides code coverage reporting and analysis, helping you understand how much of your codebase is tested.

### Installation

1. Go to [Codecov GitHub App](https://github.com/apps/codecov)
2. Click **Install**
3. Select your repository
4. Grant necessary permissions

### Configuration

#### For Public Repositories

No additional configuration needed! Codecov works automatically.

#### For Private Repositories

1. Go to [Codecov](https://codecov.io) and sign in
2. Add your repository
3. Get your `CODECOV_TOKEN`
4. Add it to GitHub repository secrets:
   - Go to **Settings** → **Secrets** → **Actions**
   - Add secret: `CODECOV_TOKEN` with your token

### Usage

Coverage reports are automatically generated from CI workflows. The [Codecov workflow](../.github/workflows/codecov.yml) handles:

1. Running tests with coverage
2. Generating coverage reports
3. Uploading to Codecov
4. Posting PR comments with coverage info

### Viewing Coverage

- **PR Comments**: Codecov bot comments on PRs with coverage changes
- **Dashboard**: Visit [codecov.io](https://codecov.io) for detailed reports
- **Badges**: Add coverage badges to your README

### Coverage Badge

Add to your README:

```markdown
[![codecov](https://codecov.io/gh/OWNER/REPO/branch/main/graph/badge.svg)](https://codecov.io/gh/OWNER/REPO)
```

### Features

- 📊 **Coverage Reports**: Detailed line-by-line coverage
- 💬 **PR Comments**: Coverage changes in PR comments
- 📈 **Trends**: Track coverage over time
- 🎯 **Targets**: Set coverage thresholds
- 🔍 **Diff Coverage**: See what's covered in your PR

---

## 🔧 Troubleshooting

### All Contributors Bot Not Responding

1. Check if the app is installed: **Settings** → **Integrations** → **Installed GitHub Apps**
2. Verify permissions are granted
3. Check bot is mentioned correctly: `@all-contributors`
4. Ensure `.all-contributorsrc` exists and is valid JSON

### Kodiak Not Auto-Merging

1. Check if the app is installed
2. Verify `.kodiak.toml` exists
3. Ensure PR has `auto-merge` label
4. Check all required checks pass
5. Verify required approvals are met
6. Check for blocking labels (`wip`, `do-not-merge`)

### Codecov Not Reporting

1. Check if the app is installed
2. Verify CI workflow runs and generates coverage
3. Check `coverage.xml` is generated
4. For private repos, verify `CODECOV_TOKEN` is set
5. Check workflow logs for errors

---

## 📚 Additional Resources

- [All Contributors Documentation](https://allcontributors.org/docs/en/bot/overview)
- [Kodiak Documentation](https://kodiakhq.com/docs)
- [Codecov Documentation](https://docs.codecov.com)

---

**Powered by [Dhwani RIS](https://dhwaniris.in)**

