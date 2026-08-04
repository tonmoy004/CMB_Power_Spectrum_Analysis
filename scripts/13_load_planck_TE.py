import os
import numpy as np
import matplotlib.pyplot as plt

# Locate project root

project_root = os.path.dirname(os.path.dirname(__file__))

filename = os.path.join(
    project_root,
    "data",
    "COM_PowerSpect_CMB-TE-full_R3.01.txt"
)

# Load Planck TE data

data = np.loadtxt(filename)

ell = data[:, 0]
Dl_TE = data[:, 1]
err = data[:, 2]

print("=" * 60)
print("Planck 2018 TE Power Spectrum")
print("=" * 60)

print("\nShape of dataset:", data.shape)

print("\nFirst five rows:\n")
print(data[:5])

print("\nLast five rows:\n")
print(data[-5:])

# Plot

plt.figure(figsize=(12,7))

plt.errorbar(
    ell,
    Dl_TE,
    yerr=err,
    fmt='.',
    color='black',
    ecolor='gray',
    markersize=2,
    elinewidth=0.6,
    capsize=1,
    alpha=0.5,
    label="Planck 2018"
)

plt.axhline(0, color='black', linestyle='--', linewidth=1)

plt.title(
    "Planck 2018 TE Power Spectrum",
    fontsize=22,
    fontweight='bold'
)

plt.xlabel(
    r"Multipole Moment, $\ell$",
    fontsize=18
)

plt.ylabel(
    r"$D_{\ell}^{TE}\ (\mu K^2)$",
    fontsize=22
)

plt.grid(True, alpha=0.3)

plt.legend(fontsize=14)

plt.tight_layout()


# Save figure
plot_dir = os.path.join(project_root, "plots")
os.makedirs(plot_dir, exist_ok=True)

plt.savefig(
    os.path.join(plot_dir, "Planck_TE.png"),
    dpi=600,
    bbox_inches="tight"
)

plt.show()