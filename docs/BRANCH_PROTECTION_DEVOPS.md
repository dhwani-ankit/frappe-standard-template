# Branch Protection - DevOps Checklist

## Overview

The DevOps Checklist is configured as a **required check** that blocks merging until all items pass.

## 🔒 Required Check Setup

### Automatic Setup

The DevOps Checklist Bot automatically creates a required check run named:
```
🔧 DevOps Checklist (Required)
```

This check appears in the PR checks section and **blocks merging** if it fails.

### Manual Branch Protection Setup

To make this check required for merging:

1. **Go to Repository Settings**
   - Navigate to **Settings** → **Branches**

2. **Add Branch Protection Rule**
   - Click **Add rule** or edit existing rule
   - Set **Branch name pattern**: `main`, `master`, or `develop`

3. **Require Status Checks**
   - Enable **Require status checks to pass before merging**
   - Enable **Require branches to be up to date before merging**
   - In **Status checks that are required**, search for:
     ```
     🔧 DevOps Checklist (Required)
     ```
   - Check the box to make it required

4. **Additional Settings** (Recommended)
   - ✅ Require pull request reviews before merging
   - ✅ Require approvals: 1
   - ✅ Dismiss stale pull request approvals when new commits are pushed
   - ✅ Require conversation resolution before merging

5. **Save Changes**

## ✅ Check Status

### Passed (✅)
- All 5 DevOps checklist items completed
- PR can be merged
- Check shows green ✅

### Failed (❌)
- One or more checklist items incomplete
- PR **cannot be merged**
- Check shows red ❌
- Error message: "DevOps Checklist incomplete: X/5 checks passed"

## 📋 Checklist Items

The check requires all of these to pass:

1. **CI/CD Pipeline** - All CI checks must pass
2. **Staging Deployment** - Code must be deployed to staging
3. **Security Scan** - Security checks must pass
4. **Code Coverage** - Coverage reports must meet thresholds
5. **E2E Tests** - End-to-end tests must pass

## 🔍 Viewing Check Status

### In PR Checks Section

The check appears in the PR sidebar under "Checks":

```
✅ All checks have passed
  ✅ 🔧 DevOps Checklist (Required)
  ✅ CI
  ✅ Quality Checks
  ...
```

### In PR Comments

The bot also posts a detailed comment with the full checklist table.

### In Actions Tab

View the workflow run:
- **Actions** → **DevOps Checklist Bot**
- See detailed logs and status

## 🚫 Merge Blocking

### When Check Fails

If the DevOps checklist check fails:
- ❌ Merge button is disabled
- ❌ "Merge pull request" shows error
- ❌ Message: "Required status check '🔧 DevOps Checklist (Required)' is pending"
- ❌ PR cannot be merged until check passes

### When Check Passes

Once all items pass:
- ✅ Check shows green
- ✅ Merge button enabled
- ✅ PR can be merged

## 🔧 Troubleshooting

### Check Not Appearing

1. **Verify workflow is enabled**:
   - Go to **Actions** → **DevOps Checklist Bot**
   - Ensure workflow is not disabled

2. **Check workflow triggers**:
   - PR opened
   - Checks completed
   - Deployments finished

3. **Manually trigger**:
   - Go to **Actions** → **DevOps Checklist Bot**
   - Click **Run workflow**
   - Enter PR number

### Check Not Required

1. **Verify branch protection**:
   - Go to **Settings** → **Branches**
   - Check if rule exists for your branch
   - Verify check is in required list

2. **Check check run name**:
   - Must be exactly: `🔧 DevOps Checklist (Required)`
   - Case-sensitive

3. **Repository permissions**:
   - Ensure workflow has `checks: write` permission
   - Verify `GITHUB_TOKEN` has correct scope

### Check Stuck in Pending

1. **Check workflow status**:
   - Go to **Actions** tab
   - Find DevOps Checklist Bot run
   - Check for errors

2. **Verify dependencies**:
   - Ensure CI/CD workflows are running
   - Check if deployments are happening
   - Verify tests are executing

3. **Re-run workflow**:
   - Go to failed workflow run
   - Click **Re-run all jobs**

## 📝 Configuration

### Check Run Name

The check run name is hardcoded as:
```
🔧 DevOps Checklist (Required)
```

To change it, edit `.github/workflows/devops-checklist-bot.yml`:
```yaml
name: '🔧 DevOps Checklist (Required)'
```

### Required Items

To modify required items, edit the `allPassed` condition in the workflow:
```javascript
const allPassed = status.ci_cd && 
                 status.staging_deployment && 
                 status.security_scan && 
                 status.code_coverage && 
                 status.e2e_tests;
```

## ✅ Verification

### Test the Setup

1. **Create a test PR**
2. **Check if DevOps Checklist check appears**
3. **Verify it blocks merging** (if items incomplete)
4. **Complete all items**
5. **Verify check passes and merge is enabled**

### Expected Behavior

- ✅ Check appears immediately when PR is created
- ✅ Check updates as items complete
- ✅ Check blocks merge if incomplete
- ✅ Check allows merge when all pass

---

**Powered by [Dhwani RIS](https://dhwaniris.in)**

