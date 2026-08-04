import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import camb

# Generate CAMB TT Spectrum

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

Dl = powers['total'][:,0]

ell = np.arange(len(Dl))

# Detect Peaks

peaks, _ = find_peaks(
    Dl,
    prominence=50,
    distance=120
)

# Ignore very low multipoles
peaks = peaks[peaks > 30]

# Keep only first five peaks
peaks = peaks[:5]

# Print Results

print("="*60)
print("Acoustic Peaks")
print("="*60)

print(f"{'Peak':<8}{'Multipole (ℓ)':<18}{'Dℓ (μK²)':<15}")

for i, p in enumerate(peaks, start=1):
    print(f"{i:<8}{p:<18}{Dl[p]:.2f}")

print("="*60)

# Plot

plt.figure(figsize=(12,7))

plt.plot(
    ell,
    Dl,
    color='navy',
    linewidth=2,
    label='CAMB TT Spectrum'
)

plt.scatter(
    peaks,
    Dl[peaks],
    color='red',
    s=60,
    zorder=5,
    label='Acoustic Peaks'
)

# Label peaks
for i, p in enumerate(peaks, start=1):
    plt.annotate(
        f"Peak {i}\nl={p}",
        (p, Dl[p]),
        xytext=(15, 12),
        textcoords="offset points",
        ha='center',
        fontsize=9,
        fontweight='bold'
    )

plt.ylim(0,5600)
plt.xlabel(r"Multipole Moment, $\ell$", fontsize=12)
plt.ylabel(r"$D_\ell$ ($\mu$K$^2$)", fontsize=12)

plt.title(
    "Identification of the First Five Acoustic Peaks in the Theoretical CMB TT Power Spectrum",
    fontsize=14,
    fontweight="bold"
)

plt.grid(alpha=0.3)

plt.legend()

plt.tight_layout()

plt.savefig(
    "plots/Acoustic_Peaks.png",
    dpi=600,
    bbox_inches="tight"
)
plt.savefig(
    "plots/Acoustic_Peaks.pdf",
    bbox_inches="tight"
)

plt.show()