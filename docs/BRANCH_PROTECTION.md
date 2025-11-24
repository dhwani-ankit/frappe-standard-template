# GitHub Branch Protection Configuration

This document outlines the recommended GitHub branch protection rules to enforce the QC Plan requirements.

## Required Branch Protection Rules

### For `main` and `master` branches (Production)

#### Required Settings:

1. **Require a pull request before merging**
   - ✅ Enable
   - Minimum number of reviewers: **1**
   - Dismiss stale pull request approvals when new commits are pushed: **Enabled**
   - Require review from Code Owners: **Enabled** (if CODEOWNERS file exists)

2. **Require approvals**
   - ✅ Enable
   - Required number of approvals: **1**
   - Dismiss stale pull request approvals when new commits are pushed: **Enabled**

3. **Require status checks to pass before merging**
   - ✅ Enable
   - Required status checks:
     - `commit-lint` (Semantic Commits)
     - `docs-required` (Documentation Required)
     - `linter` (Semgrep Rules)
     - `precommit` (Pre-Commit)
     - `e2e-tests` (E2E Tests)
     - `staging-deployment` (Staging Deployment)
   - Require branches to be up to date before merging: **Enabled**

4. **Require conversation resolution before merging**
   - ✅ Enable

5. **Require signed commits**
   - ⚠️ Optional (recommended for production)

6. **Require linear history**
   - ⚠️ Optional (recommended for clean history)

7. **Include administrators**
   - ⚠️ Set based on your team's policy

### For `develop` branch (Development)

#### Required Settings:

1. **Require a pull request before merging**
   - ✅ Enable
   - Minimum number of reviewers: **1**

2. **Require status checks to pass before merging**
   - ✅ Enable
   - Required status checks:
     - `commit-lint`
     - `docs-required`
     - `linter`
     - `precommit`
   - Require branches to be up to date before merging: **Enabled**

3. **Require conversation resolution before merging**
   - ✅ Enable

## How to Configure

### Via GitHub Web UI:

1. Go to your repository on GitHub
2. Navigate to **Settings** → **Branches**
3. Click **Add rule** or edit existing rule
4. Enter branch name pattern (e.g., `main`, `master`, `develop`)
5. Configure the settings as outlined above
6. Click **Create** or **Save changes**

### Via GitHub API:

```bash
# Example: Protect main branch
curl -X PUT \
  -H "Authorization: token YOUR_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  https://api.github.com/repos/OWNER/REPO/branches/main/protection \
  -d '{
    "required_status_checks": {
      "strict": true,
      "contexts": [
        "commit-lint",
        "docs-required",
        "linter",
        "precommit",
        "e2e-tests",
        "staging-deployment"
      ]
    },
    "enforce_admins": false,
    "required_pull_request_reviews": {
      "dismissal_restrictions": {},
      "dismiss_stale_reviews": true,
      "require_code_owner_reviews": true,
      "required_approving_review_count": 1
    },
    "restrictions": null,
    "required_linear_history": false,
    "allow_force_pushes": false,
    "allow_deletions": false
  }'
```

### Via Terraform (Infrastructure as Code):

```hcl
resource "github_branch_protection" "main" {
  repository_id = github_repository.repo.name
  pattern       = "main"

  required_status_checks {
    strict   = true
    contexts = [
      "commit-lint",
      "docs-required",
      "linter",
      "precommit",
      "e2e-tests",
      "staging-deployment"
    ]
  }

  required_pull_request_reviews {
    dismiss_stale_reviews           = true
    require_code_owner_reviews       = true
    required_approving_review_count  = 1
  }

  enforce_admins = false
}
```

## CODEOWNERS File

Create a `.github/CODEOWNERS` file to define code owners for automatic review assignment:

```
# Global owners
* @team-lead @devops-lead

# Specific paths
/.github/ @devops-team
/e2e/ @qa-team
/docs/ @documentation-team
```

## Verification

After configuring branch protection:

1. Create a test PR targeting the protected branch
2. Verify that:
   - PR cannot be merged without approval
   - PR cannot be merged if CI checks fail
   - PR cannot be merged if there are unresolved conversations
   - PR requires up-to-date branch

## Compliance with QC Plan

These branch protection rules ensure:

- ✅ **Level 1.1**: Code reviewed by at least one peer (enforced via required approvals)
- ✅ **Level 1.2**: All reviewer comments resolved (enforced via conversation resolution)
- ✅ **Level 1.3**: Coding standards followed (enforced via CI checks)
- ✅ **Level 2.2**: Test cases executed (enforced via E2E tests status check)
- ✅ **Level 2.1**: Deployed to staging (enforced via staging deployment check)

---

**Note**: These are recommendations. Adjust based on your team's specific needs and policies.

**Powered by [Dhwani RIS](https://dhwaniris.in)**

