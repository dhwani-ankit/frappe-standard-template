# GitHub Project Board Visibility Guide

If the Release Tracking Board is not visible, follow these steps to enable and access it.

## Enable Repository Projects

1. Go to your repository on GitHub
2. Navigate to **Settings** → **General**
3. Scroll down to **Features** section
4. Enable **Projects** checkbox
5. Click **Save changes**

## Access the Board

### Method 1: Via Projects Tab

1. Go to your repository
2. Click on the **Projects** tab (next to Issues, Pull requests, etc.)
3. You should see "DevOps Release Board"

### Method 2: Direct URL

The board URL is provided in the workflow summary after creation:
- Format: `https://github.com/OWNER/REPO/projects/NUMBER`
- You can bookmark this URL for quick access

### Method 3: Via Repository Sidebar

1. Go to your repository
2. Look in the right sidebar
3. Click on **Projects** section
4. Select "DevOps Release Board"

## Troubleshooting

### Projects Tab Not Visible

**Issue**: Projects tab doesn't appear in repository navigation.

**Solution**:
1. Ensure Projects are enabled in Settings → General → Features
2. Refresh the page
3. Check if you have appropriate repository permissions (read access minimum)

### Board Not Found

**Issue**: Workflow says board was created but you can't find it.

**Solutions**:
1. Check workflow logs for the board URL
2. Try accessing via direct URL from workflow output
3. Verify the board name is exactly "DevOps Release Board"
4. Check if you have access to the repository

### Permission Errors

**Issue**: Workflow fails with permission errors.

**Solution**:
1. Ensure workflow has `repository-projects: write` permission
2. Check that GITHUB_TOKEN has sufficient permissions
3. Verify repository settings allow project creation

### Organization Projects vs Repository Projects

**Note**: This workflow creates a **Repository Project**, not an Organization Project.

- **Repository Projects**: Visible to repository collaborators
- **Organization Projects**: Visible to organization members (requires different API)

If you need an Organization Project instead:
1. Create it manually via GitHub UI
2. Or modify the workflow to use organization projects API (requires organization permissions)

## Manual Board Creation

If automated creation fails, you can create the board manually:

1. Go to repository → **Projects** tab
2. Click **New project**
3. Choose **Board** template
4. Name it "DevOps Release Board"
5. Add these columns:
   - 📋 Backlog
   - 🚀 Ready for Development
   - ⚙️ In Progress
   - 🔍 PR Raised
   - 👀 In Review
   - ✅ QA Certification
   - 🚀 Staging Deployment
   - 📝 Release Authorization
   - 🌐 Production Deployment
   - ✅ Done

## Verification

After enabling Projects and creating the board:

1. ✅ Projects tab is visible in repository
2. ✅ "DevOps Release Board" appears in Projects list
3. ✅ All 10 columns are present
4. ✅ Board is accessible to all repository collaborators

---

**Powered by [Dhwani RIS](https://dhwaniris.in)**

