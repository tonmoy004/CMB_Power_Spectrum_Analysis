import camb
import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))

# Different baryon densities
baryon_values = [0.018, 0.020, 0.022, 0.024, 0.026]

for ombh2 in baryon_values:

    pars = camb.CAMBparams()

    pars.set_cosmology(
        H0=67.5,
        ombh2=ombh2,
        omch2=0.122
    )

    pars.InitPower.set_params(ns=0.965)

    pars.set_for_lmax(2500)

    results = camb.get_results(pars)

    powers = results.get_cmb_power_spectra(
        pars,
        CMB_unit='muK'
    )

    tt = powers['total'][:,0]

    ell = range(len(tt))

    plt.plot(
        ell,
        tt,
        label=f"$\\Omega_b h^2$ = {ombh2}"
    )

plt.xlim(2,2500)

plt.xlabel("Multipole ℓ")

plt.ylabel(r"$D_\ell$ ($\mu K^2$)")

plt.title("Effect of Baryon Density on CMB Power Spectrum")

plt.grid(True)

plt.legend()

plt.tight_layout()

plt.savefig("plots/Baryon_variation.png", dpi=300)

plt.show()