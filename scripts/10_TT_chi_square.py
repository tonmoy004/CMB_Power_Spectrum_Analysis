import os
import numpy as np
import camb

# CAMB Theory

pars = camb.CAMBparams()

pars.set_cosmology(
    H0=67.36,
    ombh2=0.02237,
    omch2=0.1200,
    tau=0.0544
)

pars.InitPower.set_params(
    As=2.1e-9,
    ns=0.9649
)

pars.set_for_lmax(2500)

results = camb.get_results(pars)

powers = results.get_cmb_power_spectra(
    pars,
    CMB_unit="muK"
)

Dl_theory = powers["total"][:,0]
ell_theory = np.arange(len(Dl_theory))

# Load Planck TT Data

project_root = os.path.dirname(os.path.dirname(__file__))

filename = os.path.join(
    project_root,
    "data",
    "COM_PowerSpect_CMB-TT-full_R3.01.txt"
)

data = np.loadtxt(filename)

ell = data[:,0].astype(int)
Dl_obs = data[:,1]
sigma = data[:,2]

# Interpolate Theory

Dl_model = np.interp(
    ell,
    ell_theory,
    Dl_theory
)

# Chi-Square

chi2 = np.sum(((Dl_obs - Dl_model)/sigma)**2)

N = len(ell)
p = 6

reduced_chi2 = chi2/(N-p)

# Print

print("="*60)
print("TT Chi-Square Analysis")
print("="*60)

print()
print(f"Number of data points : {N}")
print(f"Chi-square            : {chi2:.2f}")
print(f"Reduced Chi-square    : {reduced_chi2:.3f}")

print("="*60)