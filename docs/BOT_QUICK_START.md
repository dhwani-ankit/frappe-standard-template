# Bot Quick Start Guide

## 🚀 Quick Test (2 Minutes)

### Step 1: Create a Test PR

```bash
# Create test branch
git checkout -b test/bot-test

# Make a small change
echo "# Test" >> test-bot.md
git add test-bot.md
git commit -m "test: verify bot automation"

# Push and create PR
git push origin test/bot-test
```

Then create PR on GitHub.

### Step 2: Check Bots Run

1. **Wait 30 seconds** after PR creation
2. Go to **Actions** tab
3. You should see:
   - ✅ QC Plan Bot - Automated Checks
   - ✅ Coding Standards Bot
   - ✅ Pre-Commit (if configured)

### Step 3: Check PR Comments

1. Open your test PR
2. Scroll to comments section
3. Look for comments starting with `## 🤖`
4. Bots should have posted status updates

## 🔧 Manual Trigger

If bots don't run automatically:

1. Go to **Actions** → **QC Plan Bot - Automated Checks**
2. Click **Run workflow**
3. Enter PR number
4. Click **Run workflow**

## ✅ Expected Results

After creating a PR, you should see:

- **QC Plan Bot** comment with Level 1 & Level 2 status
- **Coding Standards Bot** comment (after review)
- **Pre-commit** checks running
- **E2E Test Bot** comment (if tests configured)

## 🐛 If Bots Don't Run

1. **Check Actions Tab**
   - Are workflows enabled?
   - Any errors in workflow runs?

2. **Check Permissions**
   - Repository Settings → Actions → General
   - Ensure "Allow all actions" is enabled

3. **Check Workflow Files**
   - Files exist in `.github/workflows/`?
   - YAML syntax is valid?

4. **Test Manually**
   - Use workflow_dispatch trigger
   - Go to Actions → Select workflow → Run workflow

## 📞 Still Not Working?

1. Check workflow logs for errors
2. Verify `GITHUB_TOKEN` permissions
3. Review workflow YAML syntax
4. See [HOW_TO_RUN_BOTS.md](./HOW_TO_RUN_BOTS.md) for detailed troubleshooting

---

**Powered by [Dhwani RIS](https://dhwaniris.in)**

