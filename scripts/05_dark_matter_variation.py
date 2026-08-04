import camb
import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))

# Different dark matter densities
dark_matter_values = [0.08, 0.10, 0.122, 0.14, 0.16]

for omch2 in dark_matter_values:

    pars = camb.CAMBparams()

    pars.set_cosmology(
        H0=67.5,
        ombh2=0.022,
        omch2=omch2
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
        label=f"$\\Omega_c h^2$ = {omch2}"
    )

plt.xlim(2,2500)

plt.xlabel("Multipole ℓ")

plt.ylabel(r"$D_\ell$ ($\mu K^2$)")

plt.title("Effect of Dark Matter Density on CMB Power Spectrum")

plt.grid(True)

plt.legend()

plt.tight_layout()

plt.savefig("plots/Dark_Matter_variation.png", dpi=300)

plt.show()