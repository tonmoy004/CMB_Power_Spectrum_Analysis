import camb
from camb import model
import matplotlib.pyplot as plt

# Create a CAMB parameter object
pars = camb.CAMBparams()

# Set cosmological parameters
pars.set_cosmology(
    H0=67.5,
    ombh2=0.022,
    omch2=0.122
)

# Set primordial power spectrum
pars.InitPower.set_params(
    ns=0.965
)

# Calculate spectra up to l = 2500
pars.set_for_lmax(
    2500,
    lens_potential_accuracy=0
)

# Get results
results = camb.get_results(pars)

# Get CMB power spectra
powers = results.get_cmb_power_spectra(
    pars,
    CMB_unit='muK'
)

# Total power spectrum
totCL = powers['total']

# Multipole values
ells = range(totCL.shape[0])

# Plot TT spectrum
plt.figure(figsize=(10,6))

plt.plot(
    ells,
    totCL[:,0],
    color='blue',
    linewidth=2
)

plt.xlim(2,2500)

plt.xlabel("Multipole ℓ", fontsize=12)

plt.ylabel(r"$D_\ell\ (\mu K^2)$", fontsize=12)

plt.title("Theoretical CMB Temperature Power Spectrum")

plt.grid(True)

plt.tight_layout()

plt.savefig(r"plots/TT_theory.png", dpi=300)

plt.show()