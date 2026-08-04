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
    As=2.10e-9,
    ns=0.9649,
    r=0
)

pars.set_for_lmax(2500)

results = camb.get_results(pars)

powers = results.get_cmb_power_spectra(
    pars,
    CMB_unit="muK"
)

totCL = powers["total"]

ell_theory = np.arange(totCL.shape[0])

# EE spectrum (column 1)
Dl_EE_theory = totCL[:,1]

# LOAD PLANCK EE DATA
project_root = os.path.dirname(os.path.dirname(__file__))

filename = os.path.join(
    project_root,
    "data",
    "COM_PowerSpect_CMB-EE-full_R3.01.txt"
)

data = np.loadtxt(filename)

ell = data[:,0]

Dl_EE = data[:,1]

err = data[:,2]

# PLOT

plt.figure(figsize=(12,7))

# CAMB prediction
plt.plot(
    ell_theory,
    Dl_EE_theory,
    color="darkgreen",
    linewidth=3,
    label=r"$\Lambda$CDM (CAMB)"
)

# Planck observations
plt.errorbar(
    ell,
    Dl_EE,
    yerr=err,
    fmt='.',
    markersize=2,
    color='black',
    ecolor='lightgray',
    elinewidth=0.6,
    capsize=1,
    alpha=0.45,
    label='Planck 2018 EE'
)

plt.title(
    "Planck 2018 EE Power Spectrum Compared with the ΛCDM Prediction from CAMB",
    fontsize=16,
    weight='bold'
)

plt.xlabel(
    r"Multipole Moment, $\ell$",
    fontsize=14
)

plt.ylabel(
    r"$D_\ell^{EE}$ ($\mu$K$^2$)",
    fontsize=14
)

plt.xlim(2,2500)

plt.grid(alpha=0.3, linestyle='--')

plt.legend(fontsize=12)

plots_dir = os.path.join(project_root,"plots")

os.makedirs(plots_dir,exist_ok=True)

plt.savefig(
    os.path.join(plots_dir,"EE_Theory_vs_Planck.png"),
    dpi=600,
    bbox_inches="tight"
)

plt.savefig(
    os.path.join(plots_dir,"EE_Theory_vs_Planck.pdf"),
    bbox_inches="tight"
)

plt.show()