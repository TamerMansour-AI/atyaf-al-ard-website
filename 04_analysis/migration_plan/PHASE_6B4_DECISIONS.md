# Phase 6B-4 Decisions

## Asset System Direction
- Chose a controlled SVG-led system instead of a broad raster-image generation pass.
- Kept the visual language symbolic, editorial, and warm rather than photoreal or generically AI-illustrated.
- Used one coherent family across homepage, sections, flagship productions, and research dossier presentation.

## Integration Decisions
- Integrated the strongest assets first where they would be most visible:
  - homepage hero
  - homepage browse routes
  - productions index
  - research index
  - flagship production detail heroes
  - key research dossier/detail pages
- Used CSS-driven section hero backgrounds so every index page gained a distinct anchor visual without route or template churn.
- Replaced fragile remote YouTube thumbnails on flagship detail pages with local cover treatments.

## Bilingual Decisions
- Kept most new assets language-neutral so English and Arabic pages could share them without duplication.
- Mirrored the homepage visual row and route-card icon treatment into Arabic.
- Mirrored flagship production cover replacements and key dossier visuals into Arabic detail pages where it mattered most.

## Performance Decisions
- Preferred SVG over new large PNG/JPG assets.
- Reused strong existing documentary images only where they still provided factual value.
- Avoided adding multiple heavy visuals per page.

## Tooling Decisions
- Used local authoring for the asset family in this phase.
- Did not depend on Freepik / Nano Banana 2 for this pass because:
  - the most immediate quality jump came from a coherent in-repo vector system
  - the browser control path for external generation remained unreliable during execution

## What Was Deferred
- Large-batch external image generation.
- A fuller cinematic still library for more production pages.
- More bespoke visual treatments for lower-priority detail pages.
- Section-specific Arabic editorial illustration variations.
- Final polish of every evidence/document packet page.

## Recommended Next Move
- Phase 6B-5 should extend the asset-aware treatment into a broader detail-page sweep and media/archive surfaces, then do a tighter bilingual polish pass with selective additional image generation only where the current SVG system is no longer enough.
