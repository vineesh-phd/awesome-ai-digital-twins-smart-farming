# Datasets for Smart-Farming Digital Twins

[Back to collection](../README.md) | Checked: 25 September 2026

These five resources provide different kinds of evidence. None, by itself, supplies a complete experiment with irrigation actions, metered withdrawals, root-zone moisture, and crop yield. Access and product versions must be checked again when downloading.

## D01 International Soil Moisture Network

**Provider:** ISMN, hosted by ICWRGC and BfG. [Data access](https://ismn.earth/data/data-download/) | [Availability](https://ismn.earth/data/data-availability/)

**Contents:** Harmonised in-situ soil-moisture time series, depth and station metadata, quality flags, and additional variables where supplied. **Use:** select agricultural stations and depth-matched holdouts for calibration or independent moisture validation. **Access:** free registration is required for downloads; acknowledge both ISMN and the contributing networks under their terms. **Limits:** sampling, depths, and ancillary observations vary. Check land cover and irrigation metadata; do not assume every station is an irrigated field. Reference: R22 in the [bibliography](../references/references.md).

## D02 SMAP Enhanced L3 Radiometer Soil Moisture

**Provider:** NASA NSIDC DAAC. **Product:** SPL3SMP_E, version 6. [Product page](https://nsidc.org/data/spl3smp_e/versions/6) | [Dataset DOI](https://doi.org/10.5067/M20OXIZHY3RJ)

**Contents:** Daily surface-moisture estimates posted on a 9 km EASE grid. **Use:** regional moisture context and carefully collocated satellite/ground comparisons. **Access:** Earthdata Login; cite the version and subset. **Limits:** grid spacing is not an independent 9 km footprint and is not field-scale root-zone truth. Apply retrieval-quality flags. On the check date, NSIDC reported a geolocation problem affecting 14 May-28 July 2026 and reprocessing of standard products. Consult the current advisory and processing version before using that interval.

## D03 ERA5-Land

**Provider:** Copernicus Climate Change Service / ECMWF. [Dataset and access conditions](https://cds.climate.copernicus.eu/datasets/reanalysis-era5-land)

**Contents:** Hourly land-surface reanalysis, including soil-water and meteorological variables. **Use:** historical forcing, regional context, and stress-testing model inputs. **Access:** follow the Climate Data Store's account, API, and license requirements. **Limits:** modelled soil moisture is not an independent validation target for an observational claim. Harmonise layer definitions and units; avoid assimilating and validating against the same derived product. Reference: R24.

## D04 SoilGrids

**Provider:** ISRIC - World Soil Information. [Documentation and access](https://docs.isric.org/globaldata/soilgrids/SoilGrids_faqs.html)

**Contents:** Predicted soil properties at 250 m grid spacing across six standard depth intervals, with uncertainty information. **Use:** initial soil-property priors, site stratification, and guidance for field sampling. **Access:** consult ISRIC's current distribution and attribution terms; record product/version and conversion factors. **Limits:** a mapped texture value is not a measured hydraulic parameter. Pedotransfer-derived parameters require uncertainty analysis and local calibration. Reference: R25.

## D05 NASA POWER

**Provider:** NASA Langley Research Center. [Project](https://power.larc.nasa.gov/) | [API tutorial](https://power.larc.nasa.gov/docs/tutorials/service-data-request/api/)

**Contents:** Gridded meteorological and solar data with selectable time aggregation. **Use:** exploratory crop-water simulations where local weather observations are unavailable. **Access:** public services; preserve parameter names, units, location, dates, and required acknowledgement. **Limits:** do not treat historical data as a forecast available at the original decision time. Check rainfall and radiation against local measurements when possible.

## Minimum Local Trial Data

To evaluate irrigation decisions, collect timestamps, measurement depths, calibrated moisture, rainfall, weather-forecast issue times, commands, measured delivered volume, field area, crop stage, and yield or quality. Store sensor uncertainty and maintenance events. Split validation by event, season, or field; do not randomly mix adjacent timestamps. No dataset download or field-data collection is claimed by this repository.
