# Phase 5 Decisions

## Browse / Filter / Search Decisions

- Kept the site static-first and avoided a heavy search backend.
- Implemented lightweight client-side filtering on pre-rendered cards rather than introducing a runtime indexer or framework change.
- Added filters where they provide the most practical value now:
  - productions
  - research
  - timeline
  - social archive
  - community
- Used section-based archive grouping instead of a fully unified mixed-type search interface.
  - Social records now have the richest filter surface.
  - Media appearances remain clearly surfaced and internally linked, but grouped as a dedicated archive section.

## Cross-Linking Decisions

- Treated Phase 5 as the point to make the archive graph visible, not just structurally present in JSON.
- Added conservative direct mappings only where the evidence already justified them.
- Used inverse-link synchronization to propagate valid relationships across the content graph.
- Normalized broken social-to-production references into real production slugs already present in the repo instead of preserving title-like placeholders.
- Added timeline detail pages and archive detail pages so cross-links could become practical navigation rather than hidden metadata.

## Bilingual Handling Decisions

- Added `translation_status` and `language_availability` as explicit record metadata.
- Preserved source-language evidence rather than inventing polished bilingual captions where recovery remained partial.
- Removed misleading English placeholder recovery notes from Arabic caption fields.
- Kept bilingual public summaries where they could be editorially translated safely from existing evidence.
- Preserved the existing route model:
  - English at root
  - Arabic under `/ar/`

## Source / Evidence Surfacing Decisions

- Added visible evidence-status panels instead of burying confidence and source context.
- Kept source-awareness practical rather than academic:
  - source labels
  - platform indicators
  - transcript links
  - recovered source-text blocks
  - surfaced document assets
- Reintroduced the evidence PDF and foundational research files only where they strengthened understanding of the structured experience.

## What Should Happen In Phase 6

- Keep the current JSON content model and static generator intact.
- Focus on visual and interaction polish instead of structural reinvention.
- Do manual Arabic UI QA and typography / spacing cleanup.
- Refine archive/media browse UX, especially around the split between social and media filtering.
- Improve transcript presentation and excerpt handling.
- Consider an entity layer only after the entity dataset is strong enough to justify public pages.
