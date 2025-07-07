# Numerical Analysis of Z Boson Decay Events

This module performs **numerical analysis** on filtered dimuon data to isolate and characterize **Z boson** decay events. It combines background subtraction and statistical curve fitting to extract meaningful physical parameters from noisy experimental data.

## 🎯 Goals

- Identify genuine Z boson events in an enhanced educational dataset
- Subtract background noise using sideband fitting
- Fit appropriate distributions (Gaussian, Lorentzian, Voigt) to model decay properties
- Estimate mass, resolution, and decay width of the Z boson

---

## 🔍 Key Techniques

### 1. **Background Subtraction**

- The dataset includes background events labeled as class `6`
- Even within the Z boson invariant mass range (∼91.2 GeV), some background noise persists
- Fit a **quadratic curve** to the sidebands (regions outside the Z peak) and subtract it to isolate signal

### 2. **Distribution Fitting**

Fit three statistical models to the cleaned Z peak data:

#### 🟦 Gaussian
- Models **detector smearing**
- Mean: 90.889 GeV  
- Std. Dev: 1.8 GeV  
- ~0.3% off from real Z boson mass (91.2 GeV)

#### 🟪 Lorentzian (Breit-Wigner)
- Models **natural decay width**
- HWHM: ~1.685 GeV  
- FWHM (decay width): ~3.37 GeV  
- Slightly overestimated due to detector effects

#### 🟨 Voigt Profile
- **Convolution** of Gaussian + Lorentzian
- Best model for real collider data
- Fitted decay width was underestimated (~0.674 GeV), likely due to aggressive filtering and smeared tails

---

## 📊 Outcome

- ~3357 Z boson candidates after applying filtering and mass window
- ~3000 candidates after background subtraction
- Gaussian mean closely matches real value (90.889 GeV vs 91.2 GeV)
- Voigt profile fit underestimates decay width — likely due to signal purity overreach

---
