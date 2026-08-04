import os
import numpy as np
import matplotlib.pyplot as plt
import camb

# CAMB EE THEORY
pars = camb.CAMBparams()

pars.set_cosmology(
    H0=67.4,
    ombh2=0.0224,
    omch2=0.120
)

pars.InitPower.set_params(
    ns=0.965,
    As=2.1e-9
)

pars.set_for_lmax(2500)

results = camb.get_results(pars)
powers = results.get_cmb_power_spectra(pars, CMB_unit='muK')

totCL = powers['total']

ell_theory = np.arange(totCL.shape[0])
Dl_EE_theory = totCL[:, 1]

# LOAD PLANCK EE DATA

project_root = os.path.dirname(os.path.dirname(__file__))

filename = os.path.join(
    project_root,
    "data",
    "COM_PowerSpect_CMB-EE-full_R3.01.txt"
)

data = np.loadtxt(filename)

ell = data[:,0]
Dl_obs = data[:,1]
err = data[:,2]

# INTERPOLATE THEORY

Dl_theory_interp = np.interp(
    ell,
    ell_theory,
    Dl_EE_theory
)

# RESIDUALS

residuals = Dl_obs - Dl_theory_interp

print("="*60)
print("EE Residual Analysis")
print("="*60)

print()
print("Mean Residual :", np.mean(residuals))
print("Std Residual  :", np.std(residuals))
print()

# PLOT

plt.figure(figsize=(12,7))

plt.scatter(
    ell,
    residuals,
    s=12,
    color='darkgreen',
    alpha=0.7
)

plt.axhline(
    0,
    color='red',
    linestyle='--',
    linewidth=2,
    label='Zero Residual'
)

plt.title(
    "Residuals of the Planck 2018 EE Power Spectrum Relative to the CAMB ΛCDM Prediction",
    fontsize=18,
    fontweight='bold'
)

plt.xlabel(
    r"Multipole Moment, $\ell$",
    fontsize=14
)

plt.ylabel(
    r"$D_\ell^{EE,\mathrm{obs}}-D_\ell^{EE,\mathrm{theory}}\ (\mu K^2)$",
    fontsize=14
)

plt.grid(True, alpha=0.3)

plt.legend(fontsize=12)

plt.tight_layout()

# SAVE

plot_dir = os.path.join(project_root, "plots")
os.makedirs(plot_dir, exist_ok=True)

plt.savefig(
    os.path.join(plot_dir, "EE_Residuals.png"),
    dpi=600,
    bbox_inches="tight"
)

plt.savefig(
    os.path.join(plot_dir, "EE_Residuals.pdf"),
    dpi=600,
    bbox_inches="tight"
)

plt.show()