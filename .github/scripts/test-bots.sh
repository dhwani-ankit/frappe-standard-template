#!/bin/bash
# Quick script to test if bots are configured correctly

echo "🤖 Testing QC Plan Bots Configuration"
echo "======================================"
echo ""

# Check if workflows exist
echo "📋 Checking workflow files..."
if [ -f ".github/workflows/qc-plan-bot.yml" ]; then
    echo "✅ QC Plan Bot workflow exists"
else
    echo "❌ QC Plan Bot workflow missing"
fi

if [ -f ".github/workflows/auto-fill-pr-checklist.yml" ]; then
    echo "✅ Coding Standards Bot workflow exists"
else
    echo "❌ Coding Standards Bot workflow missing"
fi

if [ -f ".github/workflows/staging-bot.yml" ]; then
    echo "✅ Staging Deployment Bot workflow exists"
else
    echo "❌ Staging Deployment Bot workflow missing"
fi

echo ""
echo "🔍 Checking workflow syntax..."

# Check YAML syntax (requires yamllint or similar)
if command -v yamllint &> /dev/null; then
    echo "Running yamllint..."
    yamllint .github/workflows/qc-plan-bot.yml 2>&1 | head -5
else
    echo "ℹ️ yamllint not installed (optional)"
fi

echo ""
echo "✅ Configuration check complete!"
echo ""
echo "📝 To test bots:"
echo "   1. Create a test PR"
echo "   2. Go to Actions → Select bot workflow → Run workflow"
echo "   3. Or wait for automatic trigger on PR events"
echo ""
echo "📚 See docs/HOW_TO_RUN_BOTS.md for detailed instructions"

