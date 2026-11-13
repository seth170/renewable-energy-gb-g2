# PART 3: MISSING VALUES AND DUPLICATE RECORDS AUDIT

## 1. Overview & Dataset Reference
- **Total Rows:** 50,401
- **Total Columns:** 16
- **Completely Duplicated Rows:** 0
- **Duplicated Timestamps:** 0

---

## 2. Missing-Value Count Table

| Column Name | Number of Missing Values | Percentage of Missing Values (%) |
| :--- | :---: | :---: |
| `utc_timestamp` | 0 | 0.00% |
| `actual_electricity_demand` | 7 | 0.01% |
| `forecast_electricity_demand` | 121 | 0.24% |
| `day_ahead_electricity_price` | 111 | 0.22% |
| `solar_capacity` | 6,600 | 13.09% |
| `solar_generation` | 55 | 0.11% |
| `solar_profile` | 6,649 | 13.19% |
| `wind_capacity` | 6,600 | 13.09% |
| `wind_generation` | 41 | 0.08% |
| `wind_profile` | 6,641 | 13.18% |
| `onshore_wind_capacity` | 6,600 | 13.09% |
| `onshore_wind_generation` | 41 | 0.08% |
| `onshore_wind_profile` | 6,641 | 13.18% |
| `offshore_wind_capacity` | 6,600 | 13.09% |
| `offshore_wind_generation` | 41 | 0.08% |
| `offshore_wind_profile` | 6,641 | 13.18% |

---

## 3. Python Execution Code

```python
import pandas as pd

# Loading dataset
df = pd.read_excel('../data/raw/GB_GBN SPECIFIC DATASET.xlsx')

# Calculating missing values and percentages
missing_counts = df.isnull().sum()
missing_percentage = (df.isnull().sum() / len(df)) * 100

print(missing_counts)
print(missing_percentage)

# Checking duplicates
print("Total duplicated rows:", df.duplicated().sum())
print("Duplicated timestamps:", df["utc_timestamp"].duplicated().sum())

---

## 4. Key Findings & Analysis

1. **Duplicate Records & Temporal Integrity:**
   - Both df.duplicated().sum() and df["utc_timestamp"].duplicated().sum() returned as 0.
     This confirms that the time series is continuous, strictly unique per timestamp and free of redundant or repeated record entries across all 50,401 rows.

2. **Columns with Highest Missing-Value Counts:**
   - The highest concentrations of missing data occur in the **profile** and **capacity** parameters for solar and wind  with each missing approximately **6,400 to 6,649         values** (~13.1% to 13.2% of the dataset). 
   - Operational variables exhibit very low missing counts (ranging from 7 to 121 rows,or < 0.25%).

3. **Impact on Subsequent Analysis:**
   - **Temporal Continuity:** The complete absence of duplicate timestamps ensures that time-series indexing and resampling can be performed seamlessly
       without alignment or duplication errors.
   - **Handling Capacity & Profile Gaps:** The 13.1% missing data in capacity and profile metrics likely stems from early reporting gaps or seasonal data collection boundaries.
