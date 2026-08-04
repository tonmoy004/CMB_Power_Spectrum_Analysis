import os
import numpy as np
import matplotlib.pyplot as plt

project_root = os.path.dirname(os.path.dirname(__file__))

filename = os.path.join(
    project_root,
    "data",
    "COM_PowerSpect_CMB-EE-full_R3.01.txt"
)

data = np.loadtxt(filename)

print("="*60)
print("Planck 2018 EE Power Spectrum")
print("="*60)

print()
print("Shape of dataset:", data.shape)

print()
print("First five rows:")
print(data[:5])

print()
print("Last five rows:")
print(data[-5:])

# Extract columns

ell = data[:,0]
Dl_EE = data[:,1]
err = data[:,2]

# Plot Planck EE spectrum

plt.figure(figsize=(12,7))

plt.errorbar(
    ell,
    Dl_EE,
    yerr=err,
    fmt='.',
    color='black',
    ecolor='gray',
    elinewidth=0.6,
    capsize=1,
    markersize=2,
    alpha=0.5
)

plt.title(
    "Planck 2018 EE Power Spectrum",
    fontsize=22,
    weight="bold"
)

plt.xlabel(
    r"Multipole Moment, $\ell$",
    fontsize=18
)

plt.ylabel(
    r"$D_\ell^{EE}$ ($\mu K^2$)",
    fontsize=18
)

plt.grid(alpha=0.3)

plt.xlim(2,2000)

plots_dir = os.path.join(project_root, "plots")
os.makedirs(plots_dir, exist_ok=True)

plt.savefig(
    os.path.join(plots_dir, "Planck_EE.png"),
    dpi=600,
    bbox_inches="tight"
)

plt.savefig(
    os.path.join(plots_dir, "Planck_EE.pdf"),
    bbox_inches="tight"
)

plt.show()