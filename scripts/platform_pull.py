#!/usr/bin/env python3
"""
Pull platform-wide data into platform/ directory.
Run once per platform instance. Use --refresh to re-pull.

Usage:
    python scripts/platform_pull.py <platform-url> <client-id> <client-secret>
    python scripts/platform_pull.py --refresh <platform-url> <client-id> <client-secret>
"""

import argparse
import json
import sys
import urllib.parse
import urllib.request
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


PLATFORM_DIR = Path(__file__).parent.parent / "platform"
PULLED_AT_FILE = PLATFORM_DIR / ".pulled-at"


def fetch(url, token=None, label=None):
    req = urllib.request.Request(url)
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    if label:
        print(f"  Pulling {label}...")
    with urllib.request.urlopen(req) as resp:
        return resp.read()


def authenticate(base, client_id, client_secret):
    print(f"Authenticating to {base}...")
    data = urllib.parse.urlencode({
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
    }).encode()
    req = urllib.request.Request(
        f"{base}/oauth/token",
        data=data,
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    with urllib.request.urlopen(req) as resp:
        token = json.loads(resp.read()).get("access_token", "")
    if not token:
        print("ERROR: Authentication failed — no access_token in response", file=sys.stderr)
        sys.exit(1)
    print("Authenticated.")
    return token


def generate_environment_summary(d: Path):
    tasks = json.loads((d / "tasks.json").read_text())
    apps_raw = json.loads((d / "apps.json").read_text())
    adapters_raw = json.loads((d / "adapters.json").read_text())
    applications_raw = json.loads((d / "applications.json").read_text())

    apps = apps_raw if isinstance(apps_raw, list) else apps_raw.get("results", [])
    adapters = adapters_raw if isinstance(adapters_raw, list) else adapters_raw.get("results", [])
    applications = applications_raw if isinstance(applications_raw, list) else applications_raw.get("results", [])

    task_locations = Counter(t.get("location", "") for t in tasks)
    task_apps = Counter(t.get("app", "") for t in tasks)

    lines = [
        "# Environment Overview\n",
        f"**Total tasks in palette:** {len(tasks)}",
        f"  - Application tasks: {task_locations.get('Application', 0)}",
        f"  - Adapter tasks: {task_locations.get('Adapter', 0)}",
        f"  - Broker tasks: {task_locations.get('Broker', 0)}\n",
        "## Applications\n",
        "| Application | State | Description | Task Count |",
        "|-------------|-------|-------------|------------|",
    ]
    for a in sorted(applications, key=lambda x: x.get("id", "")):
        name = a.get("id", "")
        desc = (a.get("description", "") or "")[:60]
        lines.append(f"| {name} | {a.get('state', '')} | {desc} | {task_apps.get(name, 0)} |")

    lines += [
        "",
        "## Adapters\n",
        "| Instance Name | Adapter Type | Package | State | Task Count |",
        "|---------------|-------------|---------|-------|------------|",
    ]
    for a in sorted(adapters, key=lambda x: x.get("id", "")):
        name = a.get("id", "")
        pkg = a.get("package_id", "")
        adapter_type = pkg.split("adapter-")[-1] if "adapter-" in pkg else pkg.split("/")[-1]
        lines.append(f"| {name} | {adapter_type} | {pkg} | {a.get('state', '')} | {task_apps.get(name, 0)} |")

    lines += [
        "",
        "## Top Task Sources\n",
        "| Source | Location | Task Count |",
        "|--------|----------|------------|",
    ]
    for app, cnt in task_apps.most_common(20):
        loc = next((t.get("location", "") for t in tasks if t.get("app") == app), "")
        lines.append(f"| {app} | {loc} | {cnt} |")

    (d / "environment.md").write_text("\n".join(lines) + "\n")


def main():
    parser = argparse.ArgumentParser(description="Pull platform-wide data into platform/")
    parser.add_argument("--refresh", action="store_true", help="Re-pull even if data already exists")
    parser.add_argument("platform_url", help="Platform base URL")
    parser.add_argument("client_id", help="OAuth client ID")
    parser.add_argument("client_secret", help="OAuth client secret")
    args = parser.parse_args()

    base = args.platform_url.rstrip("/")

    # Skip if already pulled
    if PULLED_AT_FILE.exists() and not args.refresh:
        print(f"Platform data already pulled: {PULLED_AT_FILE.read_text().strip()}")
        print("Use --refresh to re-pull.")
        return

    PLATFORM_DIR.mkdir(exist_ok=True)

    token = authenticate(base, args.client_id, args.client_secret)

    encoded_base = urllib.parse.quote(base, safe="")

    files = {
        "openapi.json": f"{base}/help/openapi?url={encoded_base}",
        "tasks.json": f"{base}/workflow_builder/tasks/list",
        "apps.json": f"{base}/automation-studio/apps/list",
        "adapters.json": f"{base}/health/adapters",
        "applications.json": f"{base}/health/applications",
    }

    for filename, url in files.items():
        data = fetch(url, token=token, label=filename)
        (PLATFORM_DIR / filename).write_bytes(data)

    print("  Generating environment.md...")
    generate_environment_summary(PLATFORM_DIR)

    pulled_at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    PULLED_AT_FILE.write_text(f"{pulled_at}  {base}\n")

    task_count = len(json.loads((PLATFORM_DIR / "tasks.json").read_text()))
    apps_raw = json.loads((PLATFORM_DIR / "apps.json").read_text())
    app_count = len(apps_raw) if isinstance(apps_raw, list) else len(apps_raw.get("results", []))

    print(f"\n=== Platform data pulled at {pulled_at} ===")
    print(f"  {PLATFORM_DIR}/")
    print(f"    openapi.json      — full API reference ({base})")
    print(f"    tasks.json        — {task_count} tasks")
    print(f"    apps.json         — {app_count} apps/adapters")
    print(f"    adapters.json     — adapter instance details")
    print(f"    applications.json — application details")
    print(f"    environment.md    — summary with task counts")


if __name__ == "__main__":
    main()
