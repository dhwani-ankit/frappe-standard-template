# DevOps Checklist Guide

## Overview

The DevOps Checklist is an **automated, non-editable** checklist that appears on every Pull Request. It's managed entirely by bots and cannot be manually edited.

## 🔧 What It Tracks

The DevOps Checklist automatically monitors:

1. **CI/CD Pipeline** - All CI checks must pass
2. **Staging Deployment** - Code must be deployed to staging
3. **Security Scan** - Security checks must pass
4. **Code Coverage** - Coverage reports must meet thresholds
5. **E2E Tests** - End-to-end tests must pass
6. **Breaking Changes** - Detects if PR has breaking changes

## 🚫 Why It's Non-Editable

The DevOps Checklist is protected to ensure:
- ✅ Accurate status reporting
- ✅ No manual manipulation
- ✅ Consistent DevOps standards
- ✅ Automated compliance tracking

## 🤖 How It Works

### Automatic Updates

The checklist is automatically updated when:
- ✅ CI/CD workflows complete
- ✅ Staging deployments finish
- ✅ Security scans run
- ✅ Coverage reports are generated
- ✅ E2E tests complete
- ✅ PR labels change

### Bot Management

The **DevOps Checklist Bot** (`.github/workflows/devops-checklist-bot.yml`) runs automatically and:
1. Checks all DevOps-related statuses
2. Updates the checklist comment
3. Overwrites any manual edits

### Protection

The **DevOps Checklist Enforcer** (`.github/workflows/enforce-devops-checklist.yml`) ensures:
- Manual edits to PR description are reverted
- Checklist template is restored
- Warning comments are posted

## 📋 Checklist Status

### ✅ Ready for Production

All checks must pass:
- ✅ CI/CD Pipeline
- ✅ Staging Deployment
- ✅ Security Scan
- ✅ Code Coverage
- ✅ E2E Tests

### ⏳ Pending Checks

Some checks are still running or failed.

### ⚠️ Breaking Changes

If breaking changes are detected, the checklist will show a warning.

## 🔍 Viewing the Checklist

The checklist appears as a **bot comment** on every PR:

```
## 🔧 DevOps Checklist (NON-EDITABLE)

| # | Check | Status | Details |
|---|-------|--------|---------|
| 1 | CI/CD Pipeline | ✅ | All CI checks passed |
| 2 | Staging Deployment | ✅ | Deployed to staging |
| ...
```

## 🛠️ Troubleshooting

### Checklist Not Appearing

1. **Check if bot workflow is running**:
   - Go to **Actions** → **DevOps Checklist Bot**
   - Verify workflow is enabled

2. **Check workflow triggers**:
   - PR opened
   - Checks completed
   - Deployments finished

3. **Manually trigger**:
   - Go to **Actions** → **DevOps Checklist Bot**
   - Click **Run workflow**
   - Enter PR number

### Checklist Not Updating

1. **Check if checks are completing**:
   - Verify CI/CD workflows are running
   - Check if deployments are happening
   - Ensure tests are executing

2. **Check bot permissions**:
   - Verify `pull-requests: write` permission
   - Check `GITHUB_TOKEN` has correct scope

### Manual Edit Attempted

If you try to edit the checklist:
- ⚠️ Your changes will be automatically reverted
- ⚠️ A warning comment will be posted
- ✅ The bot will restore the template

## 📝 PR Template

The PR template includes a placeholder section:

```markdown
## 🔧 DevOps Checklist (AUTOMATED - DO NOT EDIT)

> ⚠️ **This section is automatically managed by DevOps Bot.**

The DevOps Checklist will appear here automatically...
```

**Do not edit this section** - it's automatically replaced by the bot.

## ✅ Best Practices

1. **Don't edit the checklist** - It's automated
2. **Wait for checks to complete** - The bot updates automatically
3. **Check bot comments** - The checklist appears as a comment
4. **Review status regularly** - The bot updates in real-time

## 🔗 Related Workflows

- **DevOps Checklist Bot**: `.github/workflows/devops-checklist-bot.yml`
- **DevOps Checklist Enforcer**: `.github/workflows/enforce-devops-checklist.yml`
- **QC Plan Bot**: `.github/workflows/qc-plan-bot.yml`

---

**Powered by [Dhwani RIS](https://dhwaniris.in)**

