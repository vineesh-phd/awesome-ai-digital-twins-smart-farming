# Annotated Research Bibliography

[Back to collection](../README.md)

Checked: 2026-09-25. **23 published scholarly papers**, plus a technical guide and a preprint.

R01-R20 preserve manuscript numbering. R21-R25 are repository additions. Complete author lists are in [references.json](references.json); long lists below use et al. See [verification records](verification.md) and the [claim audit](../citation-audit/Citation_Integrity_Audit.md).

## Digital-Twin Reviews and Architectures

### R01 Digital twins in smart farming

Verdouw, Cor; Tekinerdogan, Bedir; Beulens, Adrie; Wolfert, Sjaak (2021). *Agricultural Systems, 189, 103046*.

[Primary record](https://doi.org/10.1016/j.agsy.2020.103046) | **Type:** published-paper

**Relevance:** Connects digital representations to smart-farming management cycles.

**Evidence limit:** Conceptual architecture and use cases do not establish universal water savings.

### R02 Introducing digital twins to agriculture

Pylianidis, Christos; Osinga, Sjoukje; Athanasiadis, Ioannis N. (2021). *Computers and Electronics in Agriculture, 184, 105942*.

[Primary record](https://doi.org/10.1016/j.compag.2020.105942) | **Type:** published-paper

**Relevance:** Maps early agricultural digital-twin use cases and adoption pathways.

**Evidence limit:** A historical review should not be treated as a current census of deployments.

### R03 Digital Twins in Agriculture: A State-of-the-art review

Purcell, Warren; Neubauer, Thomas (2023). *Smart Agricultural Technology, 3, 100094*.

[Primary record](https://doi.org/10.1016/j.atech.2022.100094) | **Type:** published-paper

**Relevance:** Reviews agricultural digital-twin definitions, applications, and integration.

**Evidence limit:** Definitions and maturity vary across the reviewed systems.

### R04 Digital twins in agriculture: A systematic literature review on modeling, semantics, and interoperability

Morgan Pereira, Pedro Henrique; Costa Piazza, Giovana; Usman, Khalid; Santos Comelli da Silveira, Luan; Cella Ceriotti, Vinícius; de Souza Pazin, Yuri; et al. (2026). *Smart Agricultural Technology, 14, 102283*.

[Primary record](https://doi.org/10.1016/j.atech.2026.102283) | **Type:** published-paper

**Relevance:** Examines agricultural modelling, semantic representation, and interoperability.

**Evidence limit:** Its literature corpus is not the search corpus of the accompanying narrative review.

### R05 Digital Twin in manufacturing: A categorical literature review and classification

Kritzinger, Werner; Karner, Matthias; Traar, Georg; Henjes, Jan; Sihn, Wilfried (2018). *IFAC-PapersOnLine, 51(11), 1016-1022*.

[Primary record](https://doi.org/10.1016/j.ifacol.2018.08.474) | **Type:** published-paper

**Relevance:** Provides the model, shadow, and twin data-flow classification used for careful terminology.

**Evidence limit:** A manufacturing taxonomy needs contextual adaptation to agriculture.

## Soil Physics and Crop Models

### R07 CAPILLARY CONDUCTION OF LIQUIDS THROUGH POROUS MEDIUMS

Richards, L. A. (1931). *Physics, 1(5), 318-333*.

[Primary record](https://doi.org/10.1063/1.1745010) | **Type:** published-paper

**Relevance:** Supplies the physical foundation for capillary flow in porous media.

**Evidence limit:** A governing equation alone does not determine local parameters or boundary conditions.

### R08 A Closed-form Equation for Predicting the Hydraulic Conductivity of Unsaturated Soils

van Genuchten, M. Th. (1980). *Soil Science Society of America Journal, 44(5), 892-898*.

[Primary record](https://doi.org/10.2136/sssaj1980.03615995004400050002x) | **Type:** published-paper

**Relevance:** Defines a widely used soil-water retention and conductivity relationship.

**Evidence limit:** The functional form does not remove parameter uncertainty or represent every soil process.

### R09 A new model for predicting the hydraulic conductivity of unsaturated porous media

Mualem, Yechezkel (1976). *Water Resources Research, 12(3), 513-522*.

[Primary record](https://doi.org/10.1029/wr012i003p00513) | **Type:** published-paper

**Relevance:** Provides the conductivity model paired with the van Genuchten retention relationship.

**Evidence limit:** Hydraulic closure requires calibration and a stated domain of validity.

### R10 APSIM - Evolution towards a new generation of agricultural systems simulation

Holzworth, Dean P.; Huth, Neil I.; deVoil, Peter G.; Zurcher, Eric J.; Herrmann, Neville I.; McLean, Greg; et al. (2014). *Environmental Modelling & Software, 62, 327-350*.

[Primary record](https://doi.org/10.1016/j.envsoft.2014.07.009) | **Type:** published-paper

**Relevance:** Explains a modular agricultural systems simulation framework for crop-soil coupling.

**Evidence limit:** A simulator is not an operational digital twin without observations and feedback.

### R11 AquaCrop-The FAO Crop Model to Simulate Yield Response to Water: I. Concepts and Underlying Principles

Steduto, Pasquale; Hsiao, Theodore C.; Raes, Dirk; Fereres, Elias (2009). *Agronomy Journal, 101(3), 426-437*.

[Primary record](https://doi.org/10.2134/agronj2008.0139s) | **Type:** published-paper

**Relevance:** Links crop production response to water availability through AquaCrop concepts.

**Evidence limit:** Crop parameters and management assumptions need independent validation.

### R23 AquaCrop-OS: An open source version of FAO's crop water productivity model

Foster, T.; Brozović, N.; Butler, A.P.; Neale, C.M.U.; Raes, D.; Steduto, P.; et al. (2017). *Agricultural Water Management, 181, 18-22*.

[Primary record](https://doi.org/10.1016/j.agwat.2016.11.015) | **Type:** published-paper

**Relevance:** Documents AquaCrop-OS as an open-source crop-water model relevant to irrigation baselines.

**Evidence limit:** This paper describes AquaCrop-OS, not the later Python implementation AquaCrop-OSPy.

## Calibration and Physics-Informed Learning

### R12 The Ensemble Kalman Filter: theoretical formulation and practical implementation

Evensen, Geir (2003). *Ocean Dynamics, 53(4), 343-367*.

[Primary record](https://doi.org/10.1007/s10236-003-0036-9) | **Type:** published-paper

**Relevance:** Provides the ensemble Kalman filter basis for sequential state estimation.

**Evidence limit:** Sampling, observation error, nonlinearity, and analysis water increments need attention.

### R13 Physics-informed neural networks: A deep learning framework for solving forward and inverse problems involving nonlinear partial differential equations

Raissi, M.; Perdikaris, P.; Karniadakis, G.E. (2019). *Journal of Computational Physics, 378, 686-707*.

[Primary record](https://doi.org/10.1016/j.jcp.2018.10.045) | **Type:** published-paper

**Relevance:** Introduces PINN formulations for forward and inverse differential-equation problems.

**Evidence limit:** Physics loss does not guarantee exact conservation or superiority over conventional solvers.

### R14 Physics-informed machine learning

Karniadakis, George Em; Kevrekidis, Ioannis G.; Lu, Lu; Perdikaris, Paris; Wang, Sifan; Yang, Liu (2021). *Nature Reviews Physics, 3(6), 422-440*.

[Primary record](https://doi.org/10.1038/s42254-021-00314-5) | **Type:** published-paper

**Relevance:** Places PINNs within the broader family of physics-informed machine learning.

**Evidence limit:** Methodological promise is distinct from agronomic field evidence.

### R15 Physics-Informed Neural Networks With Monotonicity Constraints for Richardson-Richards Equation: Estimation of Constitutive Relationships and Soil Water Flux Density From Volumetric Water Content Measurements

Bandai, Toshiyuki; Ghezzehei, Teamrat A. (2021). *Water Resources Research, 57(2), e2020WR027642*.

[Primary record](https://doi.org/10.1029/2020wr027642) | **Type:** published-paper

**Relevance:** Studies hydraulic constitutive inference and water flux from soil-moisture measurements.

**Evidence limit:** Inverse modelling evidence is not evidence of field-level irrigation savings.

### R16 Forward and inverse modeling of water flow in unsaturated soils with discontinuous hydraulic conductivities using physics-informed neural networks with domain decomposition

Bandai, Toshiyuki; Ghezzehei, Teamrat A. (2022). *Hydrology and Earth System Sciences, 26(16), 4469-4495*.

[Primary record](https://doi.org/10.5194/hess-26-4469-2022) | **Type:** published-paper

**Relevance:** Tests forward and inverse Richards PINNs and domain decomposition for layered soils.

**Evidence limit:** Numerical validation and training costs must not be recast as an operational field trial.

### R17 Characterizing possible failure modes in physics-informed neural networks

Krishnapriyan, Aditi; Gholami, Amir; Zhe, Shandian; Kirby, Robert; Mahoney, Michael W. (2021). *Advances in Neural Information Processing Systems, 34, 26548-26560*.

[Primary record](https://papers.neurips.cc/paper_files/paper/2021/hash/df438e5206f31600e6ae4af72f2725f1-Abstract.html) | **Type:** published-paper

**Relevance:** Demonstrates optimisation-related PINN failure modes that motivate strong baselines.

**Evidence limit:** Failures on selected PDE problems do not prove all PINNs fail on all soil-water tasks.

### R21 DeepXDE: A Deep Learning Library for Solving Differential Equations

Lu, Lu; Meng, Xuhui; Mao, Zhiping; Karniadakis, George Em (2021). *SIAM Review, 63(1), 208-228*.

[Primary record](https://doi.org/10.1137/19m1274067) | **Type:** published-paper

**Relevance:** Documents DeepXDE as a library for differential-equation-based machine learning.

**Evidence limit:** The software framework does not supply a validated agricultural model automatically.

## Smart-Farming Applications

### R19 Digital twin-enabled intelligent irrigation-drainage system for precision water-salt management in saline agroecosystems

Qin, Mengting; Zhang, Chuansong; Ma, Guorong; Ma, Yongcheng; Feng, Xiong; Li, Peijie; et al. (2025). *Agricultural Water Management, 322, 109957*.

[Primary record](https://doi.org/10.1016/j.agwat.2025.109957) | **Type:** published-paper

**Relevance:** Reports a twin-enabled irrigation-drainage system addressing water-salt management.

**Evidence limit:** A site-specific multi-component platform does not isolate the causal benefit of AI alone.

### R20 Advancing sustainable solar greenhouse management through digital twin enabled by functional-structural plant modeling: case study in Beijing, China

Xu, Demin; Zhu, Jinyu; Ma, Yuntao (2025). *Energy Conversion and Management, 346, 120505*.

[Primary record](https://doi.org/10.1016/j.enconman.2025.120505) | **Type:** published-paper

**Relevance:** Connects functional-structural plant modelling to greenhouse twin management.

**Evidence limit:** A greenhouse case study does not establish transfer to open-field agriculture.

## Data and Evaluation Foundations

### R22 The International Soil Moisture Network: serving Earth system science for over a decade

Dorigo, Wouter; Himmelbauer, Irene; Aberer, Daniel; Schremmer, Lukas; Petrakovic, Ivana; Zappa, Luca; et al. (2021). *Hydrology and Earth System Sciences, 25(11), 5749-5804*.

[Primary record](https://doi.org/10.5194/hess-25-5749-2021) | **Type:** published-paper

**Relevance:** Describes harmonised in-situ moisture observations useful for independent validation.

**Evidence limit:** Station coverage, depth, quality, and land management must be checked for the chosen subset.

### R24 ERA5-Land: a state-of-the-art global reanalysis dataset for land applications

Muñoz-Sabater, Joaquín; Dutra, Emanuel; Agustí-Panareda, Anna; Albergel, Clément; Arduini, Gabriele; Balsamo, Gianpaolo; et al. (2021). *Earth System Science Data, 13(9), 4349-4383*.

[Primary record](https://doi.org/10.5194/essd-13-4349-2021) | **Type:** published-paper

**Relevance:** Describes ERA5-Land as a land reanalysis resource for forcing and regional context.

**Evidence limit:** Modelled reanalysis should not be presented as independent field moisture truth.

### R25 SoilGrids 2.0: producing soil information for the globe with quantified spatial uncertainty

Poggio, Laura; de Sousa, Luis M.; Batjes, Niels H.; Heuvelink, Gerard B. M.; Kempen, Bas; Ribeiro, Eloi; et al. (2021). *SOIL, 7(1), 217-240*.

[Primary record](https://doi.org/10.5194/soil-7-217-2021) | **Type:** published-paper

**Relevance:** Describes global soil-property mapping with spatial uncertainty.

**Evidence limit:** Predicted gridded properties are priors, not local hydraulic measurements.

## Technical Guide and Preprint

### R06 Crop evapotranspiration: Guidelines for computing crop water requirements

Allen, Richard G.; Pereira, Luis S.; Raes, Dirk; Smith, Martin (1998). *FAO Irrigation and Drainage Paper 56. Food and Agriculture Organization, Rome*.

[Primary record](https://www.fao.org/4/x0490e/x0490e00.htm) | **Type:** technical-guide

**Relevance:** Provides evapotranspiration and root-zone depletion concepts for irrigation accounting.

**Evidence limit:** A technical guide, not a journal paper; crop and site assumptions require local adaptation.

### R18 Model predictive control of agro-hydrological systems based on a two-layer neural network modeling framework

Huang, Zhiyinan; Liu, Jinfeng; Huang, Biao (2022). *arXiv preprint arXiv:2204.12694*.

[Primary record](https://doi.org/10.48550/arXiv.2204.12694) | **Type:** preprint

**Relevance:** Studies neural-network approximation within zone model predictive irrigation control.

**Evidence limit:** Cited as an arXiv preprint and numerical control study, not peer-reviewed field evidence.
