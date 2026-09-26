# From Governing Equations to Irrigation Outcomes

[Back to collection](../README.md) | [Review paper](../paper/AI_Assisted_Research_Paper.pdf)

This is a proposed research workflow, not an implemented controller. The original paper remains the authority for its equation numbering, definitions, and assumptions.

## Physical Accounting

Equation (1) balances root-zone storage against rainfall, the modelled fraction of gross irrigation, capillary rise, evapotranspiration, runoff, and drainage. All interval fluxes use millimetres. Define the measurement boundary before choosing an efficiency factor; do not count the same loss twice.

Equations (2)-(3) connect mean volumetric moisture and rooting depth to available water and depletion. Equation (4) uses an upward-positive vertical coordinate in the Richards formulation. Equations (5)-(6) close the model using retention and conductivity relationships. Boundary assumptions and soil layering must match the case being studied.

## Calibration and Updating

Calibrate sensors separately from model parameters. Equation (7) distinguishes observation error, parameter bounds, and regularisation. Start with sensitivity and identifiability checks. Hold out entire events, seasons, or fields rather than randomly mixing neighbouring timestamps.

Equation (8) illustrates sequential state updating. Log analysis increments separately from physical water fluxes, since a state correction can change model storage without measured inflow. Check the observation operator's depth or spatial footprint.

## Physics-Informed Learning

Equations (9)-(10) combine the Richards residual with observation, initial-condition, boundary-condition, and parameter terms. Scale the terms consistently. Compare against a numerical solver and a simpler water-balance baseline. Track conservation, extrapolation, initialisation sensitivity, and training cost in addition to fit.

## Decision and Execution

Equation (11) illustrates a normalised control objective, not a universal irrigation policy. Define pump limits, water availability, application windows, stress tolerance, and any required leaching. Execute only an approved action and compare commands with metered delivery. A data or communications failure requires a locally approved fallback, not blind continuation.

## Measurable Outcomes

| Question | Evidence needed | Invalid shortcut |
| --- | --- | --- |
| Does moisture prediction improve? | Independent observations by depth and forecast horizon | Random timestamp splits |
| Is the water account plausible? | Storage and measured fluxes, plus assimilation increments | Small neural-network loss |
| Is less irrigation applied? | Comparable metered seasonal volumes | Counting valve commands |
| Is consumptive use reduced? | Actual ET and a defined accounting boundary | Equating pumping with consumption |
| Is agronomic value retained? | Replicated crop yield or quality and stress measures | Moisture accuracy alone |
| Is operation practical? | Failures, maintenance, cost, and operator effort | A successful notebook run |

## Reproducibility Record

Retain data provenance and access date, site and depth definitions, train/test split, model and solver version, parameter distributions, weather-forecast issue times, software environment, seeds, action logs, and evaluation scripts. Field protocols need agronomic review and appropriate replication. No experimental results are supplied in this repository.

## Illustrative Calculation Check

For the paper's assumed 0.40 m root depth, field capacity 0.30, wilting point 0.15, and depletion fraction 0.50: total available water is 60 mm and readily available water is 30 mm. Moisture 0.24 implies 24 mm depletion. After an assumed 6 mm ET loss, reducing depletion from 30 to 12 mm requires 18 mm net water. At a 0.90 delivery fraction, that is 20 mm gross, or 200 m3 over 10,000 m2. A moisture uncertainty of 0.02 corresponds to 8 mm of storage. These are assumed inputs and arithmetic, not a recommended field treatment.
