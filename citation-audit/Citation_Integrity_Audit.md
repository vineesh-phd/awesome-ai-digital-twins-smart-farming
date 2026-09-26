# Citation Integrity Audit for the Smart-Farming Review

**Manuscript:** The Convergence of Artificial Intelligence and Digital Twins for Smart Farming: A Critical Review of Architectures, Applications, and Research Directions

**Literature checks:** 25 September 2026

**Method:** AI-assisted external metadata checks, selected primary-source passages, technical consistency review, and arithmetic verification.

**Status:** Bibliographic identity checked; focused claim assessment completed; independent student full-text review remains pending.

[Paper](../paper/AI_Assisted_Research_Paper.pdf) | [PDF audit](Citation_Integrity_Audit.pdf) | [Bibliography](../references/references.md) | [Per-reference evidence](../references/verification.md)

## Scope and Boundaries

This audit concerns the new smart-farming manuscript only. The previous-topic audit is historical and cannot support these claims. The manuscript's 20 references are retained as R01-R20. Five additional repository references, R21-R25, support software and dataset curation but are not cited in the manuscript.

The 25-item collection contains 23 published scholarly papers, a FAO technical guide, and a clearly identified control preprint. Bibliographic records were compared with Crossref/DOI metadata or authoritative FAO, NeurIPS, and arXiv records. Title, authors, year, venue, and identifier were checked. DOI year strings were not substituted for publication years. Full author lists and evidence URLs are retained in structured data.

These checks establish the identity of the cited works, not their universal scientific validity. Claim review is limited to the selected statements below and the source material available. Some application papers were accessible as publisher summaries rather than complete methods and results. No exhaustive sentence-level entailment audit, retraction-database screening, independent reproduction, plagiarism test, or human verification is claimed.

## Bibliographic Findings

- All 20 manuscript references have corresponding records in the new bibliography; none is missing from the manuscript-to-repository mapping.
- The 23 published-paper count excludes R06 (FAO-56) and R18 (arXiv control preprint).
- R01 uses DOI `10.1016/j.agsy.2020.103046` for the 2021 *Agricultural Systems* article.
- R03 is cited with publication year 2023 although its DOI contains 2022.
- R15 and R16 are distinct studies: the 2021 *Water Resources Research* constitutive-inference study and the 2022 *Hydrology and Earth System Sciences* domain-decomposition study.
- R23 describes AquaCrop-OS. It is not presented as the publication for the later Python implementation AquaCrop-OSPy.
- No DOI is invented for the FAO guide or the NeurIPS proceedings reference. Their authoritative records are linked instead.

## Focused Claim Assessment

The statements below are paraphrases identifying the claims assessed, not quotations from source papers. "Supported within scope" does not imply universal applicability.

| ID | Manuscript location and claim | Evidence | Assessment and limit |
| --- | --- | --- | --- |
| C01 | Section 3 distinguishes model, shadow, and twin by data-flow integration | R05; agricultural context R01-R04 | Supported within scope; manufacturing terminology is explicitly adapted, not declared a universal agricultural standard |
| C02 | Section 4 uses Richards flow to model unsaturated soil water | R07; formulation discussion in R16 | Consistent with upward-positive z and a root-extraction sink; assumptions and boundaries remain necessary |
| C03 | Equations (5)-(6) use retention and conductivity closure | R08-R09 | Standard model family identified; calibration is still required and the saturated branch is stated |
| C04 | Section 5 proposes a regularised parameter-estimation objective | Manuscript synthesis | Correctly labelled as a generic proposed objective, not a newly validated algorithm |
| C05 | Equation (8) illustrates sequential state correction | R12 | The linear-observation update is stated with the correct covariance structure; ensemble and nonlinear qualifications are retained |
| C06 | Section 6 combines data with differential-equation residuals in PINNs | R13-R14 | Supported within scope; no claim of guaranteed exact conservation or universal solver superiority |
| C07 | Layered-soil PINNs need attention to discontinuous hydraulic properties | R16, full-text methods and abstract | Supported; numerical comparisons, sensitivity to initialisation, and computational limitations are not converted into field-benefit claims |
| C08 | PINNs can suffer optimisation failure modes | R17, proceedings paper and author manuscript | Supported for the studied equation classes; not a statement that all PINNs fail |
| C09 | Neural surrogates can be used within irrigation zone MPC | R18, arXiv abstract/manuscript record | Supported as a numerical preprint contribution; not peer-reviewed field evidence |
| C10 | A twin-enabled irrigation-drainage application addresses water-salt management | R19, publisher summary | Supported at summary level; full study design and effect attribution require student review |
| C11 | Functional-structural plant modelling is used in a greenhouse twin case study | R20, publisher summary | Supported at summary level; transfer to open fields is not established |
| C12 | The one-hectare example yields 20 mm gross irrigation and 200 m3 | Manuscript assumptions and independent arithmetic | Correct under the stated assumptions; not a measured result or optimised treatment |
| C13 | The proposed architecture and validation protocol improve outcomes | Manuscript synthesis, Sections 3 and 8-10 | The paper proposes how to test improvement; it does not claim that improvement has already been demonstrated |

## Numerical and Modelling Checks

The illustrative example was recomputed independently: total available water = 1000 x 0.40 x (0.30 - 0.15) = 60 mm; readily available water = 0.50 x 60 = 30 mm; initial depletion = 1000 x 0.40 x (0.30 - 0.24) = 24 mm. With 6 mm ET loss and no other flux, depletion becomes 30 mm. A selected 12 mm target needs 18 mm net water, 18 / 0.90 = 20 mm gross, and 20 / 1000 x 10,000 = 200 m3. A moisture uncertainty of 0.02 gives 8 mm storage uncertainty. These checks are also encoded in the local repository checker.

The governing equations use stated units and sign conventions. The manuscript warns against double-counting losses already represented by delivery efficiency, distinguishes calibration from assimilation, logs analysis increments separately from physical fluxes, and separates irrigation application from consumptive use. The objective in Equation (11) is illustrative and dimensionally normalised; site-specific constraints are still required. This consistency check is not solver verification or validation against measured data.

## Resource Checks

Official providers and project pages were consulted for five datasets, seven tools, five implementations, and seven learning resources. The implementation record includes license findings and reported push timestamps. GitHub examples were not run. Data were not downloaded. Read the [external link report](../references/link-check.md) for access status: bot blocking, rate limits, and authentication do not prove a link is broken or that the underlying source was fully inspected.

## Required Student Follow-Up

1. Read the complete application studies R19-R20 and the central modelling studies; confirm study conditions, outcomes, and evidence limits.
2. Independently check the selected references and record completed human review rather than treating AI-assisted checks as personal verification.
3. Reassess claims if the manuscript changes; this audit does not automatically apply to later versions.
4. Confirm the teacher's approval of the topic change and review the [assignment checklist](../docs/assignment-2-checklist.md).
5. Check software terms and dataset conditions at the version actually used; execute and document baseline experiments before claiming reproducibility.

## Overall Assessment

The bibliography provides traceable identities and the selected claims are appropriately qualified at the assessed evidence level. The arithmetic is consistent. The manuscript remains a review draft with proposed research, not evidence that a deployed system achieves water savings. Full-text student curation, course approval, and future experimental validation remain separate responsibilities.
