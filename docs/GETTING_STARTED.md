# Getting Started Guide

Welcome to {{ cookiecutter.project_name }}! This guide will help you set up and start developing with this Frappe application template.

**Powered by [Dhwani RIS](https://dhwaniris.in)** 🚀

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

### System Requirements
- **Operating System**: Ubuntu 20.04+, macOS 10.15+, or Windows 10+ (with WSL2)
- **RAM**: Minimum 4GB (8GB+ recommended)
- **Storage**: At least 10GB free space
- **Internet**: Stable connection for package downloads

### Required Software
- **Python**: 3.8+ (3.13 recommended)
- **Node.js**: 18+ (22 LTS recommended)
- **npm**: 8+ (comes with Node.js)
- **Git**: Latest version
- **Database**: MariaDB 10.6+ or PostgreSQL 13+

### Optional Tools
- **VS Code**: Recommended IDE with Python and Frappe extensions
- **Docker**: For containerized development
- **Postman**: For API testing

## 🛠️ Installation Steps

### Step 1: Install Frappe Framework

#### Option A: Automatic Installation (Recommended)
```bash
# Download and run the easy install script
curl -sSL https://github.com/frappe/bench/raw/develop/easy-install.py | python3

# Or using wget
wget https://github.com/frappe/bench/raw/develop/easy-install.py
python3 easy-install.py
```

#### Option B: Manual Installation
```bash
# Install system dependencies (Ubuntu/Debian)
sudo apt update
sudo apt install -y python3-dev python3-pip python3-setuptools python3-venv
sudo apt install -y software-properties-common mariadb-server mariadb-client
sudo apt install -y redis-server nodejs npm
sudo apt install -y git curl

# Install bench
pip3 install frappe-bench

# Initialize bench
bench init frappe-bench --frappe-branch version-15
cd frappe-bench
```

### Step 2: Set up Database

#### MariaDB Setup
```bash
# Secure MariaDB installation
sudo mysql_secure_installation

# Create database user
sudo mysql -u root -p
```

```sql
-- In MySQL/MariaDB prompt
CREATE USER 'frappe'@'localhost' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON *.* TO 'frappe'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;
EXIT;
```

### Step 3: Configure Bench

```bash
# Set MariaDB configuration for bench
bench set-mariadb-host localhost
bench set-mariadb-root-password your_root_password

# Create a new site
bench new-site [your-site-name]
# Example: bench new-site myapp.localhost
```

### Step 4: Get Your App

```bash
# Navigate to your bench directory
cd frappe-bench

# Get the app from your repository
bench get-app {{ cookiecutter.app_name }} https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}.git

# Install the app on your site
bench --site [your-site-name] install-app {{ cookiecutter.app_name }}
```

### Step 5: Set up Development Environment

```bash
# Enable developer mode
bench --site [your-site-name] set-config developer_mode 1

# Set up pre-commit hooks
cd apps/{{ cookiecutter.app_name }}
pip install pre-commit
pre-commit install

# Start development server
bench start
```

## 🚀 Development Workflow

### 1. Create Your Development Branch
```bash
cd apps/{{ cookiecutter.app_name }}
git checkout -b feat/your-feature-name
```

### 2. Start Development Server
```bash
# From bench directory
bench start

# Or start specific services
bench start --help
```

### 3. Access Your Application
- **Main App**: http://[your-site-name]:8000
- **Socket.io**: http://localhost:9000
- **Redis**: localhost:11000 and localhost:13000

### 4. Create New DocType
```bash
# From bench directory
bench --site [your-site-name] console

# In Frappe console
from frappe.core.doctype.doctype.doctype import make_doctype
make_doctype('[Your DocType Name]', '[Your App Name]')
```

### 5. Database Migrations
```bash
# Run migrations after DocType changes
bench --site [your-site-name] migrate

# Clear cache and reload
bench --site [your-site-name] clear-cache
bench --site [your-site-name] reload-doc [app_name] [doctype] [doctype_name]
```

## 🔧 Configuration

### Environment Variables
Create a `.env` file in your app directory:

```env
# Database Configuration
DB_HOST=localhost
DB_PORT=3306
DB_NAME=[your-site-name]
DB_USER=frappe
DB_PASSWORD=your_password

# Email Configuration
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password

# Development Settings
DEVELOPER_MODE=1
DEBUG=1
```

### Site Configuration
Edit `sites/[your-site-name]/site_config.json`:

```json
{
	"db_host": "localhost",
	"db_name": "[your-site-name]",
	"db_password": "your_password",
	"db_type": "mariadb",
	"developer_mode": 1,
	"email_sender_name": "[Your App Name]",
	"email_sender_email": "noreply@yourdomain.com",
	"logging": 2,
	"log_level": "DEBUG"
}
```

## 🧪 Testing Setup

### Install Testing Dependencies
```bash
# From your app directory
pip install pytest pytest-cov

# Install Frappe testing requirements
pip install -e ".[testing]"
```

### Run Tests
```bash
# Run all tests
bench --site [your-site-name] run-tests

# Run specific app tests
bench --site [your-site-name] run-tests --app {{ cookiecutter.app_name }}

# Run with coverage
bench --site [your-site-name] run-tests --coverage --app {{ cookiecutter.app_name }}

# Run specific test file
bench --site [your-site-name] run-tests --module {{ cookiecutter.app_name }}.tests.test_module
```

### Writing Tests
Create test files in `{{ cookiecutter.app_name }}/tests/`:

```python
import frappe
import unittest

class TestYourDocType(unittest.TestCase):
	def setUp(self):
		# Setup test data
		pass
	
	def test_creation(self):
		# Test document creation
		doc = frappe.get_doc({
			"doctype": "Your DocType",
			"field1": "value1"
		})
		doc.insert()
		self.assertTrue(doc.name)
	
	def tearDown(self):
		# Cleanup test data
		pass
```

## 📝 Code Quality Setup

### Pre-commit Hooks
The template includes comprehensive pre-commit hooks:

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/psf/black
    rev: 23.12.1
    hooks:
      - id: black

  - repo: https://github.com/pycqa/isort
    rev: 5.13.2
    hooks:
      - id: isort

  - repo: https://github.com/pycqa/flake8
    rev: 7.0.0
    hooks:
      - id: flake8

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.8.0
    hooks:
      - id: mypy
```

### Run Quality Checks
```bash
# Run all pre-commit hooks
pre-commit run --all-files

# Run specific hook
pre-commit run black --all-files

# Format code
black .
isort .

# Check code quality
flake8 .
mypy .
```

## 🐛 Common Issues & Solutions

### Issue 1: Bench Command Not Found
```bash
# Add bench to PATH
echo 'export PATH=$PATH:~/.local/bin' >> ~/.bashrc
source ~/.bashrc

# Or use full path
~/.local/bin/bench --version
```

### Issue 2: MariaDB Connection Error
```bash
# Check MariaDB status
sudo systemctl status mariadb

# Restart MariaDB
sudo systemctl restart mariadb

# Check configuration
bench setup config
```

### Issue 3: Node.js Version Issues
```bash
# Install Node Version Manager
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
source ~/.bashrc

# Install and use Node.js 22
nvm install 22
nvm use 22
```

### Issue 4: Permission Denied
```bash
# Fix file permissions
sudo chown -R $USER:$USER frappe-bench

# Fix bench permissions
chmod +x ~/.local/bin/bench
```

### Issue 5: Redis Connection Error
```bash
# Start Redis
sudo systemctl start redis

# Check Redis status
redis-cli ping
# Should return: PONG
```

## 📚 Next Steps

1. **Read the Documentation**: Explore the `docs/` directory for detailed guides
2. **Customize Your App**: Modify the app according to your requirements
3. **Set up CI/CD**: Configure GitHub Actions for automated testing
4. **Deploy**: Follow deployment guides for production setup
5. **Community**: Join the Frappe community for support and discussions

## 🔗 Useful Resources

- [Frappe Framework Documentation](https://frappeframework.com/docs)
- [ERPNext Documentation](https://docs.erpnext.com)
- [Frappe School](https://frappe.school) - Learn Frappe development
- [Community Forum](https://discuss.frappe.io)
- [GitHub Discussions](https://github.com/frappe/frappe/discussions)

## 🆘 Getting Help

### Community Support
- **Forum**: [discuss.frappe.io](https://discuss.frappe.io)
- **Discord**: [Frappe Discord Server](https://discord.gg/frappe)
- **Stack Overflow**: Tag your questions with `frappe`

### Enterprise Support
For professional support and custom development:
- **Website**: [dhwaniris.in](https://dhwaniris.in)
- **Email**: [hello@dhwaniris.in](mailto:hello@dhwaniris.in)
- **Phone**: +91-XXX-XXX-XXXX

### Documentation Issues
If you find issues with this documentation:
1. Create an issue in the repository
2. Submit a pull request with improvements
3. Contact the maintainers

---

**Happy coding! 🎉**

Made with ❤️ by [Dhwani RIS](https://dhwaniris.in)
