# Assignment 6: ACM CSUR Review Paper

**Vineesh Cutting - RSI2026505**  
**AI Tools for Research - Mid-Semester Evaluation**

Paper: **The Convergence of Artificial Intelligence and Digital Twins for Smart Farming: A Critical Review of Architectures, Applications, and Research Directions**.

## Submission Files

- `Smart_Farming_Digital_Twins_ACM_CSUR.pdf`: updated review paper.
- `LaTeX_Source.zip`: complete clean source project. Open `main.tex`; use BibTeX and a current TeX Live environment.
- `main.tex`, `references.bib`, `Figures/`, `acmart.cls`, and `ACM-Reference-Format.bst`: editable source and required resources.
- `Vendor/`: third-party ACM source and notices accompanying the template files.

The [compliance checklist](Assignment_6_Checklist.md) maps every assignment requirement to the manuscript. `Evidence/` contains provenance and validation records, not additional required submission reports.

## Current Status

**Completed; final student review remains.** The genuine Overleaf PDF has 16 pages, 3 figures, 5 tables, 12 equations, and 20 references. All pages were rendered and visually inspected. There are zero compilation errors, unresolved citations/references, or overfull boxes. All earlier main sections and mathematical equations were retained, including the approved calibration paragraph.

The separate [Assignment 6 Overleaf project](https://www.overleaf.com/project/6ab96bb19ede0f3877019950) was created from the official ACM template. The manuscript, bibliography, and all three figures were uploaded; `main.tex` was selected and compiled with pdfLaTeX / TeX Live 2026. The downloaded source files were compared byte-for-byte with the prepared files. The final paper PDF and compiler logs are genuine platform exports.

Two non-fatal BibTeX warnings remain for missing publisher/address fields in R17 (NeurIPS 2021). The official title, authors, proceedings, volume, pages, year, and URL are present; no address was invented to suppress the warning. Two underfull vertical-box notices concern page spacing, not clipped text. The independent local Tectonic build produced 17 pages because its engine/fonts paginate differently; the submission PDF is the 16-page Overleaf build.

Nothing has been submitted to Classroom or ACM, committed, or pushed. Final student review remains necessary.

## Build and Reuse

Use the official template's default pdfLaTeX compiler in Overleaf, with `main.tex` as the main document and active editor file. For a local installation: `pdflatex main`, `bibtex main`, then run `pdflatex main` twice. A local XeTeX/Tectonic build has also been tested; pagination can vary by engine.

Original documentation, manuscript, and diagrams remain unlicensed. ACM resources retain their own notices, detailed in [Vendor/README.md](Vendor/README.md). The supplied XAI sample paper is a formatting reference and is not redistributed in this package.
