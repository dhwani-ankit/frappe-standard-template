# How to Run QC Plan Bots

This guide explains how the automated bots work and how to test/run them.

## 🤖 Available Bots

1. **QC Plan Bot** - Main bot that checks Level 1 & Level 2 compliance
2. **Coding Standards Bot** - Validates coding standards and reviews
3. **Staging Deployment Bot** - Monitors staging deployments
4. **E2E Test Bot** - Runs and reports E2E test results
5. **Pre-commit Bot** - Validates code quality

## 🚀 Automatic Triggers

Bots run automatically when:

### QC Plan Bot
- ✅ PR opened
- ✅ PR updated (new commits pushed)
- ✅ PR marked as ready for review
- ✅ PR reviewed (approval/rejection)

### Coding Standards Bot
- ✅ PR opened
- ✅ PR reviewed
- ✅ PR updated

### Staging Deployment Bot
- ✅ Staging deployment workflow completes
- ✅ Deployment status changes

### E2E Test Bot
- ✅ PR opened/updated
- ✅ Code pushed to PR branch

### Pre-commit Bot
- ✅ PR opened/updated
- ✅ Code pushed to PR branch

## 🧪 Manual Testing

### Method 1: Via GitHub Actions UI

1. Go to **Actions** tab
2. Select the bot workflow (e.g., "QC Plan Bot - Automated Checks")
3. Click **Run workflow**
4. Enter PR number (if required)
5. Click **Run workflow**

### Method 2: Create a Test PR

1. Create a new branch:
   ```bash
   git checkout -b test/bot-test
   ```

2. Make a small change and commit:
   ```bash
   git commit -m "test: verify bot automation"
   ```

3. Push and create PR:
   ```bash
   git push origin test/bot-test
   ```

4. Bots will automatically run when PR is created

### Method 3: Trigger via PR Comment

Some bots can be triggered via PR comments (if configured):
- Comment `/qc-check` on a PR
- Comment `/run-bots` on a PR

## 🔍 Verify Bots Are Running

### Check Workflow Runs

1. Go to **Actions** tab
2. Look for bot workflows in the list
3. Check if they show as "running" or "completed"

### Check PR Comments

1. Open your PR
2. Look for bot comments (they start with `## 🤖`)
3. Bots post status updates automatically

### Check Workflow Logs

1. Go to **Actions** → Select workflow run
2. Click on the job
3. Expand steps to see logs
4. Look for errors or warnings

## 🐛 Troubleshooting

### Bot Not Running

**Issue**: Bot workflow doesn't trigger

**Solutions**:
1. Check workflow file exists in `.github/workflows/`
2. Verify workflow syntax (YAML validation)
3. Check if workflow is enabled in repository settings
4. Ensure triggers match your actions (PR opened, etc.)

### Bot Runs But No Comments

**Issue**: Workflow runs but no PR comments appear

**Solutions**:
1. Check workflow permissions - needs `pull-requests: write`
2. Verify `GITHUB_TOKEN` has correct permissions
3. Check workflow logs for errors
4. Ensure PR number is correctly identified

### Bot Comments Duplicate

**Issue**: Multiple comments from same bot

**Solutions**:
1. Bots should update existing comments (if implemented)
2. Check if multiple workflow runs triggered
3. Review bot logic for comment deduplication

### Bot Shows Wrong Status

**Issue**: Bot reports incorrect compliance status

**Solutions**:
1. Check if PR actually has approvals
2. Verify CI checks are running
3. Check if staging deployment completed
4. Review bot logic in workflow file

## 📋 Bot Status Check

Run this command to check all bot workflows:

```bash
# List all bot workflows
gh workflow list | grep -i bot

# Check specific bot status
gh run list --workflow="QC Plan Bot - Automated Checks"
```

## 🔧 Enable/Disable Bots

### Disable a Bot

1. Go to **Actions** → **Workflows**
2. Find the bot workflow
3. Click **...** → **Disable workflow**

### Re-enable a Bot

1. Go to **Actions** → **Workflows**
2. Find the disabled workflow
3. Click **Enable workflow**

## ✅ Expected Behavior

### When PR is Created

1. **QC Plan Bot** runs and posts initial status
2. **Coding Standards Bot** checks code quality
3. **Pre-commit Bot** validates formatting
4. **E2E Test Bot** runs tests (if configured)

### When PR is Reviewed

1. **Coding Standards Bot** detects approval
2. **QC Plan Bot** updates Level 1 status
3. Bots post updated compliance status

### When Code is Deployed

1. **Staging Deployment Bot** detects deployment
2. **QC Plan Bot** updates Level 2 status
3. Bots post deployment confirmation

## 🎯 Quick Test

To quickly test if bots are working:

1. Create a test PR with a simple change
2. Wait 1-2 minutes
3. Check PR for bot comments
4. If no comments appear, check Actions tab for errors

## 📞 Support

If bots are not working:

1. Check workflow logs in Actions tab
2. Verify repository permissions
3. Review workflow YAML syntax
4. Check GitHub Actions settings

---

**Powered by [Dhwani RIS](https://dhwaniris.in)**

