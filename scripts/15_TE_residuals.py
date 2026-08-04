import os
import numpy as np
import camb
import matplotlib.pyplot as plt

# CAMB ΛCDM PARAMETERS

pars = camb.CAMBparams()

pars.set_cosmology(
    H0=67.36,
    ombh2=0.02237,
    omch2=0.1200,
    mnu=0.06,
    omk=0,
    tau=0.0544
)

pars.InitPower.set_params(
    As=2.100e-9,
    ns=0.9649,
    r=0
)

pars.set_for_lmax(2500, lens_potential_accuracy=0)

results = camb.get_results(pars)

powers = results.get_cmb_power_spectra(
    pars,
    CMB_unit='muK'
)

totCL = powers['total']

ell_theory = np.arange(totCL.shape[0])

# TE spectrum is column 3
Dl_TE_theory = totCL[:, 3]


# LOAD PLANCK 2018 TE DATA

project_root = os.path.dirname(os.path.dirname(__file__))

planck_file = os.path.join(
    project_root,
    "data",
    "COM_PowerSpect_CMB-TE-full_R3.01.txt"
)

data = np.loadtxt(planck_file)

ell = data[:,0]
Dl_TE = data[:,1]
err = data[:,2]

# MATCH THEORY TO OBSERVED MULTIPOLES

Dl_theory_interp = np.interp(
    ell,
    ell_theory,
    Dl_TE_theory
)


# RESIDUALS
residual = Dl_TE - Dl_theory_interp

# PLOT

plt.figure(figsize=(12,7))

plt.scatter(
    ell,
    residual,
    s=8,
    color='navy',
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
    "Residuals of the Planck 2018 TE Power Spectrum Relative to the CAMB ΛCDM Prediction",
    fontsize=16,
    weight='bold'
)

plt.xlabel(
    r"Multipole Moment, $\ell$",
    fontsize=14
)

plt.ylabel(
    r"$D_\ell^{TE,\mathrm{obs}}-D_\ell^{TE,\mathrm{theory}}\ (\mu K^2)$",
    fontsize=14
)

plt.grid(alpha=0.3)

plt.legend(fontsize=12)

plots_dir = os.path.join(project_root, "plots")
os.makedirs(plots_dir, exist_ok=True)

plt.savefig(
    os.path.join(plots_dir, "TE_Residuals.png"),
    dpi=600,
    bbox_inches="tight"
)

plt.savefig(
    os.path.join(plots_dir, "TE_Residuals.pdf"),
    bbox_inches="tight"
)

plt.show()

# PRINT SUMMARY

print("="*60)
print("TE Residual Analysis")
print("="*60)
print(f"Number of data points : {len(ell)}")
print(f"Mean residual         : {np.mean(residual):.3f} μK²")
print(f"Std. deviation        : {np.std(residual):.3f} μK²")
print("="*60)