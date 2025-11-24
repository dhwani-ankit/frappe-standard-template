# QC Plan Setup Guide

This guide walks you through setting up the Production Merge Readiness Checklist & Release Plan in your repository.

## Prerequisites

- GitHub repository with Actions enabled
- Admin access to repository settings
- Python 3.8+ installed
- Node.js 18+ installed

## Step-by-Step Setup

### 1. Install Dependencies

```bash
# Install Python dependencies
pip install requests

# Install Node.js dependencies (for E2E tests)
npm install

# Install Playwright browsers
npx playwright install --with-deps
```

### 2. Configure GitHub Secrets

Go to **Repository Settings** → **Secrets and variables** → **Actions** and add:

#### Required Secrets:
- `GITHUB_TOKEN` - Automatically provided by GitHub Actions


#### Optional Secrets (for deployments):
- `STAGING_URL` - Staging environment URL
- `E2E_BASE_URL` - E2E test base URL

### 3. Create Release Board

Run the board creation workflow:

1. Go to **Actions** → **Auto Create Release Board**
2. Click **Run workflow**
3. Click **Run workflow** button

This will create a GitHub Project board with columns aligned to the QC Plan workflow.

### 4. Configure Branch Protection

Follow the guide in [BRANCH_PROTECTION.md](./BRANCH_PROTECTION.md) to set up branch protection rules.

**Quick Setup:**
1. Go to **Settings** → **Branches**
2. Add rule for `main`/`master` branch
3. Enable:
   - ✅ Require a pull request before merging
   - ✅ Require approvals (1 reviewer)
   - ✅ Require status checks to pass
   - ✅ Require conversation resolution

### 5. Test the Setup

#### Test PR Template:
1. Create a new branch
2. Make a small change
3. Create a PR
4. Verify the PR template appears with QC Plan checklist

#### Test Release Request Tool:
1. Merge a test PR to `main`/`master` (or use workflow_dispatch)
2. Go to **Actions** → **Release Request Sender**
3. Run workflow with PR number
4. Verify:
   - GitHub issue created
   - Request ID generated
   - Deployment plan generated
   - Rollback script generated

#### Test Staging Deployment:
1. Merge a PR to `develop` branch
2. Verify staging deployment workflow runs
3. Check PR comment for staging URL

#### Test E2E Tests:
1. Create a PR
2. Verify E2E tests run automatically
3. Check test results in PR comments

### 6. Verify Workflows

Check that all workflows are enabled:

- ✅ `code-quality.yml` - Code quality checks
- ✅ `staging-deployment.yml` - Staging deployment
- ✅ `e2e-tests.yml` - E2E testing
- ✅ `release-request.yml` - Release request creation
- ✅ `release-approval.yml` - Release approval tracking
- ✅ `create-release-board.yml` - Board creation
- ✅ `update-release-board.yml` - Board updates

### 7. Create CODEOWNERS File (Optional)

Create `.github/CODEOWNERS` to automatically assign reviewers:

```
# Global owners
* @team-lead @devops-lead

# Specific paths
/.github/ @devops-team
/e2e/ @qa-team
/docs/ @documentation-team
```

## Verification Checklist

- [ ] All GitHub secrets configured
- [ ] Release board created
- [ ] Branch protection rules configured
- [ ] PR template working
- [ ] Release Request Tool working
- [ ] Staging deployment working
- [ ] E2E tests running
- [ ] All workflows enabled

## Troubleshooting

### Workflows Not Running

1. Check **Settings** → **Actions** → **General**
2. Ensure "Allow all actions and reusable workflows" is enabled
3. Check workflow file syntax (YAML validation)

### Release Request Tool Fails

1. Check GitHub token permissions
2. Verify workflow has correct permissions (issues: write, pull-requests: write)
3. Check if deployment plan generator script exists
4. Review workflow logs

### Board Not Created

1. Check repository has Projects enabled
2. Verify workflow has `repository-projects: write` permission
3. Run workflow manually via workflow_dispatch

### E2E Tests Failing

1. Verify Playwright browsers installed
2. Check `E2E_BASE_URL` secret is set
3. Ensure test environment is accessible
4. Review test logs for errors

## Next Steps

1. **Train Team**: Share [QC_PLAN_INTEGRATION.md](./QC_PLAN_INTEGRATION.md) with team
2. **Configure Notifications**: Set up email notifications if needed
3. **Customize Workflows**: Adjust workflows for your specific needs
4. **Monitor Compliance**: Use release tracker to monitor compliance

## Support

For issues or questions:
- Review [QC_PLAN_INTEGRATION.md](./QC_PLAN_INTEGRATION.md)
- Check [QC_PLAN_COMPARISON.md](../QC_PLAN_COMPARISON.md) for gap analysis
- Contact DevOps team

---

**Powered by [Dhwani RIS](https://dhwaniris.in)**

