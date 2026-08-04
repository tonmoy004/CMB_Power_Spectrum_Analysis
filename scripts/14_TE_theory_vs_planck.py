import numpy as np
import matplotlib.pyplot as plt
import camb
from camb import model

# CAMB ΛCDM PARAMETERS
pars = camb.CAMBparams()

pars.set_cosmology(
    H0=67.5,
    ombh2=0.022,
    omch2=0.122,
)

pars.InitPower.set_params(
    As=2e-9,
    ns=0.965
)

pars.set_for_lmax(2500)

results = camb.get_results(pars)

powers = results.get_cmb_power_spectra(
    pars,
    CMB_unit='muK'
)

totCL = powers['total']

print(totCL.shape)
print(totCL[:10])

# CAMB TE SPECTRUM
ell_theory = np.arange(totCL.shape[0])

Dl_TE_theory = totCL[:,3]

# LOAD PLANCK 2018 TE DATA

data = np.loadtxt("data/COM_PowerSpect_CMB-TE-full_R3.01.txt")

ell = data[:,0]

Dl_TE = data[:,1]

err_low = data[:,2]

err_high = data[:,3]

err = (err_low + err_high)/2

# PLOT

plt.figure(figsize=(12,7))

# CAMB prediction
plt.plot(
    ell_theory,
    Dl_TE_theory,
    color="darkred",
    linewidth=3,
    label="ΛCDM (CAMB)"
)

# Planck data
plt.errorbar(
    ell,
    Dl_TE,
    yerr=err,
    fmt='.',
    markersize=2,
    color='black',
    ecolor='gray',
    elinewidth=0.4,
    capsize=0,
    alpha=0.35,
    label='Planck 2018 TE'
)

# Zero line
plt.axhline(
    0,
    color='black',
    linestyle='--',
    linewidth=1.2
)

# Labels
plt.title(
    "Planck 2018 TE Power Spectrum vs. CAMB ΛCDM Prediction",
    fontsize=18,
    weight='bold'
)

plt.xlabel(
    r"Multipole Moment, $\ell$",
    fontsize=16
)

plt.ylabel(
    r"$D_\ell^{TE}\ (\mu K^2)$",
    fontsize=16
)

plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

plt.grid(
    True,
    linestyle='--',
    alpha=0.3
)

plt.legend(
    fontsize=14
)

plt.xlim(2,2500)

plt.grid(True, linestyle="--", alpha=0.35)

plt.tight_layout()

plt.savefig(
    "plots/TE_Theory_vs_Planck.png",
    dpi=600,
    bbox_inches='tight'
)

plt.show()