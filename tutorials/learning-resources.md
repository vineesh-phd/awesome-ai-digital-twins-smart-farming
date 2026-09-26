# Learning Pathway

[Back to collection](../README.md) | Checked: 25 September 2026

These seven resources are provider or project documentation, not third-party promotional lists. The sequence moves from physical meaning to data preparation and control. Exercises are proposed, not completed experiments.

## L01 FAO Irrigation and Drainage Paper 56

[FAO-56](https://www.fao.org/4/x0490e/x0490e00.htm) - understand reference and crop evapotranspiration, root-zone depletion, and irrigation accounting. Start by reproducing the manuscript's storage calculation and documenting the assumed crop stage and rooting depth. This guide is R06, not one of the 23 published papers.

## L02 AquaCrop-OSPy Notebooks

[Official project documentation](https://aquacropos.github.io/aquacrop/) - follow the getting-started, irrigation-demand, and irrigation-optimisation notebooks. Record weather, crop, soil, management inputs, and software version. A tutorial run is a simulation, not field validation.

## L03 DeepXDE Inverse Problems

[Inverse-problem demos](https://deepxde.readthedocs.io/en/latest/demos/pinn_inverse.html) - learn how observations and equation constraints enter parameter inference. Reproduce a small documented problem before formulating soil-water physics. Record loss scaling and held-out errors.

## L04 do-mpc Documentation

[Project documentation](https://www.do-mpc.com/en/latest/) - study modelling, constraints, simulation, estimation, and control examples. The learning goal is to separate an estimated state from the controller's objectives and admissible actions.

## L05 Reading ISMN Data

[ISMN reader example](https://ismn.readthedocs.io/en/latest/examples/interface.html) - work with station metadata and sensor-specific observations. Preserve depth, quality flags, and measurement units; do not treat all sensors as root-zone averages.

## L06 NASA POWER API Tutorial

[Provider tutorial](https://power.larc.nasa.gov/docs/tutorials/service-data-request/api/) - construct an auditable request for location, parameters, time range, and aggregation. Save the request and provenance; check whether the returned units match the crop model's inputs.

## L07 Xarray Tutorial

[Project tutorial](https://tutorial.xarray.dev/) - learn labelled dimensions, selection, grouping, and environmental-data operations. Build a time/depth/site representation without silently mixing spatial footprints or observation types.
