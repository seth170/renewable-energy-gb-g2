# Data Dictionary: GB_GBN Time Series Dataset

## Overview
This document provides a complete data dictionary for the 16 variables included in the **GB_GBN** (Great Britain — National Grid control area) power system dataset. The definitions, data types, and units of measurement are aligned with the official **Open Power System Data (OPSD)** Time Series documentation (ENTSO-E Transparency Platform and national TSO sources).

> **Note on Data Types & Missing Values:** 
> - **Data Types** reflect standard pandas/SQL schema interpretations of the dataset (to be cross-verified against Member 1's `df.dtypes` / `df.info()` output).
> - **Expected Missing Values** reflect both known structural gaps in the OPSD GB_GBN time series (e.g., boundary timestamps, unreporting periods, or capacity reporting lags) and placeholders to be populated/confirmed with Member 3's exact `isnull().sum()` quality audit counts.

---

## Summary Table

| # | Variable Name | Data Type | Unit of Measurement | Expected Missing Values |
| :--- | :--- | :--- | :--- | :--- |
| 1 | `utc_timestamp` | `datetime64[ns, UTC]` (ISO 8601 String in raw CSV/Excel) | UTC Timestamp (`YYYY-MM-DDTHH:MM:SSZ`) | None (0%) — Primary index key |
| 2 | `GB_GBN_load_actual_entsoe_transparency` | `float64` | Megawatts ($\text{MW}$) | Low — Occasional single-hour gaps and boundary intervals |
| 3 | `GB_GBN_load_forecast_entsoe_transparency` | `float64` | Megawatts ($\text{MW}$) | Low — Occasional day-ahead submission gaps |
| 4 | `GB_GBN_price_day_ahead` | `float64` | Currency per Megawatt-hour ($\text{EUR/MWh}$ or $\text{GBP/MWh}$ per OPSD source) | Moderate to High — Often sparse or missing in OPSD GB series |
| 5 | `GB_GBN_solar_capacity` | `float64` | Megawatts ($\text{MW}$) | Low to Moderate — Missing at series boundaries or before reporting start |
| 6 | `GB_GBN_solar_generation_actual` | `float64` | Megawatts ($\text{MW}$) | Low — Minor reporting dropouts; nighttime values are `0` |
| 7 | `GB_GBN_solar_profile` | `float64` | Dimensionless ratio ($0 \text{ to } 1$) | Low to Moderate — Missing wherever capacity or actual generation is missing |
| 8 | `GB_GBN_wind_capacity` | `float64` | Megawatts ($\text{MW}$) | Low to Moderate — Missing at series boundaries or unreporting periods |
| 9 | `GB_GBN_wind_generation_actual` | `float64` | Megawatts ($\text{MW}$) | Low — Occasional TSO telemetry dropouts |
| 10 | `GB_GBN_wind_profile` | `float64` | Dimensionless ratio ($0 \text{ to } 1$) | Low to Moderate — Missing wherever capacity or actual generation is missing |
| 11 | `GB_GBN_wind_offshore_capacity` | `float64` | Megawatts ($\text{MW}$) | Low to Moderate — Missing prior to disaggregated reporting periods |
| 12 | `GB_GBN_wind_offshore_generation_actual` | `float64` | Megawatts ($\text{MW}$) | Low — Occasional reporting dropouts |
| 13 | `GB_GBN_wind_offshore_profile` | `float64` | Dimensionless ratio ($0 \text{ to } 1$) | Low to Moderate — Missing wherever capacity or actual generation is missing |
| 14 | `GB_GBN_wind_onshore_capacity` | `float64` | Megawatts ($\text{MW}$) | Low to Moderate — Missing prior to disaggregated reporting periods |
| 15 | `GB_GBN_wind_onshore_generation_actual` | `float64` | Megawatts ($\text{MW}$) | Low — Occasional reporting dropouts |
| 16 | `GB_GBN_wind_onshore_profile` | `float64` | Dimensionless ratio ($0 \text{ to } 1$) | Low to Moderate — Missing wherever capacity or actual generation is missing |

---

## Detailed Variable Specifications

### 1. `utc_timestamp`
- **Data Type:** `datetime64[ns, UTC]` *(stored as ISO 8601 text string `object` in raw Excel/CSV before parsing)*
- **Description / Meaning:** Start of the time interval in Coordinated Universal Time (UTC). Serves as the primary chronological index for all hourly/sub-hourly observations in the Great Britain (`GB_GBN`) bidding zone / control area.
- **Unit of Measurement:** Timestamp (`YYYY-MM-DDTHH:MM:SSZ`, UTC)
- **Expected Missing Values:** **None (`0` missing values)**. Every row requires a valid, unique timestamp. *(Verify against Member 3 audit for any duplicate or skipped intervals).*

### 2. `GB_GBN_load_actual_entsoe_transparency`
- **Data Type:** `float64`
- **Description / Meaning:** Total actual electrical load (power demand) in the Great Britain National Grid control area (`GB_GBN`), as reported via the ENTSO-E Transparency Platform. Represents the average power consumption during the respective time interval.
- **Unit of Measurement:** Megawatts ($\text{MW}$)
- **Expected Missing Values:** **Yes (Low)**. Typically exhibits minor missing values at the very beginning/end of the multi-year OPSD time series and isolated single-hour telemetry gaps. *(Cross-check exact count with Member 3 audit).*

### 3. `GB_GBN_load_forecast_entsoe_transparency`
- **Data Type:** `float64`
- **Description / Meaning:** Day-ahead forecasted total electrical load in the `GB_GBN` control area, published by the Transmission System Operator (TSO) on the ENTSO-E Transparency Platform prior to the delivery day.
- **Unit of Measurement:** Megawatts ($\text{MW}$)
- **Expected Missing Values:** **Yes (Low)**. Occasional gaps occur when day-ahead forecast submissions were delayed or omitted on ENTSO-E. *(Cross-check exact count with Member 3 audit).*

### 4. `GB_GBN_price_day_ahead`
- **Data Type:** `float64`
- **Description / Meaning:** Day-ahead wholesale electricity market clearing price for the Great Britain (`GB_GBN`) bidding zone.
- **Unit of Measurement:** Currency per Megawatt-hour ($\text{EUR/MWh}$ in harmonized OPSD tables, or $\text{GBP/MWh}$ depending on raw national feed)
- **Expected Missing Values:** **Yes (Moderate to High)**. In OPSD time series releases for `GB_GBN`, day-ahead price coverage is frequently partial or missing across extended historical windows due to market data licensing restrictions. *(Verify exact missing percentage with Member 3 audit).*

### 5. `GB_GBN_solar_capacity`
- **Data Type:** `float64`
- **Description / Meaning:** Cumulative installed electrical generation capacity of photovoltaic (PV) solar power plants in `GB_GBN` at the given timestamp. Derived by OPSD from national renewable energy registries and ENTSO-E installed capacity reports.
- **Unit of Measurement:** Megawatts ($\text{MW}$)
- **Expected Missing Values:** **Yes (Low to Moderate)**. Missing values typically appear at the start of the dataset before solar capacity tracking began or after the final capacity update cutoff date. *(Cross-check exact count with Member 3 audit).*

### 6. `GB_GBN_solar_generation_actual`
- **Data Type:** `float64`
- **Description / Meaning:** Actual aggregated electrical power output generated by solar PV installations in `GB_GBN` during the time interval. Nighttime intervals legitimately record `0.0` rather than `NaN`.
- **Unit of Measurement:** Megawatts ($\text{MW}$)
- **Expected Missing Values:** **Yes (Low)**. Minor gaps occur during TSO reporting outages or at series boundaries. *(Cross-check exact count with Member 3 audit).*

### 7. `GB_GBN_solar_profile`
- **Data Type:** `float64`
- **Description / Meaning:** Normalized solar generation profile (capacity factor), calculated in the OPSD pipeline as the ratio of actual solar generation to installed solar capacity:
  $$\text{Profile}_{\text{solar}} = \frac{\text{GB\_GBN\_solar\_generation\_actual}}{\text{GB\_GBN\_solar\_capacity}}$$
- **Unit of Measurement:** Dimensionless ratio ($0 \text{ to } 1$, i.e., $\text{MW}/\text{MW}$)
- **Expected Missing Values:** **Yes (Low to Moderate)**. Directly inherits missing values from both `GB_GBN_solar_generation_actual` and `GB_GBN_solar_capacity` (any timestamp where either input is `NaN` results in `NaN`). *(Cross-check exact count with Member 3 audit).*

### 8. `GB_GBN_wind_capacity`
- **Data Type:** `float64`
- **Description / Meaning:** Total cumulative installed electrical generation capacity of all wind power plants (combined onshore and offshore) in `GB_GBN`.
- **Unit of Measurement:** Megawatts ($\text{MW}$)
- **Expected Missing Values:** **Yes (Low to Moderate)**. Missing values occur outside the active capacity registry window or at series boundaries. *(Cross-check exact count with Member 3 audit).*

### 9. `GB_GBN_wind_generation_actual`
- **Data Type:** `float64`
- **Description / Meaning:** Total actual aggregated electrical power generated by all wind turbines (onshore and offshore combined) in `GB_GBN` during the time interval.
- **Unit of Measurement:** Megawatts ($\text{MW}$)
- **Expected Missing Values:** **Yes (Low)**. Occasional short gaps due to ENTSO-E / National Grid reporting interruptions. *(Cross-check exact count with Member 3 audit).*

### 10. `GB_GBN_wind_profile`
- **Data Type:** `float64`
- **Description / Meaning:** Normalized total wind generation profile (capacity factor), calculated as the ratio of total actual wind generation to total installed wind capacity:
  $$\text{Profile}_{\text{wind}} = \frac{\text{GB\_GBN\_wind\_generation\_actual}}{\text{GB\_GBN\_wind\_capacity}}$$
- **Unit of Measurement:** Dimensionless ratio ($0 \text{ to } 1$, i.e., $\text{MW}/\text{MW}$)
- **Expected Missing Values:** **Yes (Low to Moderate)**. Missing whenever either `GB_GBN_wind_generation_actual` or `GB_GBN_wind_capacity` is missing. *(Cross-check exact count with Member 3 audit).*

### 11. `GB_GBN_wind_offshore_capacity`
- **Data Type:** `float64`
- **Description / Meaning:** Cumulative installed electrical generation capacity of offshore wind farms located in `GB_GBN` waters.
- **Unit of Measurement:** Megawatts ($\text{MW}$)
- **Expected Missing Values:** **Yes (Low to Moderate)**. Missing at series boundaries or during early periods prior to separate offshore/onshore reporting. *(Cross-check exact count with Member 3 audit).*

### 12. `GB_GBN_wind_offshore_generation_actual`
- **Data Type:** `float64`
- **Description / Meaning:** Actual aggregated electrical power output generated specifically by offshore wind farms in `GB_GBN` during the time interval.
- **Unit of Measurement:** Megawatts ($\text{MW}$)
- **Expected Missing Values:** **Yes (Low)**. Occasional single-hour or multi-hour TSO telemetry dropouts. *(Cross-check exact count with Member 3 audit).*

### 13. `GB_GBN_wind_offshore_profile`
- **Data Type:** `float64`
- **Description / Meaning:** Normalized offshore wind generation profile (capacity factor), calculated as:
  $$\text{Profile}_{\text{wind, offshore}} = \frac{\text{GB\_GBN\_wind\_offshore\_generation\_actual}}{\text{GB\_GBN\_wind\_offshore\_capacity}}$$
- **Unit of Measurement:** Dimensionless ratio ($0 \text{ to } 1$, i.e., $\text{MW}/\text{MW}$)
- **Expected Missing Values:** **Yes (Low to Moderate)**. Missing whenever either `GB_GBN_wind_offshore_generation_actual` or `GB_GBN_wind_offshore_capacity` is missing. *(Cross-check exact count with Member 3 audit).*

### 14. `GB_GBN_wind_onshore_capacity`
- **Data Type:** `float64`
- **Description / Meaning:** Cumulative installed electrical generation capacity of onshore (land-based) wind farms in `GB_GBN`.
- **Unit of Measurement:** Megawatts ($\text{MW}$)
- **Expected Missing Values:** **Yes (Low to Moderate)**. Missing at series boundaries or prior to disaggregated onshore capacity tracking. *(Cross-check exact count with Member 3 audit).*

### 15. `GB_GBN_wind_onshore_generation_actual`
- **Data Type:** `float64`
- **Description / Meaning:** Actual aggregated electrical power output generated specifically by onshore wind farms in `GB_GBN` during the time interval.
- **Unit of Measurement:** Megawatts ($\text{MW}$)
- **Expected Missing Values:** **Yes (Low)**. Occasional reporting gaps from ENTSO-E / National Grid. *(Cross-check exact count with Member 3 audit).*

### 16. `GB_GBN_wind_onshore_profile`
- **Data Type:** `float64`
- **Description / Meaning:** Normalized onshore wind generation profile (capacity factor), calculated as:
  $$\text{Profile}_{\text{wind, onshore}} = \frac{\text{GB\_GBN\_wind\_onshore\_generation\_actual}}{\text{GB\_GBN\_wind\_onshore\_capacity}}$$
- **Unit of Measurement:** Dimensionless ratio ($0 \text{ to } 1$, i.e., $\text{MW}/\text{MW}$)
- **Expected Missing Values:** **Yes (Low to Moderate)**. Missing whenever either `GB_GBN_wind_onshore_generation_actual` or `GB_GBN_wind_onshore_capacity` is missing. *(Cross-check exact count with Member 3 audit).*

---

## Team Reconciliation Checklist
- [ ] **Member 1 Sync:** Confirm whether `utc_timestamp` is parsed as `datetime64[ns, UTC]` or left as `object` in the final cleaned schema, and verify all numeric columns are `float64`.
- [ ] **Member 3 Sync:** Replace qualitative missing-value expectations (`Low`, `Moderate`, `High`) with exact missing counts and percentages from the quality audit script (`df.isna().sum()`).