import camb
import matplotlib.pyplot as plt

plt.figure(figsize=(10,6))

ns_values = [0.92, 0.94, 0.965, 0.98, 1.00]

for ns in ns_values:

    pars = camb.CAMBparams()

    pars.set_cosmology(
        H0=67.5,
        ombh2=0.022,
        omch2=0.122
    )

    pars.InitPower.set_params(ns=ns)

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
        label=f"$n_s$ = {ns}"
    )

plt.xlim(2,2500)

plt.xlabel("Multipole ℓ")

plt.ylabel(r"$D_\ell$ ($\mu K^2$)")

plt.title("Effect of Scalar Spectral Index on CMB Power Spectrum")

plt.grid(True)

plt.legend()

plt.tight_layout()

plt.savefig("plots/ns_variation.png", dpi=300)

plt.show()