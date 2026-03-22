#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parents[2]
BASE_HREF = "/atyaf-al-ard-website/"
ASSET_ATTR_RE = re.compile(r'(?:href|src|poster|data-src)=["\']([^"\']+)["\']', re.IGNORECASE)
BASE_TAG_RE = re.compile(r'<base\s+href=["\']([^"\']+)["\']', re.IGNORECASE)


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise SystemExit(f"Missing required file: {path.relative_to(ROOT)}")
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid JSON in {path.relative_to(ROOT)}: {exc}")


def resolve_link(raw: str, base_href: str) -> Path | None:
    raw = raw.strip()
    if not raw or raw.startswith("#"):
        return None

    parts = urlsplit(raw)
    if parts.scheme or parts.netloc:
        return None

    path = parts.path
    if not path:
        return None

    normalized = path
    if normalized.startswith(base_href):
        normalized = normalized[len(base_href) :]
        return (ROOT / normalized).resolve()

    if normalized.startswith("/"):
        return (ROOT / normalized.lstrip("/")).resolve()

    return (ROOT / normalized).resolve()


def candidate_paths(path: Path) -> list[Path]:
    candidates = [path]
    if path.suffix == "":
        candidates.append(path.with_suffix(".html"))
        candidates.append(path / "index.html")
    return candidates


def exists_any(path: Path) -> bool:
    return any(candidate.exists() for candidate in candidate_paths(path))


def validate_routes(manifest: dict) -> list[str]:
    problems: list[str] = []
    routes = manifest.get("routes", [])
    if manifest.get("route_count") != len(routes):
        problems.append(
            f"route_count mismatch: manifest says {manifest.get('route_count')} but routes array has {len(routes)}"
        )

    seen: set[str] = set()
    for route in routes:
        relative_path = route.get("relative_path")
        route_name = route.get("route", "<unknown>")
        if not relative_path:
            problems.append(f"route {route_name} is missing relative_path")
            continue
        if relative_path in seen:
            problems.append(f"duplicate relative_path in route manifest: {relative_path}")
        seen.add(relative_path)

        target = ROOT / relative_path
        if not exists_any(target):
            problems.append(f"missing route target for {route_name}: {relative_path}")

    return problems


def extract_base_href(sample_file: Path) -> str:
    text = sample_file.read_text(encoding="utf-8")
    match = BASE_TAG_RE.search(text)
    if match:
        href = match.group(1).strip()
        if href:
            return href
    return BASE_HREF


def validate_links() -> list[str]:
    problems: list[str] = []
    base_href = extract_base_href(ROOT / "index.html")

    for html_path in ROOT.rglob("*.html"):
        if ".git" in html_path.parts or ".github" in html_path.parts:
            continue

        html_text = html_path.read_text(encoding="utf-8")
        for raw in ASSET_ATTR_RE.findall(html_text):
            resolved = resolve_link(raw, base_href)
            if resolved is None:
                continue
            if not exists_any(resolved):
                problems.append(
                    f"{html_path.relative_to(ROOT)} -> {raw} does not resolve to an existing file"
                )

    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate the Atyaf Al Ard static site.")
    parser.add_argument("--full", action="store_true", help="Run the deeper cross-link validation pass.")
    args = parser.parse_args()

    manifest_path = ROOT / "07_manifests" / "phase_5_route_manifest.json"
    manifest = load_json(manifest_path)

    problems = validate_routes(manifest)
    if args.full:
        problems.extend(validate_links())

    if problems:
        label = "full" if args.full else "smoke"
        print(f"{label} validation failed with {len(problems)} issue(s):")
        for problem in problems[:50]:
            print(f"- {problem}")
        if len(problems) > 50:
            print(f"- ... and {len(problems) - 50} more")
        return 1

    if args.full:
        print(
            f"Full validation passed: {len(manifest.get('routes', []))} routes checked and internal links resolved."
        )
    else:
        print(
            f"Smoke validation passed: {len(manifest.get('routes', []))} manifest routes verified."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
