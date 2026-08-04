import numpy as np
import matplotlib.pyplot as plt

# Load Planck TT spectrum
data = np.loadtxt("data/COM_PowerSpect_CMB-TT-full_R3.01.txt")

# Extract columns
ell = data[:,0]
Dl = data[:,1]
err_low = data[:,2]
err_high = data[:,3]

# Plot
plt.figure(figsize=(10,6))

plt.errorbar(
    ell,
    Dl,
    yerr=[err_low, err_high],
    fmt='.',
    color='black',
    markersize=3,
    capsize=2,
    label="Planck 2018"
)

plt.xlabel("Multipole ℓ", fontsize=12)
plt.ylabel(r"$D_\ell$ ($\mu K^2$)", fontsize=12)
plt.title("Planck 2018 TT Power Spectrum", fontsize=14)

plt.grid(True)
plt.legend()

plt.tight_layout()

plt.savefig("plots/Planck_TT.png", dpi=300)

plt.show()