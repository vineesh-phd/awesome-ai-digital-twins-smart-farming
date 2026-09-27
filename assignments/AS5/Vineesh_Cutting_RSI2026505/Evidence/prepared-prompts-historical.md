# Historical Preparation Prompts

These prompts were prepared before the actual platform session; their pending labels are historical, not current status.

## 1 Text Conversion

**Prompt prepared:** Convert the supplied smart-farming manuscript into LaTeX. Preserve the exact title, abstract, keywords, paragraph order, all existing sections and subsections, scientific meaning, numerical values, limitations, and citations. Do not shorten the paper or add experimental results. Keep Research Transparency. Use the supplied author information only; distinguish it from the author block absent in the original PDF.

**Local action:** All original manuscript prose and section headings were converted; author details were sourced from existing AS5 records. **Prism response and decision:** Pending actual run and student review.

## 2 Equations

**Prompt prepared:** Check the 12 supplied LaTeX equations against the original paper. Preserve each operator, sign, subscript, superscript, parameter bound, and numerical value. Check the upward-positive coordinate convention in the Richards equation and the root-extraction sign. Use numbered equation environments and unique labels. Report ambiguities without guessing and do not replace equations with images.

**Local action:** The original equation strings were retained in editable equation environments. **Prism response and decision:** Pending actual run and student review.

## 3 Tables

**Prompt prepared:** Convert both supplied tables into publication-quality LaTeX using booktabs and wrapping columns. Preserve all rows, headings, units, evidence limitations, and captions. Keep each table within the text width, use readable type, and reference it through a label. Do not invent performance measurements or round any value.

**Local action:** All cells were taken from the source Word tables and converted into native LaTeX. **Prism response and decision:** Pending actual run and student review.

## 4 Figure and Cross References

**Prompt prepared:** Insert Figures/irrigation_digital_twin_architecture.png without cropping or redrawing it. Preserve the original caption. Verify unique labels and working references for the figure, both tables, referenced equations, and at least one section. Replace hard-coded object numbers with reference commands without changing the meaning of surrounding text.

**Local action:** The original figure file is included; figure, table, equation, and section labels were added. **Prism response and decision:** Pending actual run and student review.

## 5 BibTeX and Citations

**Prompt prepared:** Use the supplied references.bib containing R01-R20. Convert each original numeric citation into a citation command referencing the same work. Preserve the distinction between the FAO guide, the arXiv preprint, and published papers. Do not invent metadata, add uncited R21-R25 repository resources, or use a blanket nocite command to conceal missing citations. Check for missing and unused keys.

**Local action:** The 20 manuscript records were exported from the verified repository catalogue. **Prism response and decision:** Pending actual run and student review.

## 6 Debugging

**Prompt prepared:** Inspect the attached main.tex, bibliography, figure paths, and actual compilation log. Identify each error or formatting problem, explain its cause, and propose the smallest correction. Check unresolved citations, unresolved labels, missing assets, and overfull boxes. Do not rewrite unrelated text. Separate problems visible in this log from hypothetical warnings.

**Local action:** A local compiler and preservation checks are used; actual findings belong in Error_Log.pdf. **Prism response and decision:** Pending actual run and student review.

## 7 Paragraph Revision

**Prompt prepared:** Improve the supplied paragraph beginning "Calibration estimates model parameters" for clarity and scientific style. Preserve the distinctions among model-parameter calibration, state assimilation, and sensor calibration. Preserve the warning about compensating for sensor bias, incorrect irrigation input, or water-table influence. Do not introduce a new result or imply that any method eliminates these errors. Return the revision separately from the manuscript.

**Local action:** An original paragraph and a Codex-assisted candidate are retained in Verification_and_Comparison.pdf. The paper itself keeps the original paragraph. **Prism response and decision:** Pending actual run and student verification of Version C.

## 8 Consistency and Portability

**Prompt prepared:** Report inconsistencies in terminology, abbreviations, variables, units, captions, figure paths, citation keys, and cross-references without rewriting the paper. Then check whether the complete exported project uses relative paths and includes main.tex, references.bib, and Figures. Record the first Overleaf compilation of the unchanged export separately from any later corrections; do not claim success without the actual log.

**Local action:** Relative paths and complete project packaging are checked locally. **Prism response, acceptance decision, and Overleaf result:** Pending actual runs.
