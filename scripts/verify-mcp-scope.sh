#!/usr/bin/env bash
# verify-mcp-scope.sh — Verify MCP tools are registered at user scope
# Checks ~/.claude/mcp.json for GSC MCP registration.
# Warns if project-scoped mcp.json files would shadow user-scope config.
# Always exits 0 — MCP registration is informational, not blocking.

USER_MCP="${HOME}/.claude/mcp.json"

echo "=== MCP Scope Verification ==="
echo ""

# --- GSC MCP ---
if [ -f "${USER_MCP}" ]; then
  if grep -qi '"google-search-console"\|"gsc"\|GSC-MCP\|gsc-mcp' "${USER_MCP}" 2>/dev/null; then
    echo "  GSC MCP: registered at user scope (~/.claude/mcp.json)"
  else
    echo "  GSC MCP: NOT FOUND in ~/.claude/mcp.json"
    echo "         GSC commands require a Google Search Console MCP server."
    echo "         See README.md for setup instructions."
  fi
else
  echo "  GSC MCP: NOT FOUND — ~/.claude/mcp.json does not exist"
  echo "         Create ~/.claude/mcp.json and register the GSC MCP."
  echo "         See README.md for setup instructions."
fi

echo ""

# --- Ahrefs MCP ---
echo "  Ahrefs MCP: available via Claude.ai (no local registration needed)"
echo "              Connected at claude.ai account level — no mcp.json entry required"

echo ""

# --- Check for project-scoped mcp.json files that could shadow user scope ---
# Look in common project locations (current dir and parent dirs up to home)
SHADOWING_FILES=()
search_dir="$(pwd)"
while [[ "${search_dir}" != "${HOME}" && "${search_dir}" != "/" ]]; do
  if [ -f "${search_dir}/.claude/mcp.json" ]; then
    SHADOWING_FILES+=("${search_dir}/.claude/mcp.json")
  fi
  search_dir="$(dirname "${search_dir}")"
done

if [ ${#SHADOWING_FILES[@]} -gt 0 ]; then
  echo "  WARNING: Project-scoped mcp.json files detected that may shadow user-scope config:"
  for f in "${SHADOWING_FILES[@]}"; do
    echo "           ${f}"
  done
  echo "           These project configs take precedence over ~/.claude/mcp.json"
  echo "           Per project decision: MCPs must be at user scope to avoid subagent hallucination"
  echo "           Consider removing project-scoped mcp.json or moving entries to user scope"
else
  echo "  Scope check: No project-scoped mcp.json files found (user scope is active)"
fi

echo ""
echo "=== End MCP Verification ==="

# Always exit 0 — informational only
exit 0
