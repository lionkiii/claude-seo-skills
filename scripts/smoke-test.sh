#!/usr/bin/env bash
# smoke-test.sh — Verify SEO skill system installation and basic functionality
# Target domain: vanihq.com (per CONTEXT.md decision)
# Usage: ./scripts/smoke-test.sh [--quick]
#   --quick: only check file existence, skip routing table checks

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
INSTALLED_SKILLS="${HOME}/.claude/skills"
SKILLS_SRC="${PROJECT_ROOT}/skills"

QUICK=false
for arg in "$@"; do
  case "$arg" in
    --quick) QUICK=true ;;
    *) echo "Unknown argument: $arg" >&2; echo "Usage: $0 [--quick]" >&2; exit 1 ;;
  esac
done

# Colors
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m'

PASS=0
FAIL=0
WARN=0
FAILURES=()

pass() { echo -e "  ${GREEN}PASS${NC} $*"; PASS=$((PASS + 1)); }
fail() { echo -e "  ${RED}FAIL${NC} $*"; FAIL=$((FAIL + 1)); FAILURES+=("$*"); }
warn() { echo -e "  ${YELLOW}WARN${NC} $*"; WARN=$((WARN + 1)); }

echo ""
echo "================================================="
echo "  SEO Skill System Smoke Test"
echo "================================================="
echo ""

# -------------------------------------------------------
# CHECK 1: Installation — All 42 skill directories exist
# -------------------------------------------------------
echo "[ 1/5 ] Skill Directory Installation"

EXPECTED_SKILLS=(
  # Phase 1 — Original 12
  "seo"
  "seo-audit"
  "seo-page"
  "seo-sitemap"
  "seo-schema"
  "seo-images"
  "seo-technical"
  "seo-content"
  "seo-geo"
  "seo-plan"
  "seo-programmatic"
  "seo-competitor-pages"
  "seo-hreflang"
  # Phase 2 — GSC (9)
  "seo-gsc-overview"
  "seo-gsc-drops"
  "seo-gsc-opportunities"
  "seo-gsc-brand-vs-nonbrand"
  "seo-gsc-cannibalization"
  "seo-gsc-compare"
  "seo-gsc-content-decay"
  "seo-gsc-indexing"
  "seo-gsc-new-keywords"
  # Phase 2 — Ahrefs (10)
  "seo-ahrefs-overview"
  "seo-ahrefs-backlinks"
  "seo-ahrefs-keywords"
  "seo-ahrefs-competitors"
  "seo-ahrefs-content-gap"
  "seo-ahrefs-broken-links"
  "seo-ahrefs-new-links"
  "seo-ahrefs-anchor-analysis"
  "seo-ahrefs-dr-history"
  "seo-ahrefs-top-pages"
  # Phase 2 — Local/No MCP (1)
  "seo-markdown-audit"
  # Phase 3 — Cross-MCP (5)
  "seo-serp"
  "seo-content-brief"
  "seo-brand-radar"
  "seo-site-audit-pro"
  "seo-report"
  # Phase 4 — Local Analysis (5)
  "seo-log-analysis"
  "seo-ai-content-check"
  "seo-internal-links"
  "seo-local"
  "seo-migration-check"
)

for skill in "${EXPECTED_SKILLS[@]}"; do
  if [ -d "${INSTALLED_SKILLS}/${skill}" ]; then
    pass "Installed: ${skill}/"
  else
    fail "Missing from installation: ${INSTALLED_SKILLS}/${skill}/"
  fi
done

echo ""

# -------------------------------------------------------
# CHECK 2: YAML Validation
# -------------------------------------------------------
echo "[ 2/5 ] YAML Frontmatter Validation"

VALIDATE_SCRIPT="${SKILLS_SRC}/seo/hooks/validate-yaml.py"
VENV_PATH="${INSTALLED_SKILLS}/seo/.venv"
PYTHON_BIN="python3"

if [ -f "${VENV_PATH}/bin/python" ]; then
  PYTHON_BIN="${VENV_PATH}/bin/python"
fi

if [ ! -f "${VALIDATE_SCRIPT}" ]; then
  warn "validate-yaml.py not found at ${VALIDATE_SCRIPT} — skipping YAML validation"
elif ! "${PYTHON_BIN}" -c "import yaml" 2>/dev/null; then
  warn "PyYAML not available — skipping YAML validation (run install.sh to set up venv)"
else
  SKILL_MDS=()
  while IFS= read -r -d '' f; do
    SKILL_MDS+=("$f")
  done < <(find "${SKILLS_SRC}" -name "SKILL.md" -print0)

  if "${PYTHON_BIN}" "${VALIDATE_SCRIPT}" "${SKILL_MDS[@]}" 2>&1; then
    pass "YAML validation passed (${#SKILL_MDS[@]} SKILL.md files)"
  else
    fail "YAML validation failed — see errors above"
  fi
fi

echo ""

# -------------------------------------------------------
# CHECK 3: Routing Table Completeness
# -------------------------------------------------------
echo "[ 3/5 ] Routing Table Check"

if $QUICK; then
  warn "Skipped (--quick mode)"
else
  ORCHESTRATOR="${SKILLS_SRC}/seo/SKILL.md"
  ROUTING_COMMANDS=(
    "seo-audit" "seo-page" "seo-sitemap" "seo-schema" "seo-images"
    "seo-technical" "seo-content" "seo-geo" "seo-plan" "seo-programmatic"
    "seo-competitor-pages" "seo-hreflang"
    "seo-gsc-overview" "seo-gsc-drops" "seo-gsc-opportunities"
    "seo-gsc-brand-vs-nonbrand" "seo-gsc-cannibalization" "seo-gsc-compare"
    "seo-gsc-content-decay" "seo-gsc-indexing" "seo-gsc-new-keywords"
    "seo-ahrefs-overview" "seo-ahrefs-backlinks" "seo-ahrefs-keywords"
    "seo-ahrefs-competitors" "seo-ahrefs-content-gap" "seo-ahrefs-broken-links"
    "seo-ahrefs-new-links" "seo-ahrefs-anchor-analysis" "seo-ahrefs-dr-history"
    "seo-ahrefs-top-pages" "seo-markdown-audit" "seo-serp" "seo-content-brief"
    "seo-brand-radar" "seo-site-audit-pro" "seo-report"
    "seo-log-analysis" "seo-ai-content-check" "seo-internal-links"
    "seo-local" "seo-migration-check"
  )

  for entry in "${ROUTING_COMMANDS[@]}"; do
    if grep -q "${entry}/" "${ORCHESTRATOR}" 2>/dev/null; then
      pass "Routing entry: ${entry}/"
    else
      fail "Missing routing entry: ${entry}/ not found in seo/SKILL.md"
    fi
  done

  # Verify each routing entry maps to an existing source directory
  for entry in "${ROUTING_COMMANDS[@]}"; do
    if [ -d "${SKILLS_SRC}/${entry}" ]; then
      pass "Source directory exists: skills/${entry}/"
    else
      fail "Source directory missing: skills/${entry}/"
    fi
  done
fi

echo ""

# -------------------------------------------------------
# CHECK 4: Reference Files
# -------------------------------------------------------
echo "[ 4/5 ] Reference Files Check"

REFERENCE_FILES=(
  "${SKILLS_SRC}/seo/references/cwv-thresholds.md"
  "${SKILLS_SRC}/seo/references/schema-types.md"
  "${SKILLS_SRC}/seo/references/eeat-framework.md"
  "${SKILLS_SRC}/seo/references/quality-gates.md"
  "${SKILLS_SRC}/seo/references/mcp-degradation.md"
  "${SKILLS_SRC}/seo/references/ahrefs-api-reference.md"
  "${SKILLS_SRC}/seo/references/gsc-api-reference.md"
  "${SKILLS_SRC}/seo/references/google-seo-guide.md"
  "${SKILLS_SRC}/seo/references/markdown-guide.md"
)

for ref in "${REFERENCE_FILES[@]}"; do
  ref_name=$(basename "${ref}")
  if [ -f "${ref}" ]; then
    pass "Reference file: ${ref_name}"
  else
    fail "Missing reference file: ${ref}"
  fi
done

echo ""

# -------------------------------------------------------
# CHECK 5: Script Availability
# -------------------------------------------------------
echo "[ 5/5 ] Script Availability"

SCRIPTS=(
  "${SKILLS_SRC}/seo/scripts/fetch_page.py"
  "${SKILLS_SRC}/seo/scripts/parse_html.py"
  "${SKILLS_SRC}/seo/scripts/capture_screenshot.py"
  "${SKILLS_SRC}/seo/scripts/analyze_visual.py"
)

for script in "${SCRIPTS[@]}"; do
  script_name=$(basename "${script}")
  if [ -f "${script}" ]; then
    pass "Script exists: ${script_name}"
  else
    fail "Missing script: ${script}"
  fi
done

# Check validate-yaml.py (in hooks, not scripts)
if [ -f "${VALIDATE_SCRIPT}" ]; then
  pass "Script exists: validate-yaml.py"
else
  fail "Missing script: ${VALIDATE_SCRIPT}"
fi

echo ""

# -------------------------------------------------------
# Summary
# -------------------------------------------------------
echo "================================================="
echo "  Smoke Test Summary"
echo "================================================="
echo -e "  ${GREEN}PASS${NC}: ${PASS}"
echo -e "  ${RED}FAIL${NC}: ${FAIL}"
echo -e "  ${YELLOW}WARN${NC}: ${WARN}"
echo "================================================="

if [ ${#FAILURES[@]} -gt 0 ]; then
  echo ""
  echo "Failed checks:"
  for f in "${FAILURES[@]}"; do
    echo -e "  ${RED}x${NC} ${f}"
  done
  echo ""
fi

if [ ${FAIL} -gt 0 ]; then
  echo -e "${RED}SMOKE TEST FAILED${NC} — ${FAIL} check(s) failed"
  echo "Run ./install.sh to deploy missing skills, then re-run this script."
  exit 1
else
  echo -e "${GREEN}SMOKE TEST PASSED${NC} — all checks passed"
  exit 0
fi
