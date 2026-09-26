# Tools and Libraries

[Back to collection](../README.md) | Checked: 25 September 2026

These are candidate research components, not a tested end-to-end farming platform. See the [implementation assessment](../implementations/github-repositories.md) for licensing and activity checks.

## T01 DeepXDE

[Project documentation](https://deepxde.readthedocs.io/en/latest/) - scientific machine learning for forward and inverse differential-equation problems. Use it to prototype a Richards-equation PINN with explicit data, boundary, and residual losses. Compare against a conventional solver; small training loss alone is insufficient.

## T02 AquaCrop-OSPy

[Documentation](https://aquacropos.github.io/aquacrop/) - Python crop-water simulation suited to exploratory irrigation strategies. It is a community implementation built from AquaCrop-OS, **not an official FAO AquaCrop release**. Check supported processes before studying salinity or other stresses.

## T03 APSIM Next Generation

[Source and project documentation](https://github.com/APSIMInitiative/ApsimX) - modular agricultural systems simulation for soil, crops, and management. A candidate physical baseline for crop-water coupling, not a digital twin unless observations and decisions are integrated. Read the custom APSIM agreement before use.

## T04 PCSE

[Documentation](https://pcse.readthedocs.io/en/stable/) - Python Crop Simulation Environment, including WOFOST-related crop modelling workflows. Useful for comparing crop response and management assumptions. Record model configuration and parameter sources, not just the package name.

## T05 do-mpc

[Documentation](https://www.do-mpc.com/en/latest/) - model predictive control, simulation, and estimation infrastructure. Useful for expressing irrigation bounds and scenario-based control experiments; an agricultural model and safe operating constraints still have to be supplied.

## T06 Xarray

[Documentation](https://docs.xarray.dev/en/stable/) - labelled multi-dimensional arrays for environmental time, depth, and spatial data. Useful for keeping dimensions explicit while preparing gridded forcing and validation subsets. Unit correctness and observation independence remain the researcher's responsibility.

## T07 Crossref REST API

[Official documentation](https://www.crossref.org/documentation/retrieve-metadata/rest-api/) - DOI metadata lookup for bibliographic identity checks. Used to cross-check this collection. Metadata existence is not a claim-entailment test; inspect the actual paper for scientific support.
