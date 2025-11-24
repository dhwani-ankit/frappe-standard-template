#!/usr/bin/env python3
"""
Deployment Plan Generator

Generates comprehensive deployment plans based on PR changes and QC Plan requirements.

Usage:
    python deployment-plan-generator.py --pr-number <PR_NUMBER> [--output <FILE>]
"""

import argparse
import os
import sys
from datetime import datetime
from typing import Dict, List, Optional

import requests


class DeploymentPlanGenerator:
    """Generates deployment plans for release requests."""

    def __init__(self):
        self.github_token = os.getenv("GITHUB_TOKEN") or os.getenv("DHWANI_FRAPPE_TOKEN")
        self.github_repo = os.getenv("GITHUB_REPOSITORY", "")

    def get_github_headers(self) -> Dict[str, str]:
        """Get GitHub API headers."""
        headers = {
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "Deployment-Plan-Generator/1.0",
        }
        if self.github_token:
            headers["Authorization"] = f"token {self.github_token}"
        return headers

    def fetch_pr_details(self, pr_number: str) -> Optional[Dict]:
        """Fetch PR details and changed files from GitHub."""
        if not self.github_repo:
            return None

        headers = self.get_github_headers()

        # Fetch PR details
        pr_url = f"https://api.github.com/repos/{self.github_repo}/pulls/{pr_number}"
        try:
            pr_response = requests.get(pr_url, headers=headers, timeout=30)
            if not pr_response.ok:
                return None
            pr_data = pr_response.json()
        except Exception:
            return None

        # Fetch changed files
        files_url = f"https://api.github.com/repos/{self.github_repo}/pulls/{pr_number}/files"
        try:
            files_response = requests.get(files_url, headers=headers, timeout=30)
            if files_response.ok:
                pr_data["changed_files"] = files_response.json()
            else:
                pr_data["changed_files"] = []
        except Exception:
            pr_data["changed_files"] = []

        return pr_data

    def analyze_changes(self, pr_data: Dict) -> Dict:
        """Analyze PR changes to determine deployment impact."""
        changed_files = pr_data.get("changed_files", [])
        
        analysis = {
            "has_database_changes": False,
            "has_migrations": False,
            "has_config_changes": False,
            "has_frontend_changes": False,
            "has_backend_changes": False,
            "has_dependencies": False,
            "affected_modules": set(),
            "file_types": set(),
        }

        for file in changed_files:
            filename = file.get("filename", "")
            status = file.get("status", "")
            
            # Check file type
            if filename.endswith((".py", ".js", ".vue", ".ts")):
                analysis["file_types"].add("code")
            if filename.endswith((".json", ".yaml", ".yml", ".conf", ".ini")):
                analysis["file_types"].add("config")
            if filename.endswith((".sql", ".db")):
                analysis["file_types"].add("database")
            
            # Check for migrations
            if "migration" in filename.lower() or "migrate" in filename.lower():
                analysis["has_migrations"] = True
                analysis["has_database_changes"] = True
            
            # Check for database changes
            if filename.endswith(".json") and ("doctype" in filename or "custom" in filename):
                analysis["has_database_changes"] = True
            
            # Check for config changes
            if any(x in filename for x in ["config", "site_config", "hooks", "requirements"]):
                analysis["has_config_changes"] = True
            
            # Check for frontend changes
            if filename.endswith((".js", ".vue", ".ts", ".scss", ".css")):
                analysis["has_frontend_changes"] = True
            
            # Check for backend changes
            if filename.endswith(".py"):
                analysis["has_backend_changes"] = True
            
            # Check for dependency changes
            if filename in ["requirements.txt", "package.json", "package-lock.json"]:
                analysis["has_dependencies"] = True
            
            # Extract module name
            parts = filename.split("/")
            if len(parts) > 1:
                analysis["affected_modules"].add(parts[0])

        analysis["affected_modules"] = sorted(list(analysis["affected_modules"]))
        analysis["file_types"] = sorted(list(analysis["file_types"]))

        return analysis

    def generate_deployment_plan(
        self, pr_number: str, pr_data: Optional[Dict] = None
    ) -> str:
        """Generate a comprehensive deployment plan."""
        if not pr_data:
            pr_data = self.fetch_pr_details(pr_number)

        analysis = self.analyze_changes(pr_data) if pr_data else {}

        plan = []
        plan.append("# Deployment Plan")
        plan.append("")
        plan.append(f"**Generated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}")
        plan.append(f"**PR Number**: #{pr_number}")
        if pr_data:
            plan.append(f"**PR Title**: {pr_data.get('title', 'N/A')}")
            plan.append(f"**Author**: {pr_data.get('user', {}).get('login', 'N/A')}")
            plan.append(f"**Base Branch**: {pr_data.get('base', {}).get('ref', 'N/A')}")
        plan.append("")

        # Change Analysis
        plan.append("## Change Analysis")
        plan.append("")
        if analysis:
            plan.append("### Impact Assessment")
            plan.append("")
            plan.append("| Category | Status |")
            plan.append("|----------|--------|")
            plan.append(f"| Database Changes | {'✅ Yes' if analysis.get('has_database_changes') else '❌ No'} |")
            plan.append(f"| Migrations | {'✅ Yes' if analysis.get('has_migrations') else '❌ No'} |")
            plan.append(f"| Config Changes | {'✅ Yes' if analysis.get('has_config_changes') else '❌ No'} |")
            plan.append(f"| Frontend Changes | {'✅ Yes' if analysis.get('has_frontend_changes') else '❌ No'} |")
            plan.append(f"| Backend Changes | {'✅ Yes' if analysis.get('has_backend_changes') else '❌ No'} |")
            plan.append(f"| Dependency Updates | {'✅ Yes' if analysis.get('has_dependencies') else '❌ No'} |")
            plan.append("")
            
            if analysis.get("affected_modules"):
                plan.append("### Affected Modules")
                plan.append("")
                for module in analysis["affected_modules"]:
                    plan.append(f"- `{module}`")
                plan.append("")
        else:
            plan.append("*Change analysis unavailable*")
            plan.append("")

        # Pre-Deployment Checklist
        plan.append("## Pre-Deployment Checklist")
        plan.append("")
        plan.append("- [ ] All QC Plan Level 1 items completed (Peer Review)")
        plan.append("- [ ] All QC Plan Level 2 items completed (QA Certification)")
        plan.append("- [ ] Release request approved (Level 3)")
        plan.append("- [ ] Backup current production database")
        plan.append("- [ ] Backup current codebase (tag/commit)")
        plan.append("- [ ] Verify staging deployment is successful")
        plan.append("- [ ] Review deployment plan with team")
        plan.append("- [ ] Notify stakeholders of deployment window")
        plan.append("")

        # Deployment Steps
        plan.append("## Deployment Steps")
        plan.append("")
        plan.append("### Step 1: Pre-Deployment Verification")
        plan.append("```bash")
        plan.append("# Verify current production version")
        plan.append("git log -1 --oneline")
        plan.append("")
        plan.append("# Check system health")
        plan.append("bench --site production.localhost doctor")
        plan.append("```")
        plan.append("")

        plan.append("### Step 2: Database Backup")
        plan.append("```bash")
        plan.append("# Create database backup")
        plan.append("bench --site production.localhost backup --with-files")
        plan.append("")
        plan.append("# Verify backup")
        plan.append("ls -lh sites/production.localhost/private/backups/")
        plan.append("```")
        plan.append("")

        if analysis.get("has_database_changes") or analysis.get("has_migrations"):
            plan.append("### Step 3: Database Migrations")
            plan.append("```bash")
            plan.append("# Run migrations")
            plan.append("bench --site production.localhost migrate")
            plan.append("")
            plan.append("# Verify migrations")
            plan.append("bench --site production.localhost console")
            plan.append("```")
            plan.append("")

        plan.append("### Step 4: Code Deployment")
        plan.append("```bash")
        plan.append("# Pull latest code")
        plan.append("git pull origin main")
        plan.append("")
        plan.append("# Update dependencies (if changed)")
        if analysis.get("has_dependencies"):
            plan.append("pip install -r requirements.txt")
            plan.append("npm ci")
        else:
            plan.append("# No dependency changes detected")
        plan.append("")
        plan.append("# Build assets (if frontend changes)")
        if analysis.get("has_frontend_changes"):
            plan.append("bench build")
        else:
            plan.append("# No frontend changes detected")
        plan.append("")
        plan.append("# Clear cache")
        plan.append("bench --site production.localhost clear-cache")
        plan.append("```")
        plan.append("")

        plan.append("### Step 5: Service Restart")
        plan.append("```bash")
        plan.append("# Restart services")
        plan.append("bench restart")
        plan.append("")
        plan.append("# Verify services are running")
        plan.append("bench --site production.localhost doctor")
        plan.append("```")
        plan.append("")

        plan.append("### Step 6: Post-Deployment Verification")
        plan.append("```bash")
        plan.append("# Run smoke tests")
        plan.append("bench --site production.localhost run-tests --module <affected_modules>")
        plan.append("")
        plan.append("# Check application logs")
        plan.append("tail -f logs/web.log")
        plan.append("tail -f logs/worker.log")
        plan.append("```")
        plan.append("")

        # Rollback Plan
        plan.append("## Rollback Plan")
        plan.append("")
        plan.append("### Rollback Triggers")
        plan.append("- Critical errors in application logs")
        plan.append("- Database migration failures")
        plan.append("- Service unavailability")
        plan.append("- Data integrity issues")
        plan.append("")

        plan.append("### Rollback Steps")
        plan.append("```bash")
        plan.append("# 1. Revert code to previous version")
        plan.append("git checkout <previous-commit-hash>")
        plan.append("")
        plan.append("# 2. Restore database (if needed)")
        plan.append("bench --site production.localhost restore <backup-file>")
        plan.append("")
        plan.append("# 3. Restart services")
        plan.append("bench restart")
        plan.append("")
        plan.append("# 4. Verify rollback")
        plan.append("bench --site production.localhost doctor")
        plan.append("```")
        plan.append("")

        # Downtime Estimate
        plan.append("## Downtime Estimate")
        plan.append("")
        if analysis.get("has_database_changes") or analysis.get("has_migrations"):
            plan.append("**Estimated Downtime**: 15-30 minutes")
            plan.append("- Database backup: 5-10 minutes")
            plan.append("- Migration execution: 5-10 minutes")
            plan.append("- Code deployment: 5-10 minutes")
        else:
            plan.append("**Estimated Downtime**: 5-10 minutes")
            plan.append("- Code deployment: 3-5 minutes")
            plan.append("- Service restart: 2-5 minutes")
        plan.append("")
        plan.append("**Mitigation**: Deploy during low-traffic hours if possible")
        plan.append("")

        # Monitoring
        plan.append("## Post-Deployment Monitoring")
        plan.append("")
        plan.append("- [ ] Monitor application logs for errors")
        plan.append("- [ ] Check system resource usage (CPU, Memory)")
        plan.append("- [ ] Verify critical user workflows")
        plan.append("- [ ] Monitor database performance")
        plan.append("- [ ] Check error tracking (Sentry, etc.)")
        plan.append("- [ ] Verify scheduled jobs are running")
        plan.append("")

        # Contacts
        plan.append("## Emergency Contacts")
        plan.append("")
        plan.append("- **Team Lead**: [To be filled]")
        plan.append("- **DevOps**: [To be filled]")
        plan.append("- **On-Call Engineer**: [To be filled]")
        plan.append("")

        return "\n".join(plan)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Deployment Plan Generator")
    parser.add_argument("--pr-number", type=str, required=True, help="PR number")
    parser.add_argument(
        "--output",
        type=str,
        help="Output file path (default: deployment-plan.md)",
    )

    args = parser.parse_args()

    generator = DeploymentPlanGenerator()
    plan = generator.generate_deployment_plan(args.pr_number)

    output_file = args.output or "deployment-plan.md"
    with open(output_file, "w") as f:
        f.write(plan)

    print(f"✅ Deployment plan generated: {output_file}")
    print(f"\n📄 Plan Preview:\n")
    print(plan[:500] + "..." if len(plan) > 500 else plan)


if __name__ == "__main__":
    main()

