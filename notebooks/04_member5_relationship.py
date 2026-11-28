from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Locate cleaned dataset relative to repo root or notebooks/
candidates = [
    Path("..") / "data" / "processed" / "cleaned_data.csv",
    Path("data") / "processed" / "cleaned_data.csv",
]
DATA_PATH = next((p for p in candidates if p.exists()), None)
if DATA_PATH is None:
    raise FileNotFoundError("Could not find data/processed/cleaned_data.csv")

df = pd.read_csv(DATA_PATH, parse_dates=["utc_timestamp"])

# 2. Compute total renewable generation (Wind + Solar) in GW for readability
df["total_renewable_mw"] = (
    df["GB_GBN_wind_generation_actual"] + df["GB_GBN_solar_generation_actual"]
)
valid = df.dropna(subset=["total_renewable_mw", "GB_GBN_load_actual_entsoe_transparency"]).copy()

x_gw = valid["total_renewable_mw"] / 1000.0
y_gw = valid["GB_GBN_load_actual_entsoe_transparency"] / 1000.0

# 3. Calculate correlation and linear fit
r_val = x_gw.corr(y_gw)
slope, intercept = np.polyfit(x_gw, y_gw, 1)
x_line = np.linspace(x_gw.min(), x_gw.max(), 200)
y_line = slope * x_line + intercept

print(f"Valid hourly observations: {len(valid):,}")
print(f"Pearson correlation (r): {r_val:.4f}")
print(f"Linear fit: Demand (GW) = {slope:.3f} * Renewables (GW) + {intercept:.2f}")

# 4. Create scatter plot matching group styling conventions
fig, ax = plt.subplots(figsize=(9, 5.5))

ax.scatter(
    x_gw,
    y_gw,
    alpha=0.12,
    s=8,
    color="#1565C0",
    edgecolors="none",
    label="Hourly Observations",
)
ax.plot(
    x_line,
    y_line,
    color="#D84315",
    linewidth=2,
    label=f"Linear Trend (r = {r_val:.2f})",
)

ax.set_title(
    "Relationship Between Total Renewable Generation and Electricity Demand in GB",
    fontsize=12.5,
    fontweight="bold",
    pad=12,
)
ax.set_xlabel("Total Renewable Generation: Wind + Solar (GW)", fontsize=10.5)
ax.set_ylabel("Actual Electricity Demand (GW)", fontsize=10.5)
ax.spines[["top", "right"]].set_visible(False)
ax.grid(True, linestyle="--", alpha=0.3)
ax.legend(frameon=False, loc="upper right")

plt.tight_layout()

# 5. Export PNG to visuals/
out_dir = Path("..") / "visuals" if Path("..").joinpath("visuals").exists() else Path("visuals")
out_dir.mkdir(parents=True, exist_ok=True)
out_file = out_dir / "member5_renewables_vs_demand_scatter.png"
plt.savefig(out_file, dpi=300, bbox_inches="tight")
print(f"Saved chart to {out_file}")
plt.show()
