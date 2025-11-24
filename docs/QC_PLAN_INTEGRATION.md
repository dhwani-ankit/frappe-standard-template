# QC Plan Integration Guide

This guide explains how the Production Merge Readiness Checklist & Release Plan is integrated into the development workflow.

## Overview

The QC Plan enforces a three-level validation process before any code is merged to production:

1. **Level 1**: Peer Review - Coding Standards and Business Logic
2. **Level 2**: QA Certification - Functional, Edge, and Regression Testing
3. **Level 3**: Release Authorization - Deployment Planning

## Automated Components

### ✅ Level 1: Peer Review

#### 1.1 & 1.2: Code Review Requirements
- **Enforced via**: GitHub Branch Protection Rules
- **Configuration**: See [BRANCH_PROTECTION.md](./BRANCH_PROTECTION.md)
- **Requirement**: At least 1 approval required before merge

#### 1.3: Coding Standards
- **Enforced via**: Pre-commit hooks + CI workflows
- **Tools**: `ruff`, `prettier`, `eslint`, `frappe-pre-commit`
- **Status**: ✅ Fully automated

#### 1.4: Sensitive Logic Documentation
- **Enforced via**: PR Template checklist
- **Manual**: Developer must check and document sensitive code
- **Location**: PR description

#### 1.5: Screenshots/Review Notes
- **Enforced via**: PR Template checklist
- **Manual**: Developer must attach screenshots for UI changes
- **Location**: PR comments or description

### ✅ Level 2: QA Certification

#### 2.1: Staging Deployment
- **Enforced via**: `.github/workflows/staging-deployment.yml`
- **Trigger**: Automatic on merge to `develop` branch
- **Output**: Staging URL posted as PR comment
- **Status**: ✅ Automated

#### 2.2: Test Execution
- **Enforced via**: 
  - Unit tests: `.github/workflows/ci.yml`
  - E2E tests: `.github/workflows/e2e-tests.yml`
- **Tools**: `pytest`, `playwright`
- **Status**: ✅ Automated

#### 2.3: No High/Critical Bugs
- **Enforced via**: PR Template checklist
- **Manual**: QA Lead must verify and check
- **Integration**: Can be linked to bug tracker (Bitrix, Jira, etc.)

#### 2.4: Known Issues Listed
- **Enforced via**: PR Template checklist
- **Manual**: Developer/QA must list known issues with severity
- **Location**: PR description

#### 2.5: Regression Testing
- **Enforced via**: `.github/workflows/e2e-tests.yml`
- **Tool**: Playwright E2E tests
- **Status**: ✅ Automated

### ✅ Level 3: Release Authorization

#### 3.1: Deployment Plan
- **Generated via**: `.github/helper/deployment-plan-generator.py`
- **Trigger**: Automatic when creating release request
- **Output**: Markdown file in `.github/release-requests/`
- **Status**: ✅ Automated

#### 3.2: Rollback Steps
- **Generated via**: `.github/workflows/release-request.yml`
- **Trigger**: Automatic when creating release request
- **Output**: Shell script in `.github/release-requests/`
- **Status**: ✅ Automated

#### 3.3: Downtime Estimate
- **Generated via**: Deployment plan generator
- **Calculated**: Based on change analysis (database migrations, etc.)
- **Status**: ✅ Automated

#### 3.4: Stakeholder Communication
- **Handled via**: Release Request Workflow
- **Tool**: `.github/workflows/release-request.yml`
- **Output**: GitHub issue
- **Status**: ✅ Automated

#### 3.5: Go/No-Go Decision
- **Tracked via**: `.github/workflows/release-approval.yml`
- **Method**: GitHub issue comments (`/approve` or `/reject`)
- **Status**: ✅ Automated

## Release Request Sender Tool

### Usage

#### Option 1: GitHub Actions Workflow

1. Go to **Actions** → **Release Request Sender**
2. Click **Run workflow**
3. Enter PR number
4. Optionally enable email notification
5. Click **Run workflow**

#### Option 2: PR Comment

Comment `/release-request` on a merged PR to automatically create a release request.

### What It Does

1. **Generates Unique Request ID**: Format: `REL-YYYYMMDD-XXXXXXXX`
2. **Fetches PR Details**: Gets PR information from GitHub API
3. **Creates GitHub Issue**: Tracks the release request with QC checklist
4. **Generates Deployment Plan**: Analyzes changes and creates deployment steps
5. **Generates Rollback Script**: Creates executable rollback script
6. **Saves Artifacts**: All files saved to `.github/release-requests/`

### Output Files

- `REL-YYYYMMDD-XXXXXXXX.json` - Request metadata
- `REL-YYYYMMDD-XXXXXXXX-deployment-plan.md` - Deployment plan
- `REL-YYYYMMDD-XXXXXXXX-rollback.sh` - Rollback script

## Workflow Examples

### Example 1: Standard Feature Release

1. Developer creates PR with feature
2. Pre-commit hooks run automatically ✅
3. CI checks run (linting, tests) ✅
4. Peer reviews and approves ✅
5. PR merged to `develop`
6. Staging deployment runs automatically ✅
7. QA tests in staging
8. QA certifies (checks Level 2 items in PR)
9. Release request created via tool
10. Deployment plan and rollback script generated ✅
11. Team Lead/DevOps reviews and approves
12. PR merged to `main`
13. Production deployment (manual or automated)

### Example 2: Hotfix Release

1. Developer creates hotfix branch from `main`
2. Fix implemented and tested
3. PR created targeting `main`
4. Fast-track review (same process, shorter timeline)
5. Release request created with `hotfix` label
6. Expedited approval
7. Deploy to production

## Tracking and Reporting

### Release Tracker

View all release requests:

```bash
# View all requests (table format)
python .github/helper/release-tracker.py

# Filter by status
python .github/helper/release-tracker.py --status approved

# Export as JSON
python .github/helper/release-tracker.py --format json --output releases.json

# Export as CSV
python .github/helper/release-tracker.py --format csv --output releases.csv
```

### GitHub Issues

All release requests are tracked as GitHub issues with the `release-request` label. Filter by:
- Status: `pending`, `approved`, `rejected`, `deployed`, `rolled_back`
- Request ID: Search for `REL-YYYYMMDD-XXXXXXXX`

## Configuration

### GitHub Secrets

Add these secrets in repository settings (optional):

- `STAGING_URL` - Staging environment URL
- `E2E_BASE_URL` - E2E test base URL

Note: `GITHUB_TOKEN` is automatically provided by GitHub Actions and doesn't need to be configured.

## Compliance Reporting

### Success Metrics

Track these metrics to measure QC Plan compliance:

1. **100% of release requests via tool**: Check release tracker
2. **0 manual release emails**: Monitor email logs
3. **100% QC checklist compliance**: Review PR templates
4. **≥40% reduction in approval time**: Compare before/after metrics
5. **End-to-end tracking**: All releases have Request IDs

### Audit Trail

All release requests are logged in:
- `.github/release-requests/*.json` - Request metadata
- GitHub Issues - Tracking and approval history
- GitHub Actions - Workflow execution logs

## Troubleshooting

### Release Request Tool Not Working

1. Check GitHub token permissions (automatically provided)
2. Verify workflow has correct permissions (issues: write, pull-requests: write)
3. Check if deployment plan generator script exists
4. Review workflow logs in GitHub Actions

### Staging Deployment Fails

1. Check deployment secrets
2. Verify staging environment access
3. Review deployment logs
4. Check service health

### E2E Tests Failing

1. Verify test environment URL
2. Check Playwright browser installation
3. Review test logs and screenshots
4. Update test selectors if UI changed

## Support

For questions or issues:
- Check [QC_PLAN_COMPARISON.md](../QC_PLAN_COMPARISON.md) for gap analysis
- Review [BRANCH_PROTECTION.md](./BRANCH_PROTECTION.md) for branch protection setup
- Contact DevOps team for tool configuration

---

**Powered by [Dhwani RIS](https://dhwaniris.in)**

