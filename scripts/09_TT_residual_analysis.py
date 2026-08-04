import numpy as np
import matplotlib.pyplot as plt
import camb

# Load Planck data

data = np.loadtxt("data/COM_PowerSpect_CMB-TT-full_R3.01.txt")

ell = data[:,0].astype(int)
Dl_obs = data[:,1]

# CAMB theory

pars = camb.CAMBparams()

pars.set_cosmology(
    H0=67.5,
    ombh2=0.022,
    omch2=0.122
)

pars.InitPower.set_params(ns=0.965)

pars.set_for_lmax(2500)

results = camb.get_results(pars)

powers = results.get_cmb_power_spectra(
    pars,
    CMB_unit='muK'
)

Dl_theory = powers["total"][:,0]

# Residuals

Dl_model = Dl_theory[ell]

residual = Dl_obs - Dl_model

# Plot

plt.figure(figsize=(12,5))

plt.axhline(
    y=0,
    color='red',
    linestyle='--',
    linewidth=1.8,
    label='Zero Residual (Observation = Theory)'
)

plt.scatter(
    ell,
    residual,
    s=8,
    color='navy',
    alpha=0.65,
    edgecolors='none'
)

plt.xlabel(r"Multipole Moment, $\ell$", fontsize=14)
plt.ylabel(
    r"$D_{\ell}^{\mathrm{obs}}-D_{\ell}^{\mathrm{theory}}\ (\mu K^2)$", 
    fontsize=14,
    labelpad=10
)
plt.title(
    "Residuals between the Planck 2018 TT Power Spectrum and the Best-Fit ΛCDM Model Computed with CAMB",
    fontsize=16,
    fontweight='bold'
)
plt.grid(
    linestyle=':',
    alpha=0.6
)
plt.legend(fontsize=12)
plt.tight_layout()

plt.savefig(
    "plots/Residuals.png",
    dpi=600,
    bbox_inches='tight'
)
plt.savefig(
    "plots/Residuals.pdf",
    bbox_inches="tight"
)
plt.show()