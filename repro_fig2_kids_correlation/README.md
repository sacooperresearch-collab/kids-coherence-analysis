# Reproduction Materials for Figure 2

This folder contains all files required to reproduce Figure 2 from the paper:

**“From Scratch: An Empirical Measurement of Scale-Dependent Coherence in KiDS DR4.1 Shapes.”**

Figure 2 shows the standard two-point correlation function  
\( C(\theta) \) computed from preprocessed KiDS ellipticity data.

The CSV provided here is the exact precomputed correlation output used in the paper; no access to the raw KiDS catalog is required to reproduce the figure.

## Contents

- **kids_coherence.csv**  
  Precomputed correlation measurements.  
  Columns:
  - `theta_arcmin` — angular separation (arcmin)  
  - `C` — measured correlation amplitude  

- **kids_coherence_plot.py**  
  Python script that generates the Figure 2 plot from the CSV.

- **kids_coherence.png** *(optional)*  
  Example output produced by the script.

## Requirements

- Python 3  
- `pandas`  
- `matplotlib`
