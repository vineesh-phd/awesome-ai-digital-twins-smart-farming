# GitHub Implementations

[Back to collection](../README.md) | Inspection date: 25 September 2026

Selection considers scientific fit, visible source, documentation, examples, license, and activity. GitHub's reported push timestamps are maintenance signals, **not** evidence that a release or example has been tested. All five repositories were non-archived at inspection. Metadata are preserved in [repository-inspections.json](repository-inspections.json). No external code was installed or executed for this assessment.

## I01 DeepXDE

**Repository:** [lululxvi/deepxde](https://github.com/lululxvi/deepxde)

**Fit:** forward/inverse PINN experiments and parameter inference; see R21.

**Inspection:** README, source and example directories, installation instructions, and inverse-problem demos are available.

**License:** LGPL-2.1 as identified by the project. **Last reported push:** 18 August 2026.

**Reproducibility step:** pin a commit and backend, then reproduce a documented inverse problem before adding soil hydraulics. The repository is a general library, not a ready-made irrigation twin.

## I02 AquaCrop-OSPy

**Repository:** [aquacropos/aquacrop](https://github.com/aquacropos/aquacrop)

**Fit:** crop-water response and irrigation-strategy baselines; related foundation R23 describes AquaCrop-OS, not this Python implementation itself.

**Inspection:** readable Python source, a runnable README example, and linked irrigation notebooks.

**License:** Apache-2.0. **Last reported push:** 23 September 2026.

**Reproducibility step:** fix weather, soil, crop, and management inputs and reproduce a tutorial. Do not call this the official FAO implementation or assume every FAO model process is supported.

## I03 APSIM Next Generation

**Repository:** [APSIMInitiative/ApsimX](https://github.com/APSIMInitiative/ApsimX)

**Fit:** mechanistic agricultural systems modelling; R10 provides the framework background.

**Inspection:** model source, examples, tests, and project documentation are visible.

**License:** custom APSIM General Use Licence Agreement; GitHub reports NOASSERTION, not a standard permissive license. [License text](https://github.com/APSIMInitiative/ApsimX/blob/master/LICENSE.md). **Last reported push:** 25 September 2026.

**Reproducibility step:** review terms and system requirements, fix the build and simulation inputs, and validate a documented example. Availability of source is not permission for every use.

## I04 Python Crop Simulation Environment

**Repository:** [ajwdewit/pcse](https://github.com/ajwdewit/pcse)

**Fit:** crop simulation and a second physical modelling baseline.

**Inspection:** README, source, examples, and linked model documentation are available.

**License:** the project license notice specifies EUPL 1.1 or subsequent approved versions; GitHub's automatic classification is NOASSERTION. **Last reported push:** 1 September 2026.

**Reproducibility step:** fix the model class, weather provider, soil/crop parameters, and management configuration before comparing outputs. Different crop-model choices are not interchangeable.

## I05 do-mpc

**Repository:** [do-mpc/do-mpc](https://github.com/do-mpc/do-mpc)

**Fit:** constrained receding-horizon control and state-estimation experiments.

**Inspection:** source, documentation, and examples provide a starting point for controller construction.

**License:** LGPL-3.0 as identified by the project. **Last reported push:** 22 September 2026.

**Reproducibility step:** test a documented example, then supply a validated agro-hydrological model with irrigation and stress constraints. An optimisation solver does not establish field safety or water savings.

## Before Using Any Implementation

Record the exact commit or release, dependency environment, seed, input provenance, baseline, and expected outputs. Review the license at that pinned version. Preserve failures and numerical tolerances. An operational deployment additionally needs sensor validation, actuation confirmation, uncertainty handling, and a locally approved fallback.
