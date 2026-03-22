# Direct-to-Main Workflow Update

## What changed
- The GitHub Actions workflow now runs full validation on `push` to `main`.
- The workflow also allows optional manual runs through `workflow_dispatch`.
- The previous `pull_request` trigger was removed.
- `codex/**` branch-specific handling was removed from the workflow.

## What stays useful
- The validation script remains in `.github/scripts/validate_site.py`.
- It still performs the full static-site checks against the repo's route manifest and internal links.

## What was updated in docs
- `05_reports/CODEX_GITHUB_FIRST_WORKFLOW_PLAN.md` now records that the old Codex-branch workflow is superseded.
- This report documents the new direct-to-main strategy so future Codex work has one clear path.

## How Codex should work now
- Work directly on `main`.
- Push changes directly to `origin/main`.
- Use workflow dispatch only when you want a manual validation run.
- Do not rely on `codex/**` branches for this repo's normal workflow.

## Result
- The repo is configured for a direct-to-main workflow.
- GitHub Actions is now aligned with that model.
