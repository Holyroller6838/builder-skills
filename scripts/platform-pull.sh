#!/usr/bin/env bash
# Pull platform-wide data into platform/ directory.
# Run once per platform instance. Use --refresh to re-pull.
#
# Usage:
#   ./scripts/platform-pull.sh [--refresh] <platform-url> <client-id> <client-secret>
#
# Example:
#   ./scripts/platform-pull.sh https://platform.example.com client123 secret456
#   ./scripts/platform-pull.sh --refresh https://platform.example.com client123 secret456

set -euo pipefail

REFRESH=false
if [ "${1:-}" = "--refresh" ]; then
  REFRESH=true
  shift
fi

BASE="${1:?Usage: platform-pull.sh [--refresh] <platform-url> <client-id> <client-secret>}"
CLIENT_ID="${2:?Missing client ID}"
CLIENT_SECRET="${3:?Missing client secret}"
BASE="${BASE%/}"

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PLATFORM_DIR="$SCRIPT_DIR/../platform"
PULLED_AT_FILE="$PLATFORM_DIR/.pulled-at"

# Skip if already pulled and --refresh not set
if [ -f "$PULLED_AT_FILE" ] && [ "$REFRESH" = false ]; then
  echo "Platform data already pulled: $(cat "$PULLED_AT_FILE")"
  echo "Use --refresh to re-pull."
  exit 0
fi

mkdir -p "$PLATFORM_DIR"

echo "Authenticating to $BASE..."
TOKEN=$(curl -s "$BASE/oauth/token" \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode "client_id=$CLIENT_ID" \
  --data-urlencode "client_secret=$CLIENT_SECRET" \
  --data-urlencode 'grant_type=client_credentials' \
  | python3 -c "import json,sys; print(json.load(sys.stdin).get('access_token',''))")

if [ -z "$TOKEN" ]; then
  echo "ERROR: Authentication failed" >&2
  exit 1
fi
echo "Authenticated."

echo "Pulling OpenAPI spec..."
ENCODED_URL=$(python3 -c "import urllib.parse,sys; print(urllib.parse.quote(sys.argv[1], safe=''))" "$BASE")
curl -s "$BASE/help/openapi?url=$ENCODED_URL" -H "Authorization: Bearer $TOKEN" > "$PLATFORM_DIR/openapi.json"

echo "Pulling task catalog..."
curl -s "$BASE/workflow_builder/tasks/list" -H "Authorization: Bearer $TOKEN" > "$PLATFORM_DIR/tasks.json"

echo "Pulling apps list..."
curl -s "$BASE/automation-studio/apps/list" -H "Authorization: Bearer $TOKEN" > "$PLATFORM_DIR/apps.json"

echo "Pulling adapter health..."
curl -s "$BASE/health/adapters" -H "Authorization: Bearer $TOKEN" > "$PLATFORM_DIR/adapters.json"

echo "Pulling application health..."
curl -s "$BASE/health/applications" -H "Authorization: Bearer $TOKEN" > "$PLATFORM_DIR/applications.json"

echo "Generating environment summary..."
python3 - "$PLATFORM_DIR" << 'PYEOF'
import json, sys
from collections import Counter

d = sys.argv[1]
tasks = json.load(open(f"{d}/tasks.json"))
apps = json.load(open(f"{d}/apps.json"))
adapters_raw = json.load(open(f"{d}/adapters.json"))
applications_raw = json.load(open(f"{d}/applications.json"))

adapters = adapters_raw if isinstance(adapters_raw, list) else adapters_raw.get("results", [])
applications = applications_raw if isinstance(applications_raw, list) else applications_raw.get("results", [])

task_locations = Counter(t.get("location", "") for t in tasks)
task_apps = Counter(t.get("app", "") for t in tasks)

out = []
out.append("# Environment Overview\n")
out.append(f"**Total tasks in palette:** {len(tasks)}")
out.append(f"  - Application tasks: {task_locations.get('Application', 0)}")
out.append(f"  - Adapter tasks: {task_locations.get('Adapter', 0)}")
out.append(f"  - Broker tasks: {task_locations.get('Broker', 0)}\n")

out.append("## Applications\n")
out.append("| Application | State | Description | Task Count |")
out.append("|-------------|-------|-------------|------------|")
for a in sorted(applications, key=lambda x: x.get("id", "")):
    name = a.get("id", "")
    desc = (a.get("description", "") or "")[:60]
    count = task_apps.get(name, 0)
    out.append(f"| {name} | {a.get('state', '')} | {desc} | {count} |")
out.append("")

out.append("## Adapters\n")
out.append("| Instance Name | Adapter Type | Package | State | Task Count |")
out.append("|---------------|-------------|---------|-------|------------|")
for a in sorted(adapters, key=lambda x: x.get("id", "")):
    name = a.get("id", "")
    pkg = a.get("package_id", "")
    adapter_type = pkg.split("adapter-")[-1] if "adapter-" in pkg else pkg.split("/")[-1]
    count = task_apps.get(name, 0)
    out.append(f"| {name} | {adapter_type} | {pkg} | {a.get('state', '')} | {count} |")
out.append("")

out.append("## Top Task Sources\n")
out.append("| Source | Location | Task Count |")
out.append("|--------|----------|------------|")
for app, cnt in task_apps.most_common(20):
    loc = next((t.get("location", "") for t in tasks if t.get("app") == app), "")
    out.append(f"| {app} | {loc} | {cnt} |")

with open(f"{d}/environment.md", "w") as f:
    f.write("\n".join(out) + "\n")
PYEOF

# Write timestamp
PULLED_AT=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
printf "%s  %s\n" "$PULLED_AT" "$BASE" > "$PULLED_AT_FILE"

TASK_COUNT=$(python3 -c "import json; print(len(json.load(open('$PLATFORM_DIR/tasks.json'))))" 2>/dev/null || echo "?")
APP_COUNT=$(python3 -c "import json; d=json.load(open('$PLATFORM_DIR/apps.json')); print(len(d) if isinstance(d,list) else len(d.get('results',[])))" 2>/dev/null || echo "?")

echo ""
echo "=== Platform data pulled at $PULLED_AT ==="
echo "  $PLATFORM_DIR/"
echo "    openapi.json      — full API reference ($BASE)"
echo "    tasks.json        — $TASK_COUNT tasks"
echo "    apps.json         — $APP_COUNT apps/adapters"
echo "    adapters.json     — adapter instance details"
echo "    applications.json — application details"
echo "    environment.md    — summary with task counts"
