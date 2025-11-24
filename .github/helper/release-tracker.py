#!/usr/bin/env python3
"""
Release Tracker Dashboard

Tracks and reports on all release requests and their status.
Provides audit trail and compliance reporting for QC Plan.

Usage:
    python release-tracker.py [--status <status>] [--format <json|csv|table>]
"""

import argparse
import json
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional


class ReleaseTracker:
    """Tracks and reports on release requests."""

    def __init__(self):
        self.requests_dir = Path(".github/release-requests")

    def load_all_requests(self) -> List[Dict]:
        """Load all release request files."""
        requests = []
        
        if not self.requests_dir.exists():
            return requests
        
        for file_path in self.requests_dir.glob("*.json"):
            try:
                with open(file_path, "r") as f:
                    request_data = json.load(f)
                    requests.append(request_data)
            except Exception as e:
                print(f"⚠️  Error loading {file_path}: {e}")
        
        return sorted(requests, key=lambda x: x.get("created_at", ""), reverse=True)

    def filter_by_status(self, requests: List[Dict], status: Optional[str]) -> List[Dict]:
        """Filter requests by status."""
        if not status:
            return requests
        return [r for r in requests if r.get("status", "").lower() == status.lower()]

    def generate_summary(self, requests: List[Dict]) -> Dict:
        """Generate summary statistics."""
        total = len(requests)
        by_status = {}
        
        for request in requests:
            status = request.get("status", "unknown")
            by_status[status] = by_status.get(status, 0) + 1
        
        return {
            "total_requests": total,
            "by_status": by_status,
            "last_updated": datetime.now().isoformat(),
        }

    def format_table(self, requests: List[Dict]) -> str:
        """Format requests as a table."""
        if not requests:
            return "No release requests found."
        
        lines = []
        lines.append("| Request ID | PR # | Status | Created | Author |")
        lines.append("|------------|------|--------|---------|--------|")
        
        for req in requests:
            request_id = req.get("request_id", "N/A")
            pr_number = req.get("pr_number", "N/A")
            status = req.get("status", "unknown")
            created = req.get("created_at", "N/A")
            if created != "N/A":
                try:
                    created = datetime.fromisoformat(created).strftime("%Y-%m-%d %H:%M")
                except:
                    pass
            
            pr_details = req.get("pr_details", {})
            author = pr_details.get("user", {}).get("login", "N/A") if pr_details else "N/A"
            
            # Status emoji
            status_emoji = {
                "pending": "🟡",
                "approved": "✅",
                "rejected": "❌",
                "deployed": "🚀",
                "rolled_back": "↩️",
            }.get(status, "❓")
            
            lines.append(f"| `{request_id}` | #{pr_number} | {status_emoji} {status} | {created} | {author} |")
        
        return "\n".join(lines)

    def format_json(self, requests: List[Dict]) -> str:
        """Format requests as JSON."""
        return json.dumps(requests, indent=2)

    def format_csv(self, requests: List[Dict]) -> str:
        """Format requests as CSV."""
        if not requests:
            return "No release requests found."
        
        lines = ["Request ID,PR Number,Status,Created,Author"]
        
        for req in requests:
            request_id = req.get("request_id", "N/A")
            pr_number = req.get("pr_number", "N/A")
            status = req.get("status", "unknown")
            created = req.get("created_at", "N/A")
            
            pr_details = req.get("pr_details", {})
            author = pr_details.get("user", {}).get("login", "N/A") if pr_details else "N/A"
            
            lines.append(f"{request_id},{pr_number},{status},{created},{author}")
        
        return "\n".join(lines)

    def generate_report(
        self, status_filter: Optional[str] = None, output_format: str = "table"
    ) -> str:
        """Generate a release tracking report."""
        requests = self.load_all_requests()
        requests = self.filter_by_status(requests, status_filter)
        
        summary = self.generate_summary(requests)
        
        if output_format == "json":
            return self.format_json(requests)
        elif output_format == "csv":
            return self.format_csv(requests)
        else:  # table
            report = []
            report.append("# Release Request Tracker")
            report.append("")
            report.append("## Summary")
            report.append("")
            report.append(f"- **Total Requests**: {summary['total_requests']}")
            report.append("")
            report.append("### By Status")
            report.append("")
            for status, count in summary["by_status"].items():
                report.append(f"- **{status}**: {count}")
            report.append("")
            report.append("## All Requests")
            report.append("")
            report.append(self.format_table(requests))
            report.append("")
            report.append(f"*Last updated: {summary['last_updated']}*")
            
            return "\n".join(report)


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(description="Release Request Tracker")
    parser.add_argument(
        "--status",
        type=str,
        choices=["pending", "approved", "rejected", "deployed", "rolled_back"],
        help="Filter by status",
    )
    parser.add_argument(
        "--format",
        type=str,
        choices=["table", "json", "csv"],
        default="table",
        help="Output format",
    )
    parser.add_argument(
        "--output",
        type=str,
        help="Output file path (optional)",
    )

    args = parser.parse_args()

    tracker = ReleaseTracker()
    report = tracker.generate_report(args.status, args.format)

    if args.output:
        with open(args.output, "w") as f:
            f.write(report)
        print(f"✅ Report saved to: {args.output}")
    else:
        print(report)


if __name__ == "__main__":
    main()

