# Report: Lobben_2015

## Status
failed

## Paper directory
papers/Lobben_2015_InclusiveCartographicDesignOvercoming/ (not created — removed after confirming no PDF could be retrieved)

## Commit hash
n/a (no commit — nothing to add)

## Retrieval notes

Title search via Semantic Scholar cleanly resolved the intended paper and confirmed the canonical DOI is `10.1007/978-3-319-17738-0_7` (Lecture Notes in Geoinformation and Cartography, "Modern Trends in Cartography", pp 89-98). The disputed alternate DOI `10.1007/978-3-319-07926-4_7` did not surface in any search — it appears not to correspond to this chapter.

Retrieval via `fetch_paper.py` resolved metadata from S2 but returned `fallback_needed: true` with no open-access PDF URL. The waterfall then fell through to every open-access channel available:

- **Unpaywall API**: `oa_status: closed`, `has_repository_copy: false`, no OA locations, no repository embargoed copies. The paper is strictly closed-access.
- **Sci-Hub** (.st, .se, .ru mirrors): All three return "article is not in our database" for both DOI candidates. The .ru mirror explicitly says post-2021 publications are mostly unavailable since automatic download broke; this 2015 chapter was evidently never indexed.
- **Springer direct PDF URL** (`https://link.springer.com/content/pdf/10.1007/978-3-319-17738-0_7.pdf`): Returns a 289KB HTML document (redirect to paywalled landing page), not a PDF.
- **Springer chapter landing page**: No PDF download links present in DOM — paywalled.
- **Google Scholar**: Only yielded the same paywalled Springer URL with no side-bar OA link.
- **ResearchGate**: Publication 300782703 exists but the page is locked behind Cloudflare's "Temporarily Unavailable" bot-challenge and could not be reached through browser automation.
- **Anna's Archive** (.org, .se): Both mirrors DNS-blocked from this machine (`DNS_PROBE_FINISHED_NXDOMAIN`), could not query.
- **UNAM geography library** (`www.geografia.unam.mx/.../20190219100208.pdf`): A candidate surfaced by Google filetype search, but inspection showed a 4-page image-only PDF (book acquisition note / flyer), not the 10-page chapter (pp 89-98).
- **Faculty/lab pages**: Authors are affiliated with the Spatial Computation, Cognition, and Complexity Lab, Department of Geography, University of Oregon. No self-archived preprint PDF was surfaced by targeted Google searches on `site:uoregon.edu`, `Megen Brittell`, or variant queries.

Both DOIs from the PAPER_SPEC were tried: the primary `10.1007/978-3-319-17738-0_7` (which the Semantic Scholar lookup confirms is correct) and the `fallback_identifier` `10.1007/978-3-319-07926-4_7`. Neither produced a PDF via any channel.

## Extraction notes
Not reached. No PDF was obtained, so `paper-process` was not invoked.

## Files created
- notes.md: not created
- metadata.json: not created
- abstract.md: not created
- description.md: not created
- citations.md: not created
- pngs/: not created

Scratch notes file `notes/retrieve-Lobben_2015.md` was created with investigation trail.

## Issues / follow-ups

- **Paper is strictly paywalled with no reachable open-access copy.** Unpaywall's `has_repository_copy: false` combined with sci-hub's "not in database" and the failure of all alternate routes means a clean automated retrieval is not possible from this environment.
- Recommended next steps for Q:
  1. **Interlibrary loan** — most practical. The book "Modern Trends in Cartography" (2015, Springer LNGC, Eds. Brus/Vondráková/Voženílek) is widely held in academic libraries; the 10-page chapter should come through ILL quickly.
  2. **Email Amy Lobben or Megen Brittell directly** (Spatial Computation, Cognition, and Complexity Lab, Geography, University of Oregon) to request an author copy — this kind of book chapter is almost always shareable on request.
  3. **University access via Springer Link** — if Q has institutional access to Springer through a library, the chapter is directly downloadable at `https://link.springer.com/chapter/10.1007/978-3-319-17738-0_7`.
  4. If a PDF becomes available later by any of these routes, drop it in `papers/` root as `temp_lobben_2015.pdf` and rerun `research-papers:process-new-papers` — no special handling needed.
- **Note on the `fallback_identifier` in the PAPER_SPEC**: `10.1007/978-3-319-07926-4_7` does not appear to correspond to this chapter at all. The canonical DOI is unambiguously `10.1007/978-3-319-17738-0_7` per Semantic Scholar, Unpaywall, Google Scholar, and the Springer landing page.
