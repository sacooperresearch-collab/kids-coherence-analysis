# Figure 4 Reproduction — Orientation Coherence

This folder reproduces **Figure 4** from  
**S. A. Cooper, *From Scratch: An Empirical Measurement of Scale-Dependent Coherence in KiDS DR4.1 Shapes*.**

## Files
- `kids_tile_coherence.csv` — input data  
  Columns:
  - `theta_arcmin`
  - `C`
  - `pairs`

- `orientation_coherence_plot.py` — script that generates the figure  
- `figure4_orientation_coherence.png` — output after running the script

## Requirements
- Python 3  
- pandas  
- matplotlib  

## Usage
Run:

```bash
python orientation_coherence_plot.py

