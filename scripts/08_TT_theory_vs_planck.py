import numpy as np
import matplotlib.pyplot as plt
import camb

# Load Planck data

data = np.loadtxt("data/COM_PowerSpect_CMB-TT-full_R3.01.txt")

ell_data = data[:,0]
Dl_data = data[:,1]
err_low = data[:,2]
err_high = data[:,3]

# CAMB Theory

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

Dl_theory = powers['total'][:,0]

ell_theory = np.arange(len(Dl_theory))

# Plot

plt.figure(figsize=(12,7))

plt.errorbar(
    ell_data,
    Dl_data,
    yerr=[err_low, err_high],
    fmt='.',
    markersize=3,
    color='black',
    alpha=0.7,
    label='Planck 2018'
)

plt.plot(
    ell_theory,
    Dl_theory,
    color='red',
    linewidth=2,
    label='CAMB Theory'
)

plt.xlim(2,2500)

plt.xlabel("Multipole ℓ", fontsize=12)
plt.ylabel(r"$D_\ell$ ($\mu K^2$)", fontsize=12)

plt.title("Planck Observation vs CAMB Theory")

plt.grid(True)

plt.legend()

plt.tight_layout()

plt.savefig("plots/Theory_vs_Planck.png", dpi=300)

plt.show()