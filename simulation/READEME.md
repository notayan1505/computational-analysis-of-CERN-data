# Monte Carlo Simulation of Z Boson Decay

This module simulates Z boson decays into muons using **Monte Carlo methods** and the **Voigt profile** — a convolution of the Lorentzian (decay width) and Gaussian (detector resolution) distributions. It helps model the expected shape of Z boson mass peaks in experimental data and compare them to ideal theoretical predictions.

## 🎯 Purpose

- Model realistic Z boson decays using known physical parameters
- Account for both:
  - **Decay width** (intrinsic particle lifetime)
  - **Detector smearing** (resolution limitations)
- Generate synthetic data for validation against experimental distributions

## 🧪 Methodology

1. **Define Voigt Profile**
   - Voigt = convolution of:
     - Lorentzian (decay width)
     - Gaussian (detector resolution)
   - Implemented using `scipy.special.wofz`

2. **Generate Fake Events**
   - Sample 10,000 Z boson decays across the 80–100 GeV mass range
   - Use theoretical values for:
     - Mean (μ): 91.188 GeV
     - Gaussian width (σ): 1.598 GeV
     - Lorentzian width (γ): 1.247 GeV

3. **Fit Voigt to Simulated Data**
   - Fit back a Voigt profile using `curve_fit` to see if parameters match
   - Reverse-engineer μ, σ, and γ from the histogram

## 📊 Results

| Parameter         | True Input | Fit Output |
|------------------|------------|------------|
| μ (mean)         | 91.188 GeV | 91.218 GeV |
| σ (Gaussian)     | 1.598 GeV  | 1.559 GeV  |
| γ (Lorentzian)   | 1.247 GeV  | 1.293 GeV  |

The fitted parameters closely match the true values, confirming that the simulation accurately reproduces Z boson behavior under expected conditions.

