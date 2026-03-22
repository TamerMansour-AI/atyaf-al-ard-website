# Codex GitHub-First Workflow Plan

## Current state
- The repo did not have any `.github/workflows` files before this change.
- That meant GitHub Actions had no existing branch or event triggers to inspect or extend.
- The site is a static HTML repository, so the right first step is a small validation workflow instead of a framework-specific build pipeline.

## Recommended GitHub-first workflow
- Use `codex/<scope>` branches for all Codex work.
- Never push Codex changes directly to `main`.
- Open a pull request from `codex/<scope>` into `main` as the normal handoff path.
- Keep `main` as the only branch that represents reviewed, merged site state.

## Actions trigger policy
- `pull_request` targeting `main`: run full validation.
- `push` to `main`: run full validation again after merge.
- `push` to `codex/**`: run only smoke validation, not deploy/release jobs.

## Why this split works
- Codex branches stay fast and low-noise.
- PRs still get the real validation pass before merge.
- `main` remains the authoritative branch for merged content.
- The repo stays GitHub-native without forcing a heavier CI stack than the site needs.

## Workflow file added
- `.github/workflows/github-first-ci.yml`

## Validation script added
- `.github/scripts/validate_site.py`

## Phase 6 recommendation
- Keep this workflow, then add branch protection for `main` and require the validation checks before merge.
- If GitHub Pages or another publish target is added later, wire deployment only to `push` on `main`.
- Leave `codex/**` as validation-only branches unless you deliberately want preview deployments later.
