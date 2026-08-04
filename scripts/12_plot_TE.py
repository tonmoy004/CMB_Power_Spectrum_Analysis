import camb
import numpy as np
import matplotlib.pyplot as plt

# Set cosmological parameters
pars = camb.CAMBparams()

pars.set_cosmology(
    H0=67.5,
    ombh2=0.022,
    omch2=0.122
)

pars.InitPower.set_params(
    As=2e-9,
    ns=0.965
)

pars.set_for_lmax(2500, lens_potential_accuracy=0)

# Calculate CMB spectra
results = camb.get_results(pars)

powers = results.get_cmb_power_spectra(
    pars,
    CMB_unit='muK'
)

totCL = powers['total']

# Multipoles

ell = np.arange(totCL.shape[0])

# TE spectrum
TE = totCL[:, 3]

# Plot
plt.figure(figsize=(10,6))

plt.plot(
    ell,
    TE,
    color='darkred',
    linewidth=2,
    label='CAMB TE Spectrum'
)
plt.axhline(0, color='black', linestyle='--', linewidth=1)
plt.xlim(2,2500)
plt.ylim(-140, 120)
plt.xlabel(r"Multipole Moment, $\ell$", fontsize=14)

plt.ylabel(
    r"$D_\ell^{TE}\ (\mu K^2)$",
    fontsize=14
)

plt.title(
    "Theoretical CMB Temperature–Polarization (TE) Power Spectrum",
    fontsize=16,
    fontweight='bold'
)

plt.grid(alpha=0.3)

plt.legend()

plt.tight_layout()

plt.savefig(
    "plots/TE_theory.png",
    dpi=300
)

plt.show()