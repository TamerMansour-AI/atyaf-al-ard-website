# Phase 6B-1 Decisions

## Design System Decisions
- Keep the current static architecture and layered CSS approach rather than introducing a framework or component rewrite.
- Use Phase 6B-1 to establish the new visual grammar centrally in `assets/css/structured.css`, so later phases inherit the same palette, spacing, typography, and card language.
- Move the site away from generic rounded beige cards by giving each surface more tonal depth, edge treatment, and editorial weight.
- Use darker hero and emphasis surfaces selectively, not everywhere, so the site feels cinematic without becoming uniformly heavy.

## Homepage Decisions
- Treat the homepage as the primary lever for perceived quality improvement before touching the rest of the site.
- Use existing safe assets only in this phase; do not wait for newly generated artwork before upgrading the homepage.
- Reframe the homepage around visitor entry paths and project meaning, not just content buckets.
- Keep flagship productions, foundational research, timeline events, archive signals, and support paths all present, but sequence them more intentionally.

## Bilingual Decisions
- Give Arabic equal structural importance to English in this phase rather than postponing Arabic quality to later polish.
- Improve Arabic visual dignity through typography choices, spacing rules, and copy rewriting instead of relying on raw mirrored layouts.
- Keep bilingual parity in homepage architecture while allowing the Arabic copy to be phrased more naturally.

## Technical Decisions
- Limit Phase 6B-1 code changes to shared CSS, the English homepage, the Arabic homepage, and the structured home content record.
- Preserve all current routes, content loading behavior, and linked detail pages.
- Validate with the existing repo validator and local headless browser screenshots rather than introducing a new testing system.

## Deferred To Phase 6B-2 And Later
- section index redesigns beyond the homepage
- section-specific visual identities for archive, research, productions, and timeline
- broader detail-page elevation
- new visual asset generation and cleanup workflows
- richer motion design
- full bilingual QA pass across the entire site
