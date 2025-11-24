# __PROJECT_NAME__

__PROJECT_DESCRIPTION__


## 📚 Documentation

- [📖 Getting Started Guide](./docs/GETTING_STARTED.md) - Quick setup and development guide
- [🛡️ QC Plan Integration](./docs/QC_PLAN_INTEGRATION.md) - Production Merge Readiness Checklist integration
- [🔒 Branch Protection Setup](./docs/BRANCH_PROTECTION.md) - GitHub branch protection configuration
- [📊 QC Plan Comparison](./QC_PLAN_COMPARISON.md) - Gap analysis and compliance matrix
- [📋 Board Visibility Guide](./docs/BOARD_VISIBILITY.md) - Troubleshooting GitHub Project board visibility
- [🏷️ Release Tags Guide](./docs/RELEASE_TAGS.md) - How release tags are automatically created

## ⚡ Quick Start

```bash
# Clone the repository
git clone https://github.com/__GITHUB_REPOSITORY__.git
cd __REPO_NAME__

# Install pre-commit hooks
pip install pre-commit
pre-commit install

# Start development
bench start
```

## 🛡️ Code Quality & Pre-commit Hooks

This project enforces strict code quality standards using automated tools:

### Pre-commit Hooks Enabled
- **Python Code Formatting**: `black`, `isort`, `autoflake`
- **Security Scanning**: `bandit`, `safety`
- **Code Quality**: `flake8`, `mypy`, `pylint`
- **Frappe Standards**: Custom hooks for Frappe-specific patterns
- **Commit Standards**: Conventional commits with `commitlint`
- **Documentation**: Automatic documentation generation

### Installation
```bash
# Install pre-commit
pip install pre-commit

# Install hooks
pre-commit install

# Run all hooks manually
pre-commit run --all-files
```

### Commit Standards
We follow [Conventional Commits](https://www.conventionalcommits.org/) specification:

```bash
# Format: type(scope): description
feat(user): add user authentication module
fix(api): resolve data validation issue
docs(readme): update installation instructions
test(auth): add unit tests for login flow
```

**Allowed commit types:**
- `feat` - New features
- `fix` - Bug fixes
- `docs` - Documentation changes
- `style` - Code style improvements
- `refactor` - Code refactoring
- `test` - Adding/updating tests
- `chore` - Maintenance tasks
- `perf` - Performance improvements
- `ci` - CI/CD changes
- `build` - Build system changes
- `revert` - Reverting changes
- `deprecate` - Deprecation decisions


## 📋 Requirements

- **Python**: 3.8+ (3.13 recommended)
- **Node.js**: 18+ (22 recommended)
- **Frappe Framework**: Latest stable version
- **Database**: MariaDB 10.6+ or PostgreSQL 13+

## 🚀 Development Workflow

1. **Create Feature Branch**
   ```bash
   git checkout -b feat/your-feature-name
   ```

2. **Make Changes**
   - Follow code quality standards
   - Write tests for new features
   - Update documentation

3. **Commit Changes**
   ```bash
   git add .
   git commit -m "feat(module): add new feature description"
   ```

4. **Pre-commit Hooks Run Automatically**
   - Code formatting
   - Security scanning
   - Quality checks
   - Documentation updates

5. **Push and Create PR**
   ```bash
   git push origin feat/your-feature-name
   ```
   
   The PR template will automatically include the QC Plan checklist. Ensure all items are completed before requesting review.

6. **QC Plan Compliance**
   - **Level 1**: Peer Review (automated via branch protection)
   - **Level 2**: QA Certification (automated staging deployment + E2E tests)
   - **Level 3**: Release Authorization (via Release Request Sender Tool)

## 🧪 Testing

### Unit Tests
```bash
# Run all tests
bench --site test_site run-tests

# Run specific app tests
bench --site test_site run-tests --app your_app_name

# Run with coverage
bench --site test_site run-tests --coverage
```

### E2E Tests (Playwright)
```bash
# Install Playwright browsers
npx playwright install --with-deps

# Run E2E tests
npx playwright test

# Run with UI mode
npx playwright test --ui

# Run specific test file
npx playwright test e2e/example.spec.js
```

E2E tests are automatically run on PRs as part of QC Plan Level 2.2 and 2.5 requirements.

## 📦 Installation

### Option 1: Using Frappe CLI (Recommended)
```bash
# Create new site
bench new-site your-site-name

# Install the app
bench --site your-site-name install-app __APP_NAME__
```

### Option 2: Development Setup
```bash
# Get the app
bench get-app __APP_NAME__ https://github.com/__GITHUB_REPOSITORY__.git

# Create new site
bench new-site development.localhost

# Install app
bench --site development.localhost install-app __APP_NAME__

# Start development server
bench start
```


## 🚀 Release Process

### Creating a Release Request

For production deployments, use the Release Request Sender Tool:

#### Option 1: GitHub Actions Workflow
1. Go to **Actions** → **Release Request Sender**
2. Click **Run workflow**
3. Enter PR number
4. Optionally enable email notification
5. Click **Run workflow**

The workflow will:
- Generate a unique Request ID
- Create a GitHub issue for tracking
- Generate deployment plan
- Generate rollback script
- Send notifications to stakeholders

### Tracking Releases

View all release requests:
```bash
# View all requests
python .github/helper/release-tracker.py

# Filter by status
python .github/helper/release-tracker.py --status approved

# Export as JSON
python .github/helper/release-tracker.py --format json --output releases.json
```

### Release Board

A GitHub Project board is automatically created to track releases through the QC Plan workflow. The board includes columns for:
- Backlog → Ready for Development → In Progress → PR Raised → In Review → QA Certification → Staging Deployment → Release Authorization → Production Deployment → Done

## 📋 QC Plan Compliance

This repository implements the **Production Merge Readiness Checklist & Release Plan** with:

- ✅ **Automated code quality checks** (Level 1.3)
- ✅ **Automated peer review enforcement** (Level 1.1, 1.2)
- ✅ **Automated staging deployment** (Level 2.1)
- ✅ **Automated E2E testing** (Level 2.2, 2.5)
- ✅ **Automated release request tracking** (Level 3)
- ✅ **Automated deployment planning** (Level 3.1)
- ✅ **Automated rollback scripts** (Level 3.2)

See [QC_PLAN_INTEGRATION.md](./docs/QC_PLAN_INTEGRATION.md) for detailed information.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

---

**Powered by [Dhwani RIS](https://dhwaniris.in)**
