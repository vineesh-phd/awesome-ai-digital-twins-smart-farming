# Assignment 5 Error and Formatting Log

Final export check, 27 September: Overleaf compiled the approved-paragraph version to 13 pages with zero UI errors, zero warnings, and one bibliography-spacing information entry. After an idle session, stale download links produced empty files. Recompiling provided valid fresh downloads; no source change was needed. Only validated downloads are included in the submission. Final compiler evidence is in Evidence/overleaf-final-run.

**Student:** Vineesh Cutting | **Roll number:** RSI2026505

## Scope

These are actual conversion and formatting problems observed in the smart-farming source and addressed in the local LaTeX project. They are not fabricated Prism errors or a transcript of Prism suggestions. The first five entries document source-to-LaTeX preparation; compiler findings are recorded separately. The unchanged original PDF is included for comparison.

## 1 Equations Were Embedded Images

**Observed problem:** The Word manuscript contains its 12 displayed equations as rendered images. They cannot act as native LaTeX mathematics or automatically numbered LaTeX targets.

**Cause:** The original Word production workflow rendered equation strings into PNGs.

**Local correction:** Reused those exact equation strings inside numbered equation environments, with labels eq:1 through eq:12. The existing reference to Equations (2) and (3) now uses equation-reference commands.

**Verification:** Compare all 12 source expressions with main.tex, then inspect the compiled equations for signs, bounds, subscripts, and clipping. **Prism suggestion:** Recorded in the actual Prism follow-up below; this correction predates that session.

## 2 Citation Numbers Were Plain Text

**Observed problem:** Original citations such as [1-4] and [15,16] were text rather than references managed by a bibliography engine.

**Cause:** The manuscript originated in a Word/PDF workflow.

**Local correction:** Converted each citation to the corresponding R01-R20 BibTeX keys. Used a numeric, citation-order bibliography style and did not use nocite to force unrelated references into the list.

**Verification:** Confirm all cited keys exist, all 20 records are cited, and the final build contains no unresolved citation warnings. **Prism suggestion:** Recorded in the actual Prism follow-up below; this correction predates that session.

## 3 Figure and Table Numbers Were Hard Coded

**Observed problem:** References to Figure 1 and Tables 1 and 2 were typed numbers. No working section-reference command was present.

**Cause:** Fixed numbering in the original document does not provide LaTeX reference targets.

**Local correction:** Added unique figure, table, equation, and section labels. Converted the existing object references to dynamic references and added one navigation sentence pointing to the Introduction.

**Verification:** Confirm at least one resolved reference in each of the four required object categories. The navigation sentence adds no scientific claim. **Prism suggestion:** Recorded in the actual Prism follow-up below; this correction predates that session.

## 4 Word Tables Needed Native LaTeX Layout

**Observed problem:** Both source tables use wrapped Word cells and could not be copied as plain text without losing their row and column relationships.

**Cause:** The source and target formats have different layout systems.

**Local correction:** Extracted every cell, retained all headings, units, and captions, and generated booktabs tables with deliberate wrapping-column widths. No screenshot of a table is used as the replacement.

**Verification:** Compare the 7-by-4 literature table and 9-by-3 metrics table cell by cell, then inspect the compiled pages for overflow and legibility. **Prism suggestion:** Recorded in the actual Prism follow-up below; this correction predates that session.

## 5 Author Metadata Was Absent

**Observed problem:** The original smart-farming PDF contains the title, abstract, and keywords but no author or affiliation block.

**Cause:** The original review was prepared without author metadata.

**Local correction:** Added Vineesh Cutting and Indian Institute of Information Technology, Allahabad from the existing AS5 author record. The submission folder uses roll number RSI2026505 from Other_Docs.docx. The original PDF was not altered.

**Verification:** This is explicitly an addition from an existing student record, not a claim that absent metadata were preserved. The student should confirm the final author block. **Prism suggestion:** Recorded in the actual Prism follow-up below; this correction predates that session.

## Compiler Evidence

The first local build stopped at the first display equation with "Missing $ inserted". The conversion builder had inserted blank paragraph lines inside equation environments. Removing those internal blank lines fixed the syntax without changing any equation. The original failure log is retained as Evidence/first-local-build-failure.log. This was a local conversion error, not an error attributed to Prism.

First-pass undefined citation and cross-reference messages require bibliography processing and repeat LaTeX passes. Tectonic runs BibTeX and the required reruns automatically. Final validation checks the last log rather than mistaking initial unresolved references for a completed build.

The local compiler log and machine-readable checks are included in Evidence. Genuine platform evidence was subsequently obtained on 26 September 2026. Prism compiled successfully; the unchanged Prism export compiled in Overleaf on its first attempt. The full Overleaf log is retained under Evidence/overleaf-first-run and reports 13 pages, no undefined citations or references, and an underfull bibliography line (badness 1163). Overleaf's UI categorized that as one typesetting information entry, with zero errors and zero warnings. No source correction was needed for portability.

## Actual Prism Suggestions and Decisions

Prism Tasks 2-5 subsequently reviewed the equations, tables, bibliography, and three already corrected conversion problems. Task 5 confirmed removing paragraph breaks from equation environments, using keyed citations with bibliography passes, and placing labels after captions with dynamic object references. These suggestions corroborate existing fixes; they are not represented as Prism-caused errors.

Prism noted optional clarity risks: inconsistent vector/matrix typography in explanatory prose, narrow Table 1 cells, future overflow if Table 2 grows, and the unused label on an unnumbered Research Transparency section. The present document compiles and the label is not referenced, so no unrelated changes were made. The original figure and all table content were retained. External scientific validation was not claimed by these checks.

On 27 September, the student approved Prism's proposed paragraph revision. Task 7 changed only that paragraph and reported successful compilation, with the same unrelated bibliography spacing issue. A source diff independently confirmed the one-paragraph scope. A temporary Prism backend allocation error after the idle session was resolved by reloading; it was a connection issue, not a LaTeX error.
