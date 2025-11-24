# Quick Setup Guide for GitHub Integrations

## 🚀 Quick Setup (5 Minutes)

### 1. All Contributors Bot

**Install**:
1. Visit: https://github.com/apps/allcontributors
2. Click **Install**
3. Select your repository

**Test**:
Comment on any PR/Issue:
```
@all-contributors please add @yourusername for code
```

### 2. Kodiak Auto-Merge

**Install**:
1. Visit: https://github.com/apps/kodiak
2. Click **Install**
3. Select your repository

**Test**:
1. Create a PR
2. Add `auto-merge` label
3. Kodiak will auto-merge when checks pass

### 3. Codecov

**Install**:
1. Visit: https://github.com/apps/codecov
2. Click **Install**
3. Select your repository

**For Private Repos** (optional):
1. Get token from https://codecov.io
2. Add to GitHub Secrets: `CODECOV_TOKEN`

**Test**:
- Coverage reports appear automatically in PRs
- Check Actions → Codecov Coverage workflow

---

## ✅ Verification Checklist

- [ ] All Contributors bot installed
- [ ] Kodiak bot installed
- [ ] Codecov app installed
- [ ] `.all-contributorsrc` exists
- [ ] `.kodiak.toml` exists
- [ ] Codecov workflow runs in CI
- [ ] Tested All Contributors bot (commented on PR)
- [ ] Tested Kodiak (added auto-merge label)
- [ ] Verified Codecov reports in PR

---

## 📖 Detailed Documentation

See [GitHub Integrations Guide](./GITHUB_INTEGRATIONS.md) for detailed setup and usage.

---

**Powered by [Dhwani RIS](https://dhwaniris.in)**

