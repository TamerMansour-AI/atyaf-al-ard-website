# Phase 5 Enrichment Report

## Scope

Phase 5 improved the existing structured Atyaf Al Ard site without replacing the Phase 4 foundation. The work stayed inside the current static repo, preserved the JSON content model, and focused on enrichment, cross-linking, browse usability, asset resurfacing, and bilingual/source-aware handling.

## Content Types Enriched

- `Production` records: 12
- `ResearchEntry` records: 5
- `SocialPost` records: 14
- `TimelineEvent` records: 14
- `MediaAppearance` records: 2
- `VolunteerOrSupportCall` records: 3
- Site singleton records: 4

Materially improved records in this phase: 54

## Metadata Improved

- Added `translation_status`, `language_availability`, and `source_platforms` across the structured content layer.
- Fixed broken relation values in social records and normalized them to real slugs already present in the repo.
- Added or refined `featured` / `flagship` surfacing to support home highlights and browse-level priority filters.
- Added asset references for foundational research materials, the evidence PDF, and site singleton hero/about assets.
- Corrected the foundational PDF source URLs so they resolve cleanly without the broken trailing slash pattern.
- Replaced misleading English placeholder text in Arabic social caption fields with explicit source-aware handling instead of pretending a translation existed.

## Cross-Links Added Or Strengthened

- Production ↔ Research relationships were synchronized and surfaced on detail pages.
- Production ↔ Social relationships were strengthened through normalized direct links and timeline-connected related-content blocks.
- Production ↔ Timeline relationships are now visible both on production detail pages and new timeline detail pages.
- Social ↔ Timeline links were filled in for the launch-window posts, May reel, mission post, Ramallah post, WhatsApp invite, and Palestine TV / volunteer post.
- Social ↔ Research links were added where the evidence clearly supported them, especially for the Canaanite fact and kitchen records plus the October mission post.
- MediaAppearance ↔ Timeline and VolunteerOrSupportCall ↔ Social / Timeline links are now visible on their own detail pages instead of existing only as hidden JSON arrays.
- Reverse-link syncing now keeps the content graph internally consistent instead of relying only on one-sided relation arrays.

## Browse Features Added

- New client-side browse controls were added to:
  - `/productions/`
  - `/research/`
  - `/timeline/`
  - `/archive/` social archive layer
  - `/community/`
- Filters now support combinations of:
  - content type
  - theme / tag
  - platform
  - year
  - language availability
  - featured / flagship priority
- Timeline detail pages were added for every timeline event.
- Archive detail pages were added for every social post and media appearance.
- Related-content blocks now appear across production, research, social, timeline, media, and community detail pages.
- The archive now behaves more like a browseable evidence layer instead of a list of external links.

## Assets Reintroduced

- Home hero:
  - `assets/videos/hero-atyaf-al-ard-loop.mp4`
  - `assets/images/home/hero-atyaf-al-ard-v1.png`
  - `assets/images/home/hero-fallback.jpg`
- About:
  - `assets/images/about/about-founders-portal.png`
  - `assets/images/about/about-founders-portal-ar.png`
- Research:
  - `assets/images/research/foundational-overview-en.png`
  - `assets/images/research/foundational-overview-ar.png`
  - `assets/images/research/jericho-continuity-en.png`
  - `assets/images/research/jericho-continuity-ar.png`
  - `assets/docs/research/foundational-overview-en.pdf`
  - `assets/docs/research/foundational-overview-ar.pdf`
  - `assets/docs/research/foundational-overview-en.txt`
  - `assets/docs/research/foundational-overview-ar.txt`
  - `assets/Palestine_Evidence_Narrative.pdf`

## Intentionally Deferred

- A full visual redesign or brand-system overhaul
- A framework rewrite or CMS introduction
- Entity detail pages as a first-class public layer
- Transcript translation or polished transcript excerpt presentation
- Raw screenshot galleries from the workspace-only Facebook recovery folders
- A heavyweight full-text search backend
- A single universal mixed-type archive search interface beyond the current section-level browse approach
