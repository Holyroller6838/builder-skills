#!/usr/bin/env bash
# Initialize a use-case directory under use-cases/<name>/.
# Requires platform data — run scripts/platform-pull.sh first.
#
# Usage:
#   ./scripts/use-case-init.sh <use-case-name> <platform-url> <client-id> <client-secret>
#
# Example:
#   ./scripts/use-case-init.sh port-turn-up https://platform.example.com client123 secret456

set -euo pipefail

USE_CASE="${1:?Usage: use-case-init.sh <use-case-name> <platform-url> <client-id> <client-secret>}"
PLATFORM_URL="${2:?Missing platform URL}"
CLIENT_ID="${3:?Missing client ID}"
CLIENT_SECRET="${4:?Missing client secret}"
PLATFORM_URL="${PLATFORM_URL%/}"

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PLATFORM_DIR="$SCRIPT_DIR/../platform"
USE_CASE_DIR="$SCRIPT_DIR/../use-cases/$USE_CASE"

# Require platform data to exist
if [ ! -f "$PLATFORM_DIR/.pulled-at" ]; then
  echo "ERROR: Platform data not found." >&2
  echo "       Run first: ./scripts/platform-pull.sh <platform-url> <client-id> <client-secret>" >&2
  exit 1
fi

echo "Platform data: $(cat "$PLATFORM_DIR/.pulled-at")"

# Skip if already initialized
if [ -d "$USE_CASE_DIR" ]; then
  echo "Use-case '$USE_CASE' already exists at $USE_CASE_DIR — skipping."
  exit 0
fi

mkdir -p "$USE_CASE_DIR"

# Write .env
cat > "$USE_CASE_DIR/.env" << EOF
PLATFORM_URL=$PLATFORM_URL
CLIENT_ID=$CLIENT_ID
CLIENT_SECRET=$CLIENT_SECRET
AUTH_METHOD=oauth
EOF

# Get initial token
"$SCRIPT_DIR/oauth-bootstrap.sh" "$USE_CASE_DIR/.env"

# Create empty task schema cache
echo "[]" > "$USE_CASE_DIR/task-schemas.json"

echo ""
echo "=== Use-case initialized: $USE_CASE ==="
echo "  $USE_CASE_DIR/"
echo "    .env              — credentials (gitignored)"
echo "    .auth.json        — bearer token (gitignored, auto-refreshed)"
echo "    task-schemas.json — task schema cache (populated on demand)"
echo ""
echo "Platform data (shared): $PLATFORM_DIR/"
echo "  openapi.json, tasks.json, apps.json, adapters.json, environment.md"
