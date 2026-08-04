# Cosmic Microwave Background Power Spectrum Analysis Using CAMB and Planck 2018 Data

## Overview

This project presents a computational analysis of the Cosmic Microwave Background (CMB) power spectra using the Code for Anisotropies in the Microwave Background (CAMB) and compares the theoretical predictions with the Planck 2018 observational data.

The project investigates the three primary angular power spectra:

- TT (Temperature–Temperature)
- TE (Temperature–E-mode Polarization)
- EE (E-mode Polarization)

The analysis includes theoretical spectrum generation, comparison with observations, residual analysis, chi-square goodness-of-fit tests, and summary report generation.

---

## Objectives

- Generate theoretical TT, TE and EE power spectra using CAMB.
- Compare the theoretical spectra with Planck 2018 observations.
- Study the influence of cosmological parameters on the CMB power spectra.
- Perform residual analysis.
- Calculate Chi-square and Reduced Chi-square statistics.
- Summarize the statistical agreement between the ΛCDM model and Planck observations.

---

## Project Structure

```
CMB_Power_Spectrum_Analysis
│
├── data/
│   ├── COM_PowerSpect_CMB-TT-full_R3.01.txt
│   ├── COM_PowerSpect_CMB-TE-full_R3.01.txt
│   └── COM_PowerSpect_CMB-EE-full_R3.01.txt
│
├── plots/
│
├── report/
│
├── scripts/
│   ├── 01_test_camb.py
│   ├── 02_plot_TT.py
│   ├── 03_H0_variation.py
│   ├── 04_baryon_variation.py
│   ├── 05_dark_matter_variation.py
│   ├── 06_spectral_index_variation.py
│   ├── 07_load_planck_TT.py
│   ├── 08_TT_theory_vs_planck.py
│   ├── 09_TT_residual_analysis.py
│   ├── 10_TT_chi_square.py
│   ├── 11_acoustic_peaks.py
│   ├── 12_plot_TE.py
│   ├── 13_load_planck_TE.py
│   ├── 14_TE_theory_vs_planck.py
│   ├── 15_TE_residuals.py
│   ├── 16_TE_chi_square.py
│   ├── 17_plot_EE.py
│   ├── 18_load_planck_EE.py
│   ├── 19_EE_theory_vs_planck.py
│   ├── 20_EE_residuals.py
│   ├── 21_EE_chi_square.py
│   └── 22_summary_report.py
│
├── README.md
└── requirements.txt
```

---

## Software Requirements

- Python 3.x
- CAMB
- NumPy
- Matplotlib

Install the required packages using

```bash
pip install -r requirements.txt
```

---

## Workflow

1. Configure CAMB using the Planck 2018 best-fit ΛCDM parameters.
2. Generate theoretical TT, TE and EE spectra.
3. Load the Planck 2018 observational datasets.
4. Compare theory with observations.
5. Calculate residuals.
6. Compute Chi-square and Reduced Chi-square.
7. Generate a final statistical summary.

---

## Results

The theoretical ΛCDM spectra generated using CAMB successfully reproduce the main features of the Planck 2018 TT, TE and EE power spectra.

Residual analysis shows that the differences between theory and observations are generally small compared with the observational uncertainties.

Reduced Chi-square values close to unity indicate good agreement between the theoretical ΛCDM model and the observational data.

---

## References

1. Planck Collaboration (2020), *Planck 2018 Results. VI. Cosmological Parameters*.
2. Lewis, A., Challinor, A., & Lasenby, A. (2000), *Efficient Computation of CMB Anisotropies in Closed FRW Models*.
3. CAMB Documentation — https://camb.info/

---


## Zenodo Release

This repository is archived on Zenodo for reproducibility and citation.

---



## Author

**Tonmoy Goswami**

M.Sc. Physics

Department of Physics

National Institute of Technology Meghalaya