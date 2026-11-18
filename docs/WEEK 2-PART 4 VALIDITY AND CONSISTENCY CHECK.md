**WEEK 2 – PART 4: DATA QUALITY AUDIT**

**4.1 Introduction**

Data validity and consistency checks were conducted on the selected Great Britain (GB_GBN) subset of the Open Power System Data (OPSD) time-series dataset.

The purpose of this investigation was to assess whether the dataset contains valid values, consistent formats, unusual observations, negative values, zero values and missing data.

The checks focused on the timestamp column and the 15 numerical variables relating to electricity demand, electricity prices, solar energy and wind energy.

The original dataset was not modified during this investigation.

**4.2 Timestamp Format Verification**

The utc_timestamp column was examined to determine whether the timestamps followed a consistent date-and-time format.

The timestamps were displayed in ISO 8601 format, for example:

2016-09-15T18:00:00Z

The format contains:

- Date: Year, month and day.
- Time: Hour, minute and second.
- Time zone: UTC, indicated by Z.

**Finding:** The displayed timestamps follow a consistent ISO 8601 UTC format.

**4.3 Identification of Numerical Columns**

The numerical columns were identified using:

df.select_dtypes(include="number").columns

The dataset contains 15 numerical columns, covering:

- Actual and forecast electricity demand.
- Day-ahead electricity prices.
- Solar capacity, actual generation and profile.
- Wind capacity, actual generation and profile.
- Offshore and onshore wind capacity, actual generation and profiles.

These numerical variables were subsequently examined using descriptive statistics and validity checks.

**4.4 Descriptive Statistics**

The df.describe() function was used to examine the numerical variables.

This provided information on:

- Count of available observations.
- Mean and standard deviation.
- Minimum and maximum values.
- First quartile (25th percentile).
- Median (50th percentile).
- Third quartile (75th percentile).

The descriptive statistics helped identify unusual values and understand the distribution of the numerical variables.

One observation requiring further investigation was the unusually high electricity price of 999.00.

**4.5 Investigation of Unusually High Electricity Prices**

The GB_GBN_price_day_ahead column was examined to identify unusually high electricity prices.

The investigation initially identified:

- 999.00, occurring once.
- 799.00, occurring once.

The surrounding records showed that these values occurred on 15 September 2016.

The prices were:

- 15:00 UTC – 50.00
- 16:00 UTC – 50.00
- 17:00 UTC – 50.00
- 18:00 UTC – 999.00
- 19:00 UTC – 799.00
- 20:00 UTC – 99.92
- 21:00 UTC – 33.49

This indicated a sudden increase in electricity prices followed by a decline.

The ten highest electricity prices were also examined:

| **Date and time (UTC)**  | **Price** |
| ------------------------ | --------- |
| 15 September 2016, 18:00 | 999.00    |
| 15 September 2016, 19:00 | 799.00    |
| 19 September 2016, 16:00 | 500.00    |
| 19 September 2016, 17:00 | 750.00    |
| 19 September 2016, 18:00 | 960.00    |
| 19 September 2016, 19:00 | 747.00    |
| 7 November 2016, 17:00   | 796.00    |
| 8 November 2016, 17:00   | 775.92    |
| 9 November 2016, 17:00   | 600.01    |
| 14 November 2016, 17:00  | 700.00    |

**Finding:** The dataset contains several unusually high electricity prices occurring across different dates. Some occurred consecutively over several hours.

These observations may represent genuine electricity market price spikes. Therefore, they were flagged for further investigation rather than automatically classified as errors.

**4.6 Statistical Outlier Detection Using the IQR Method**

The Interquartile Range (IQR) method was applied to the day-ahead electricity price column to identify potential statistical outliers.

The following values were obtained:

| **Statistic**                | **Result** |
| ---------------------------- | ---------- |
| First Quartile (Q1)          | 33.88      |
| Third Quartile (Q3)          | 50.40      |
| Interquartile Range (IQR)    | 16.52      |
| Lower Bound                  | 9.10       |
| Upper Bound                  | 75.18      |
| Number of Potential Outliers | 1,804      |

The IQR was calculated as:

IQR = Q3 − Q1

IQR = 50.40 − 33.88 = 16.52

The outlier boundaries were calculated using:

Lower Bound = Q1 − (1.5 × IQR)

Upper Bound = Q3 + (1.5 × IQR)

Values below 9.10 or above 75.18 were classified as potential statistical outliers.

**Finding:** A total of 1,804 potential outliers were identified in the day-ahead electricity price column.

However, statistical outliers are not necessarily incorrect observations. Electricity prices can fluctuate considerably due to changes in supply and demand. Therefore, these observations require further investigation before any cleaning decisions are made.

**4.7 Investigation of Negative Electricity Prices**

The day-ahead electricity price column was examined for negative values.

A total of **81 negative electricity prices** were identified.

Ten examples included:

| **Date and time (UTC)** | **Electricity price** |
| ----------------------- | --------------------- |
| 9 December 2019, 03:00  | \-2.84                |
| 16 February 2020, 02:00 | \-0.18                |
| 16 February 2020, 03:00 | \-4.33                |
| 16 February 2020, 04:00 | \-4.21                |
| 16 February 2020, 05:00 | \-1.11                |
| 5 April 2020, 11:00     | \-0.02                |
| 5 April 2020, 12:00     | \-9.28                |
| 5 April 2020, 13:00     | \-19.00               |
| 5 April 2020, 14:00     | \-4.35                |
| 13 April 2020, 03:00    | \-0.08                |

Negative electricity prices can occur in electricity markets when electricity supply exceeds demand and generators have incentives to continue supplying electricity.

**Finding:** The 81 negative prices were flagged for investigation but were not automatically classified as invalid values.

**4.8 Negative Value Checks Across Numerical Columns**

All 15 numerical columns were examined to determine whether they contained negative values.

The results were:

| **Numerical Column**              | **Number of Negative Values** |
| --------------------------------- | ----------------------------- |
| Actual electricity load           | 0                             |
| Forecast electricity load         | 0                             |
| Day-ahead electricity price       | 81                            |
| Solar capacity                    | 0                             |
| Solar generation (actual)         | 0                             |
| Solar profile                     | 0                             |
| Wind capacity                     | 0                             |
| Wind generation (actual)          | 0                             |
| Wind profile                      | 0                             |
| Offshore wind capacity            | 0                             |
| Offshore wind generation (actual) | 0                             |
| Offshore wind profile             | 0                             |
| Onshore wind capacity             | 0                             |
| Onshore wind generation (actual)  | 0                             |
| Onshore wind profile              | 0                             |

**Finding:** Negative values were identified only in the day-ahead electricity price column. The other 14 numerical columns contained no negative observations.

**4.9 Investigation of Zero Values**

The numerical columns were examined to determine how frequently zero values occurred.

The results were:

| **Numerical Column**              | **Number of Zero Values** |
| --------------------------------- | ------------------------- |
| Actual electricity load           | 0                         |
| Forecast electricity load         | 0                         |
| Day-ahead electricity price       | 57                        |
| Solar capacity                    | 0                         |
| Solar generation (actual)         | 20,037                    |
| Solar profile                     | 17,655                    |
| Wind capacity                     | 0                         |
| Wind generation (actual)          | 4                         |
| Wind profile                      | 4                         |
| Offshore wind capacity            | 0                         |
| Offshore wind generation (actual) | 14                        |
| Offshore wind profile             | 13                        |
| Onshore wind capacity             | 0                         |
| Onshore wind generation (actual)  | 4                         |
| Onshore wind profile              | 4                         |

**Findings and interpretation:**

1. Solar generation contained 20,037 zero values. These may represent periods when solar electricity was not being generated, particularly during nighttime hours.
2. Solar profile contained 17,655 zero values. These may also reflect periods of little or no solar generation.
3. Wind generation and wind profile columns contained relatively few zero values.
4. The day-ahead electricity price column contained 57 zero values. These were not automatically classified as errors.
5. None of the four capacity columns contained zero values.

Zero values were distinguished from missing values because zero represents an observed numerical value, whereas a missing value indicates that an observation is unavailable.

**4.10 Investigation of Missing Values**

Missing values were examined using the isna().sum() function across all 15 numerical columns.

The results were:

| **Numerical Column**              | **Number of Missing Values** |
| --------------------------------- | ---------------------------- |
| Actual electricity load           | 7                            |
| Forecast electricity load         | 121                          |
| Day-ahead electricity price       | 111                          |
| Solar capacity                    | 6,600                        |
| Solar generation (actual)         | 55                           |
| Solar profile                     | 6,649                        |
| Wind capacity                     | 6,600                        |
| Wind generation (actual)          | 41                           |
| Wind profile                      | 6,641                        |
| Offshore wind capacity            | 6,600                        |
| Offshore wind generation (actual) | 41                           |
| Offshore wind profile             | 6,641                        |
| Onshore wind capacity             | 6,600                        |
| Onshore wind generation (actual)  | 41                           |
| Onshore wind profile              | 6,641                        |

**Key observations:**

1. All four capacity columns contained exactly 6,600 missing values, suggesting a shared data-availability pattern.
2. Solar profile had the highest number of missing values, with 6,649.
3. Offshore and onshore wind profiles each contained 6,641 missing values.
4. Electricity load and price columns had comparatively fewer missing values.
5. Actual solar and wind generation columns also contained missing observations, ranging from 41 to 55.

**Finding:** Missing values are present throughout the numerical dataset, with particularly high concentrations in capacity and renewable energy profile columns.

These missing values require further investigation before deciding whether to retain, replace or remove affected observations.

**4.11 Duplicate Record Verification**

Duplicate records were checked during the dataset profiling process.

**Finding:** Zero duplicate records were identified.

This indicates that no identical duplicate records were detected in the dataset.

**4.12 Overall Findings and Recommendations**

The validity and consistency investigation revealed several important characteristics of the selected GB_GBN dataset.

The main findings include:

- The timestamps follow a consistent ISO 8601 UTC display format.
- The dataset contains 15 numerical variables.
- No duplicate records were identified.
- The day-ahead electricity price column contains 81 negative values and 57 zero values.
- Several unusually high electricity prices were identified, with 999.00 being the highest.
- The IQR method identified 1,804 potential statistical outliers in the electricity price column.
- The other 14 numerical columns contained no negative values.
- Solar generation and solar profile columns contained substantial numbers of zero values.
- Missing values were identified in all 15 numerical columns.
- The capacity and renewable energy profile columns had comparatively high missing-value counts.

Based on these findings, the following recommendations were made:

1. Investigate unusual electricity prices before deciding whether they should be retained or treated as errors.
2. Retain legitimate negative and zero electricity prices.
3. Investigate missing values in capacity and renewable energy profile columns to understand their causes.
4. Distinguish genuine zero generation from missing generation records.
5. Avoid automatically replacing missing values with zero.
6. Preserve the original dataset and document all cleaning decisions during the next stage of the project.

**4.13 Conclusion**

The data validity and consistency checks provided a clearer understanding of the quality and characteristics of the selected Great Britain electricity dataset.

Although the dataset contains missing values, unusual electricity prices, negative prices and numerous zero observations, these findings do not necessarily indicate that the dataset is unreliable.

Some unusual observations may reflect genuine electricity market conditions and renewable energy generation patterns.

The investigation established the areas requiring attention during data cleaning and preparation.

The dataset was therefore considered suitable for proceeding to the next stage of the project, subject to further investigation and appropriate handling of the identified data-quality issues.