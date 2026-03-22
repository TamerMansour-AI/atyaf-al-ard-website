# Codex GitHub Workflow Plan

This document is superseded by the direct-to-main workflow update.

## Current state
- The repo now uses a direct-to-main GitHub workflow.
- The site is a static HTML repository, so the right fit is a single validation workflow rather than a PR-gated or branch-specific pipeline.

## Current workflow
- Codex should work directly on `main` for this repo.
- Changes should be pushed straight to `origin/main`.
- `codex/**` branch handling is retired for the website workflow.

## Actions trigger policy
- `push` to `main`: run full validation again after merge.
- `workflow_dispatch`: allow a manual full validation run when needed.

## Why this split works
- `main` is the single source of truth.
- Every push gets the same validation path.
- Manual dispatch is available for extra verification without reintroducing branch complexity.

## Workflow file added
- `.github/workflows/github-first-ci.yml`

## Validation script added
- `.github/scripts/validate_site.py`

## Phase 6 recommendation
- Keep the direct-to-main workflow and add branch protection only if you later want to prevent accidental pushes.
- If GitHub Pages or another publish target is added later, wire deployment only to `push` on `main`.
