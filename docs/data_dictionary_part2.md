# Data Dictionary - GB_GBN Dataset

**Project:** Renewable Energy and Smart Grid Demand (Project 07)
**File:** `GB_GBN SPECIFIC DATASET.xlsx` (sheet: `Sheet1`)
**Original source:** Open Power System Data (OPSD), *Time series* data package, file `time_series_60min_singleindex` (hourly; primary data from ENTSO-E Transparency Platform). https://doi.org/10.25832/time_series/2020-10-06.
**Shape (checked with Python):** 50,401 rows x 16 columns (1 timestamp + 15 numeric)
**Time coverage:** 2014-12-31 23:00 to 2020-09-30 23:00 UTC, exactly one row per hour (no gaps, no duplicate timestamps).
**Duplicate rows:** 0
**Zone:** `GBN` = Great Britain (England, Scotland, Wales). Northern Ireland and UK-total columns were removed.

> **Notes**
> 1. UTC was chosen as the timestamp because Great Britain is not on Central European Time and UTC has no daylight-saving shifts.
> 2. All 15 numeric columns are `float64`. Whole-number-looking values (MW) are floats because the columns contain missing values (NaN).
> 3. `profile` columns are calculated (generation divided by capacity), not measured.
> 4. Total wind generation is approximately onshore + offshore (small rounding differences).

## Columns

| # | Column name | Data type | Meaning | Unit | Missing values | Relevance to renewable-energy analysis |
|---|---|---|---|---|---|---|
| 1 | `utc_timestamp` | string (text) in the file; convert to `datetime64[us, UTC]` | The hour each row was recorded, in Coordinated Universal Time(utc). | UTC, hourly | 0 (0.0%) | High (time axis) |
| 2 | `GB_GBN_load_actual_entsoe_transparency` | float64 | Actual electricity demand (load) in Great Britain. | MW | 7 (0.0%) | High (demand) |
| 3 | `GB_GBN_load_forecast_entsoe_transparency` | float64 | Day-ahead forecast of electricity demand in Great Britain. | MW | 121 (0.2%) | Medium |
| 4 | `GB_GBN_price_day_ahead` | float64 | Day-ahead wholesale electricity price in Great Britain. | currency per MWh (confirm in OPSD README) | 111 (0.2%) | Medium |
| 5 | `GB_GBN_solar_capacity` | float64 | Installed solar capacity in Great Britain (the most it could produce). | MW | 6,600 (13.1%) | High |
| 6 | `GB_GBN_solar_generation_actual` | float64 | Actual solar electricity generated in Great Britain. | MW | 55 (0.1%) | High |
| 7 | `GB_GBN_solar_profile` | float64 | Solar capacity factor: generation divided by capacity (0 = none, 1 = full power). Calculated, not measured. | ratio (0-1) | 6,649 (13.2%) | High |
| 8 | `GB_GBN_wind_capacity` | float64 | Installed all wind (onshore + offshore) capacity in Great Britain (the most it could produce). | MW | 6,600 (13.1%) | High |
| 9 | `GB_GBN_wind_generation_actual` | float64 | Actual all wind (onshore + offshore) electricity generated in Great Britain. | MW | 41 (0.1%) | High |
| 10 | `GB_GBN_wind_profile` | float64 | All wind (onshore + offshore) capacity factor: generation divided by capacity (0 = none, 1 = full power). Calculated, not measured. | ratio (0-1) | 6,641 (13.2%) | High |
| 11 | `GB_GBN_wind_offshore_capacity` | float64 | Installed offshore wind capacity in Great Britain (the most it could produce). | MW | 6,600 (13.1%) | High |
| 12 | `GB_GBN_wind_offshore_generation_actual` | float64 | Actual offshore wind electricity generated in Great Britain. | MW | 41 (0.1%) | High |
| 13 | `GB_GBN_wind_offshore_profile` | float64 | Offshore wind capacity factor: generation divided by capacity (0 = none, 1 = full power). Calculated, not measured. | ratio (0-1) | 6,641 (13.2%) | High |
| 14 | `GB_GBN_wind_onshore_capacity` | float64 | Installed onshore wind capacity in Great Britain (the most it could produce). | MW | 6,600 (13.1%) | High |
| 15 | `GB_GBN_wind_onshore_generation_actual` | float64 | Actual onshore wind electricity generated in Great Britain. | MW | 41 (0.1%) | High |
| 16 | `GB_GBN_wind_onshore_profile` | float64 | Onshore wind capacity factor: generation divided by capacity (0 = none, 1 = full power). Calculated, not measured. | ratio (0-1) | 6,641 (13.2%) | High |

## Columns relevant to renewable energy analysis

- **Core (High):** `utc_timestamp`; all solar and wind generation, capacity and profile columns; and `GB_GBN_load_actual_entsoe_transparency` (demand), so renewable output can be compared with demand.
- **Medium:** `GB_GBN_load_forecast_entsoe_transparency` (forecast accuracy) and `GB_GBN_price_day_ahead` (price vs. renewable output).
- All 16 columns are usable.

## Data-quality flags to investigate (Week 2)

- **Capacity and profile columns** are missing about 13% of rows (6,600+). They stop at 2019-12-30T23:00:00Z, so they cover 2015-2019 only.
- `GB_GBN_solar_profile` exceeds 1 in 233 rows (maximum 1.367). A capacity factor should not normally exceed 1; flag as outliers, do not delete.
- `GB_GBN_price_day_ahead` ranges from -38.8 to 999.0. Negative prices can be genuine, but 10 values are 500 or higher (top values: 999, 960, 799); verify.
- `GB_GBN_load_actual_entsoe_transparency` has very low readings (minimum 511 MW against a mean of 34921 MW), clustered around 2019-05-20 to 2019-05-21; likely a data fault.
- The first row (2014-12-31 23:00) has no load, price or generation values.
- Solar plus wind average only about 17% of demand, so "demand exceeds generation" is almost always true; analyse the *share* of demand covered instead.
