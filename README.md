# Awesome AI and Digital Twins for Smart Farming

A curated research collection on AI-enabled agricultural digital twins, with precision irrigation as the main technical case. It connects governing equations, model calibration, physics-informed learning, and control to measurable soil moisture, irrigation delivery, consumptive water use, and crop outcomes.

**Collection:** 23 published scholarly papers, 1 technical guide, 1 preprint, 5 datasets, 7 tools, 5 implementations, and 7 learning resources. Last checked: **25 September 2026**. This is an AI-assisted, source-checked collection, not a claim that the student has independently reviewed every full text.

## Contents

- [Overview](#overview)
- [AI-Assisted Research Paper](#ai-assisted-research-paper)
- [Curated Research Papers](#curated-research-papers)
- [Datasets](#datasets)
- [Tools and Libraries](#tools-and-libraries)
- [GitHub Implementations](#github-implementations)
- [Tutorials and Learning Resources](#tutorials-and-learning-resources)
- [Modelling to Measurable Outcomes](#modelling-to-measurable-outcomes)
- [Citation Integrity Audit](#citation-integrity-audit)
- [Maintaining the Collection](#maintaining-the-collection)
- [Assignment and Repository Status](#assignment-and-repository-status)
- [License](#license)

## Overview

Agricultural digital twins link observations of a physical farm system to computational representations and management decisions. For irrigation, the physical system includes soil layers, crops, weather exposure, pumps, and valves. A useful twin must do more than display sensor readings: it should update the estimated field state, predict consequences of possible actions, and record whether irrigation was actually delivered. Human-approved recommendations and autonomous control are different operating modes and should be described honestly.

Artificial intelligence can assist with forecasting, state estimation, simulator approximation, and the interpretation of heterogeneous observations. Physical models remain important because water storage, infiltration, drainage, and crop demand constrain what a prediction can mean. This collection covers root-zone water balance, the Richardson-Richards equation, soil hydraulic relationships, crop models, parameter calibration, data assimilation, physics-informed neural networks, and model predictive control. Physics-informed learning is treated as a candidate method to compare against established alternatives, not as an automatic improvement.

The central research question is whether better modelling produces better decisions under field uncertainty. Soil-moisture accuracy, conservation error, metered irrigation volume, actual evapotranspiration, crop response, and operating cost are distinct outcomes. Satellite retrievals and reanalysis provide context, but neither automatically replaces local measurements or controlled field trials. Greenhouse and water-salt management studies broaden the application perspective while keeping site-specific evidence separate from universal performance claims.

## AI-Assisted Research Paper

**The Convergence of Artificial Intelligence and Digital Twins for Smart Farming: A Critical Review of Architectures, Applications, and Research Directions**

This critical narrative review connects twin architectures with physical modelling, calibration, assimilation, PINNs, and constrained irrigation decisions. It includes 12 numbered equations, 20 references, an architecture diagram, two comparison tables, and an illustrative irrigation calculation. It reports no new field experiment or measured water-saving percentage.

[Read the paper](paper/AI_Assisted_Research_Paper.pdf) | [Word manuscript](paper/Smart_Farming_Digital_Twins_Critical_Review.docx) | [Paper provenance](paper/README.md)

## Curated Research Papers

The [annotated bibliography](references/references.md) provides titles, authors, years, venues, primary links, relevance notes, and evidence limits. **R01-R20 correspond to references [1]-[20] in the paper.** R21-R25 extend the repository; they have not been silently added to the manuscript.

| Category | Resources | Purpose |
| --- | --- | --- |
| [Digital-twin reviews and architectures](references/references.md#digital-twin-reviews-and-architectures) | R01-R05 | Definitions, agricultural use cases, feedback, interoperability |
| [Soil physics and crop models](references/references.md#soil-physics-and-crop-models) | R07-R11, R23 | Conservation, hydraulic closure, crop-water response |
| [Calibration and physics-informed learning](references/references.md#calibration-and-physics-informed-learning) | R12-R17, R21 | State updating, inverse problems, PINNs, failure modes |
| [Smart-farming applications](references/references.md#smart-farming-applications) | R19-R20 | Irrigation-drainage and greenhouse case studies |
| [Data and evaluation foundations](references/references.md#data-and-evaluation-foundations) | R22, R24-R25 | Soil observations, reanalysis, spatial uncertainty |
| [Technical guide and preprint](references/references.md#technical-guide-and-preprint) | R06, R18 | FAO guidance and a labelled control preprint |

### Starting Papers

- **Digital twins in smart farming** - Verdouw, Tekinerdogan, Beulens, and Wolfert (2021), *Agricultural Systems*. [DOI](https://doi.org/10.1016/j.agsy.2020.103046). A framework connecting digital representations to farm management.
- **Forward and inverse modeling of water flow in unsaturated soils with discontinuous hydraulic conductivities using physics-informed neural networks with domain decomposition** - Bandai and Ghezzehei (2022), *Hydrology and Earth System Sciences*. [Paper](https://hess.copernicus.org/articles/26/4469/2022/). Soil-water PINNs with numerical comparisons and stated limitations.
- **Characterizing possible failure modes in physics-informed neural networks** - Krishnapriyan, Gholami, Zhe, Kirby, and Mahoney (2021), *NeurIPS*. [Proceedings](https://papers.neurips.cc/paper_files/paper/2021/hash/df438e5206f31600e6ae4af72f2725f1-Abstract.html). Evidence against treating physics residuals as guarantees of accuracy.
- **Digital twin-enabled intelligent irrigation-drainage system for precision water-salt management in saline agroecosystems** - Qin et al. (2025), *Agricultural Water Management*. [DOI](https://doi.org/10.1016/j.agwat.2025.109957). A physical implementation linking moisture, salt, and drainage management.
- **The International Soil Moisture Network: serving Earth system science for over a decade** - Dorigo et al. (2021), *Hydrology and Earth System Sciences*. [Paper](https://hess.copernicus.org/articles/25/5749/2021/). Background for selecting independent moisture observations.

## Datasets

The [dataset catalogue](datasets/datasets.md) records sources, access conditions, proposed uses, scales, and limitations. No third-party dataset is redistributed.

| Dataset | Research role | Important limit |
| --- | --- | --- |
| [ISMN](https://ismn.earth/data/data-download/) | In-situ moisture validation | Depth and irrigation records vary by station |
| [SMAP SPL3SMP_E v6](https://nsidc.org/data/spl3smp_e/versions/6) | Satellite surface-moisture context | Not field-scale root-zone truth |
| [ERA5-Land](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-land) | Historical land and weather context | Modelled reanalysis, not independent observations |
| [SoilGrids](https://docs.isric.org/globaldata/soilgrids/SoilGrids_faqs.html) | Soil-property priors | Predictions require local checking |
| [NASA POWER](https://power.larc.nasa.gov/) | Exploratory weather forcing | Historical forcing is not an operational forecast |

## Tools and Libraries

[Detailed catalogue](tools/tools.md): **DeepXDE**, **AquaCrop-OSPy**, **APSIM Next Generation**, **PCSE**, **do-mpc**, **Xarray**, and the **Crossref REST API**. They cover models, control, environmental arrays, and reference verification. None constitutes a field-ready digital twin on its own.

## GitHub Implementations

The [implementation review](implementations/github-repositories.md) records documentation, examples, license terms, activity snapshots, and limits for:

- [lululxvi/deepxde](https://github.com/lululxvi/deepxde): forward and inverse physics-informed modelling.
- [aquacropos/aquacrop](https://github.com/aquacropos/aquacrop): crop-water simulation and irrigation experiments.
- [APSIMInitiative/ApsimX](https://github.com/APSIMInitiative/ApsimX): modular agricultural simulation.
- [ajwdewit/pcse](https://github.com/ajwdewit/pcse): crop simulation components.
- [do-mpc/do-mpc](https://github.com/do-mpc/do-mpc): constrained model predictive control.

Project documentation and metadata were inspected; examples were **not executed** during this curation. APSIM has custom terms: public source visibility does not imply unrestricted reuse.

## Tutorials and Learning Resources

The [learning pathway](tutorials/learning-resources.md) links seven authoritative resources: FAO-56, AquaCrop-OSPy notebooks, DeepXDE inverse-problem demos, do-mpc documentation, the ISMN reader, NASA POWER API guidance, and the Xarray tutorial. Each entry explains its purpose.

## Modelling to Measurable Outcomes

The [research workflow](docs/research-workflow.md) connects sensing, modelling, calibration, decisions, and evaluation.

| Component | Observable or outcome |
| --- | --- |
| Water balance and Richards modelling | Storage changes, moisture by depth, drainage assumptions |
| Calibration and assimilation | Held-out errors, identifiable parameters, uncertainty, analysis increments |
| Physics-informed learning | Solution error, conservation, training and inference cost |
| Irrigation decisions | Timing, depth, metered volume, constraint violations |
| Agronomic value | Stress, yield or quality, water productivity, maintenance cost |

The paper's assumed one-hectare example converts an 18 mm net addition at a 0.90 delivery fraction into 20 mm gross irrigation, or 200 m3. This is illustrative arithmetic, not a field result, irrigation recommendation, or proof of savings.

## Citation Integrity Audit

[Audit](citation-audit/Citation_Integrity_Audit.md) | [PDF audit](citation-audit/Citation_Integrity_Audit.pdf) | [Reference evidence](references/verification.md)

The audit separates bibliographic checks, focused claim-support assessment, and arithmetic verification. Review evidence, numerical evidence, field cases, and proposed synthesis are distinguished. DOI existence alone does not prove claim support. Student full-text review remains necessary; no blanket human-verification claim is made.

## Maintaining the Collection

See [contribution rules](CONTRIBUTING.md). The bibliography is generated from [references.json](references/references.json); a [BibTeX export](references/references.bib) is included.

```sh
python3 scripts/build_catalog.py
python3 scripts/check_repository.py
```

Optional maintenance: `python3 scripts/check_links.py` refreshes the external-link report; `python3 -m unittest discover -s scripts -p 'test_*.py'` runs the checker tests. To regenerate the PDF audit after editing its Markdown source, install ReportLab and run `python3 scripts/render_audit.py`, then visually review every page. The other scripts use Python's standard library. Python 3.9 or newer is required.

The checker tests local links, counts, and assets, not scientific truth. [Remote link-check results](references/link-check.md) distinguish successful requests from blocked or inconclusive responses.

## Assignment and Repository Status

The local folder and Git remote retain the old repository name; no remote rename, commit, or push was performed. Suggested future name: **awesome-ai-digital-twins-smart-farming**.

The [Assignment 2 checklist](docs/assignment-2-checklist.md) records remaining student actions: topic-change approval, independent source review, naming and description, and genuine commit history. Previous-topic PDFs are preserved in the [historical archive](archive/previous-topic/README.md) and do not count toward this collection.

## License

Original content remains **unlicensed**, as requested by the owner. See the [status notice](LICENSE). Linked research, data, and software retain their own terms. No third-party research-paper PDFs are included in the active collection.
