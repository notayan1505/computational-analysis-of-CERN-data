# Proton-Proton Collisions and Computational Analysis of CERN (CMS) Open Data

This project explores particle physics using real data from the **Compact Muon Solenoid (CMS)** detector at CERN. By analyzing the **2011A DoubleMu Primary Dataset** from CERN’s Open Data Portal, we identify decay products of unstable particles — most notably the **Z boson** — through a combination of physics theory, data science, and machine learning.

> ⚠️ Note: This project was completed as a personal exploration by a high school student. While every effort was made to ensure correctness, this is a learning experience — not a peer-reviewed paper.

## 📁 Project Structure

├── Statistical Analysis/ # Processing ans Visualisation of Data using Numpy and Matplotlib

├── Numerical Analysis/ # Plotting Curves to Data and Background Subtraction

├── Machine Learning/ # PyTorch model and training scripts

├── Simulation/ # Monte Carlo Simulation to compare to Numerical Analysis

├── README.md #

└── Proton-Proton Collisions and Computational Analysis of CERN (CMS) DATA.pdf # Full project writeup


## 🧠 Concepts Covered

- The Standard Model of Particle Physics
- Quarks, Gluons, Bosons & Fundamental Forces
- Decay Width, Invariant Mass & Heisenberg’s Uncertainty Principle
- High-Energy Collisions & Detector Mechanics
- Background Subtraction in Data
- Monte Carlo Simulations
- Machine Learning Classification (PyTorch)

## 🧪 Dataset Used

**Source:** CERN Open Data Portal  
**Dataset:** [DoubleMu 2011A](https://opendata.cern.ch/record/5201)  
**Size:** ~100,000 events  
**Description:** Each event includes two detected muons. While not all events correspond to meaningful particle decays, the dataset is enhanced to make Z boson decays more observable for educational purposes.

## 🔬 Physics Goals

- Understand proton-proton collisions at the LHC
- Identify events indicative of **Z boson** decay into muon pairs
- Learn how **decay width** and **invariant mass** reveal particle identity
- Study statistical modeling of particle resonances using:
  - Gaussian (for detector smearing)
  - Lorentzian (for natural decay width)
  - Voigt Profile (convolution of the above two)

## 📈 Data Analysis Pipeline

### 1. Event Filtering
- Two muons of opposite charge
- Pseudorapidity |η| < 2.4
- Invariant mass between 0.3–300 GeV

### 2. Particle Labeling
- Assign event labels based on invariant mass windows for:
  - J/ψ and ψ(2S)
  - ϒ(1S), ϒ(2S), ϒ(3S)
  - Z boson

### 3. Background Subtraction
- Fit sidebands with quadratic polynomial
- Subtract to isolate Z boson signal

### 4. Curve Fitting
- Gaussian, Lorentzian, Voigt distribution fits
- Estimate decay width and compare to known values

### 5. Monte Carlo Simulation
- Generate Z boson events from Voigt distribution
- Compare simulated and ideal decay characteristics

## 🤖 Machine Learning

### Objective
Train a PyTorch model to classify events by decay type or background.

### Features
- Class weighting for imbalance (background = 80%)
- Threshold tuning for minority classes
- Confusion matrix, precision, recall, F1-score analysis

### Model Architecture

    nn.Sequential(
    
      nn.Linear(...),
    
      nn.BatchNorm1d(...),
    
      nn.LeakyReLU(),
    
      nn.Dropout(0.3),
    
    ...
)

## ✅ Result

- **Accuracy:** ~73%
- **Z Boson Detection:** No false negatives for Z boson class
- **Challenge:** Model struggles with distinguishing ϒ states due to class similarity and low sample counts

---

## 📊 Sample Results

- ~3000 Z boson candidate events after filtering
- **Mean invariant mass (Gaussian fit):** 90.889 GeV (vs expected 91.2 GeV)
- **Voigt simulation parameters:** Closely match theoretical expectations
- **Classifier Performance:** Successfully detects all true Z bosons despite class imbalance

---

## 🏁 Conclusion

This was a personal, curiosity-driven project combining particle physics, data science, and machine learning. While not perfect, it successfully models Z boson production and explores the use of deep learning on real CERN data.

---

## 👤 Author

**Ayan Gupta**  
Final-year high school student interested in engineering and machine learning.
