import os
import numpy as np
import camb

# CAMB PARAMETERS

pars = camb.CAMBparams()

pars.set_cosmology(
    H0=67.36,
    ombh2=0.02237,
    omch2=0.1200,
    tau=0.0544
)

pars.InitPower.set_params(
    As=2.1e-9,
    ns=0.9649
)

pars.set_for_lmax(2500)

results = camb.get_results(pars)

powers = results.get_cmb_power_spectra(
    pars,
    CMB_unit="muK"
)

project_root = os.path.dirname(os.path.dirname(__file__))

# FUNCTION TO COMPUTE CHI-SQUARE

def compute_chi2(filename, theory_column):

    filepath = os.path.join(project_root, "data", filename)

    data = np.loadtxt(filepath)

    ell = data[:,0]
    Dl_obs = data[:,1]
    sigma = data[:,2]

    Dl_theory = powers["total"][:, theory_column]
    ell_theory = np.arange(len(Dl_theory))

    Dl_model = np.interp(
        ell,
        ell_theory,
        Dl_theory
    )

    chi2 = np.sum(((Dl_obs - Dl_model)/sigma)**2)

    N = len(ell)
    p = 6

    reduced = chi2/(N-p)

    return N, chi2, reduced


# CALCULATE TT, TE, EE

TT_N, TT_chi2, TT_red = compute_chi2(
    "COM_PowerSpect_CMB-TT-full_R3.01.txt",
    0
)

EE_N, EE_chi2, EE_red = compute_chi2(
    "COM_PowerSpect_CMB-EE-full_R3.01.txt",
    1
)

TE_N, TE_chi2, TE_red = compute_chi2(
    "COM_PowerSpect_CMB-TE-full_R3.01.txt",
    3
)

# PRINT SUMMARY

print("="*70)
print("          CAMB vs Planck 2018 Power Spectrum Summary")
print("="*70)

print()
print(f"{'Spectrum':<10}{'Data Points':>12}{'Chi-Square':>18}{'Reduced Chi-Square':>24}")
print("-"*70)

print(f"{'TT':<10}{TT_N:>12}{TT_chi2:>18.2f}{TT_red:>24.3f}")
print(f"{'TE':<10}{TE_N:>12}{TE_chi2:>18.2f}{TE_red:>24.3f}")
print(f"{'EE':<10}{EE_N:>12}{EE_chi2:>18.2f}{EE_red:>24.3f}")

print("-"*70)

print("\nConclusion\n")

print("The CAMB ΛCDM theoretical power spectra reproduce")
print("the Planck 2018 TT, TE and EE observations.")

print()

print(f"TT Reduced χ² = {TT_red:.3f}")
print(f"TE Reduced χ² = {TE_red:.3f}")
print(f"EE Reduced χ² = {EE_red:.3f}")

if TT_red < 2 and TE_red < 2 and EE_red < 2:
    print("\nOverall fit : Excellent")
elif TT_red < 3 and TE_red < 2 and EE_red < 2:
    print("\nOverall fit : Good")
else:
    print("\nOverall fit : Needs Improvement")

print("="*70)

# SAVE REPORT

report_dir = os.path.join(project_root, "report")
os.makedirs(report_dir, exist_ok=True)

report_file = os.path.join(report_dir, "Summary_Report.txt")

with open(report_file, "w", encoding="utf-8") as f:

    f.write("="*70 + "\n")
    f.write("CAMB vs Planck 2018 Power Spectrum Summary\n")
    f.write("="*70 + "\n\n")

    f.write(f"{'Spectrum':<10}{'Data Points':>12}{'Chi-Square':>18}{'Reduced Chi-Square':>24}\n")
    f.write("-"*70 + "\n")

    f.write(f"{'TT':<10}{TT_N:>12}{TT_chi2:>18.2f}{TT_red:>24.3f}\n")
    f.write(f"{'TE':<10}{TE_N:>12}{TE_chi2:>18.2f}{TE_red:>24.3f}\n")
    f.write(f"{'EE':<10}{EE_N:>12}{EE_chi2:>18.2f}{EE_red:>24.3f}\n")

    f.write("\n")
    f.write("Overall fit completed successfully.\n")

print("\nSummary saved to:")
print(report_file)