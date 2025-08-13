# __PROJECT_NAME__

__PROJECT_DESCRIPTION__


## 📚 Documentation

- [📖 Getting Started Guide](./docs/GETTING_STARTED.md) - Quick setup and development guide

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

## 🧪 Testing

```bash
# Run all tests
bench --site test_site run-tests

# Run specific app tests
bench --site test_site run-tests --app your_app_name

# Run with coverage
bench --site test_site run-tests --coverage
```

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


## 📄 License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

---

**Powered by [Dhwani RIS](https://dhwaniris.in)**
