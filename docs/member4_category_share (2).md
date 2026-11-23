# Member 4: Category-Share Chart (Wind vs Solar)

## 1. Objective

The objective of this analysis is to compare wind and solar electricity generation in Great Britain from 1 January 2015 to 31 December 2019, and calculate each source's contribution to their combined generation.

## 2. Data and method

The analysis uses the group's cleaned dataset (`data/processed/cleaned_data.csv`) and two hourly generation columns:

- `GB_GBN_solar_generation_actual`
- `GB_GBN_wind_generation_actual` (total wind, onshore + offshore)

Method choices agreed for this chart:

- **Categories:** solar vs total wind (2 categories).
- **Study period:** complete calendar years only, 2015 to 2019.
- **Observations:** all available hourly rows. Missing values are skipped when the totals are calculated.

The available hourly values are summed for each source, converted from MWh to TWh, and used to calculate the percentage share.

**Calculation:**

`Contribution (%) = (Generation from one source / Combined wind and solar generation) x 100`

Missing hourly observations inside the study period: 48 solar hours and 40 wind hours.

## 3. Results

| Energy source | Generation (TWh) | Share of combined wind and solar (%) |
|---|---|---|
| Wind | 188.5 | 79.2% |
| Solar | 49.5 | 20.8% |
| **Combined total** | **238.0** | **100.0%** |

The yearly split was fairly stable: solar's share of the combined total ranged from 19.4% (2015) to 23.5% (2016).

## 4. Interpretation

Wind contributed the largest share of combined wind and solar electricity generation in Great Britain between 2015 and 2019, supplying 79.2% (188.5 TWh) while solar supplied 20.8% (49.5 TWh). This matters because most of the solar and wind electricity in Great Britain depends on wind, so output follows the weather, while solar adds a smaller daylight-only contribution. The split was fairly stable from year to year. The comparison covers only wind and solar, not all renewable sources, and 48 solar hours and 40 wind hours were missing and skipped, so the two sources are not summed over exactly the same hours.

## 5. Selected visualization

**Chart:** `category_share_wind_solar.png`

A horizontal bar chart is used because it makes the difference between the two percentage contributions easy to compare. The bars are labelled with each source's percentage and its generation in TWh.

**Supporting chart (optional):** `yearly_generation_wind_solar.png` shows annual wind and solar generation in TWh for 2015 to 2019.

## 6. Files for this contribution

- `04_category_share_chart.ipynb`: Python code for filtering the study period, calculating category shares, and creating the charts.
- `category_share_wind_solar.png`: exported category-share chart.
- `yearly_generation_wind_solar.png`: supporting yearly chart.
- `member4_category_share.md`: this methodology, results, and interpretation note.

## 7. Conclusion

Wind accounted for approximately four-fifths of combined wind and solar generation in Great Britain during 2015 to 2019, while solar accounted for approximately one-fifth. Within these two categories, wind was the dominant contributor over the period studied.

**Data source:** Open Power System Data (hourly time series, Great Britain columns).
