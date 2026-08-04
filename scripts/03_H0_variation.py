import camb
import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))

H0_values = [60, 65, 67.5, 70, 75]

for H0 in H0_values:

    pars = camb.CAMBparams()

    pars.set_cosmology(
        H0=H0,
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

    tt = powers['total'][:,0]

    ell = range(len(tt))

    plt.plot(
        ell,
        tt,
        label=f"H₀ = {H0}"
    )

plt.xlim(2,2500)

plt.xlabel("Multipole ℓ")

plt.ylabel(r"$D_\ell$ ($\mu K^2$)")

plt.title("Effect of Hubble Constant on CMB Power Spectrum")

plt.legend()

plt.grid(True)

plt.tight_layout()

plt.savefig("plots/H0_variation.png", dpi=300)

plt.show()