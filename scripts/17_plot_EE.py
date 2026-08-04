import os
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

# COMPUTE EE SPECTRUM

results = camb.get_results(pars)

powers = results.get_cmb_power_spectra(
    pars,
    CMB_unit="muK"
)

totCL = powers["total"]

ell = range(totCL.shape[0])

# EE spectrum (column 1)
Dl_EE = totCL[:,1]

# PLOT
plt.figure(figsize=(12,7))

plt.plot(
    ell,
    Dl_EE,
    color="darkgreen",
    linewidth=2.5,
    label="CAMB EE Spectrum"
)

plt.title(
    "Theoretical CMB E-mode Polarization (EE) Power Spectrum",
    fontsize=16,
    weight="bold"
)

plt.xlabel(
    r"Multipole Moment, $\ell$",
    fontsize=14
)

plt.ylabel(
    r"$D_\ell^{EE}\ (\mu K^2)$",
    fontsize=14
)

plt.xlim(2,2500)

plt.grid(alpha=0.3)

plt.legend(fontsize=12)

project_root = os.path.dirname(os.path.dirname(__file__))
plots_dir = os.path.join(project_root,"plots")

os.makedirs(plots_dir,exist_ok=True)

plt.savefig(
    os.path.join(plots_dir,"EE_theory.png"),
    dpi=600,
    bbox_inches="tight"
)

plt.savefig(
    os.path.join(plots_dir,"EE_theory.pdf"),
    bbox_inches="tight"
)

plt.show()