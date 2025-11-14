"""
Generate the standard two-point correlation plot C(theta) from a CSV file.

Requirements:
  - Python 3
  - pandas
  - matplotlib

Input:
  kids_coherence.csv
    Required columns:
      theta_arcmin : angular separation values
      C            : correlation measurements

Output:
  kids_coherence.pdf
  kids_coherence.png
"""

import matplotlib
matplotlib.use("Agg")   # required for headless environments

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Input file (must be in the same directory)
csv_path = Path("kids_coherence.csv")

if not csv_path.exists():
    raise FileNotFoundError(f"Missing required file: {csv_path}")

# Load data
df = pd.read_csv(csv_path)

# Create figure
plt.figure(figsize=(7, 5))
plt.plot(df["theta_arcmin"], df["C"], marker="o", color="black", lw=1)
plt.axhline(0, color="gray", lw=0.8)
plt.xscale("log")
plt.xlabel(r"$\theta$ (arcmin)")
plt.ylabel(r"$C(\theta)$")
plt.title("Standard Two-Point Correlation $C(\\theta)$ — KiDS Tile")
plt.grid(True, ls=":", lw=0.4)
plt.tight_layout()

# Save plot
plt.savefig("kids_coherence.pdf", dpi=300)
plt.savefig("kids_coherence.png", dpi=300)
plt.close()

print("Generated files:")
print("  kids_coherence.pdf")
print("  kids_coherence.png")
