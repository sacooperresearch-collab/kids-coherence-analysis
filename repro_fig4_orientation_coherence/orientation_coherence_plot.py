#!/usr/bin/env python3
import matplotlib
matplotlib.use("Agg")   # ensures plotting works without a display

import pandas as pd
import matplotlib.pyplot as plt

# Input CSV must be in the same folder
CSV_FILE = "kids_tile_coherence.csv"

# Output image
OUT_FILE = "figure4_orientation_coherence.png"

# Load data
df = pd.read_csv(CSV_FILE)

# Main plot
fig, ax1 = plt.subplots(figsize=(7, 5))

ax1.plot(df["theta_arcmin"], df["C"], marker="o", lw=1.2, color="#1f77b4")
ax1.set_xscale("log")
ax1.set_xlabel(r"$\theta$ (arcmin)")
ax1.set_ylabel(r"$C(\theta)$")
ax1.grid(True, which="both", ls=":", alpha=0.5)
ax1.set_title("Figure 4 — Orientation Coherence $C(\\theta)$\nS. A. Cooper, *From Scratch*")

# Pairs per bin (optional)
ax2 = ax1.twinx()
ax2.plot(df["theta_arcmin"], df["pairs"], color="#ff7f0e", lw=1.0, alpha=0.6)
ax2.set_ylabel("Pairs per bin", color="#ff7f0e")
ax2.tick_params(axis="y", labelcolor="#ff7f0e")

fig.tight_layout()
fig.savefig(OUT_FILE, dpi=300)
plt.close(fig)

print(f"Saved: {OUT_FILE}")
