# 💡 Dimuon Event Computational Analysis - Statistical Analysis

This project analyzes real high-energy physics data from dimuon collision events, focusing on identifying and visualizing the presence of fundamental particles such as **J/ψ**, **ψ(2S)**, **ϒ(nS)** states, and the **Z boson**. These particles decay into muons, and using the muon kinematic data, we classify the originating particles by their invariant mass, taking into account realistic uncertainty ranges around nominal particle masses. Using Python, we label particle signatures dynamically based on mass windows defined by combined physics and detector uncertainties, and visualize their distributions through detailed statistical and graphical analysis. This covers the statistical analysis of the project, giving an insight into the data we are working with.

---

## 📁 Dataset

Dataset is available in CSV format here: https://opendata.cern.ch/record/5201  
The dataset, `Dimuon_DoubleMu.csv`, contains kinematic variables from dimuon decay events in a particle detector. Each row corresponds to a single event and includes:

- Energies: `E1`, `E2`  
- Momentum components: `px1`, `py1`, `pz1`, `px2`, `py2`, `pz2`  
- Charge: `Q1`, `Q2`  
- Invariant mass: `M`  

---

## 📚 Dataset Context and Origin

The dataset was derived from the **CMS Run2011A DoubleMu primary dataset** and is intended for **educational and outreach** purposes. It contains **100,000 events** where two muon candidates were observed. Events were selected under the following conditions:

- Both muons have **|η| < 2.4**
- At least one muon is a **global muon**
- Muon pair must have **opposite charges**
- Invariant mass is in the range **0.3 < M < 300 GeV**

> ⚠️ **Note:** These data have been **filtered and enhanced** for educational use. The number of signal events (e.g., Z bosons, J/ψ, ϒ resonances) is **artificially increased** compared to actual collision data to make key physics features more visible and analyzable in a learning setting.  
> They are **not suitable for full physics research** or publication but serve as a reliable foundation for computational analysis and machine learning training.

---

## 📊 Key Objectives

### 1. Calculate Overall Charge for the Event

Only events with an overall charge of 0 are considered (i.e., opposite-sign muon pairs). This reflects the physics of neutral parent particles decaying into muons. In this dataset, all events satisfy this condition.

---

### 2. Classify Events Using Dynamic Mass Windows

Events are labeled into one of **7 classes** based on their invariant mass falling within dynamically calculated mass ranges. Each mass range is defined as the nominal particle mass ± a relative uncertainty, which accounts for physical width and detector resolution effects:

| Label | Particle    | Nominal Mass (GeV) | Typical Relative Uncertainty (%) |
|-------|-------------|--------------------|----------------------------------|
| 0     | J/ψ         | 3.10               | ~3%                              |
| 1     | ψ(2S)       | 3.685              | ~3%                              |
| 2     | ϒ(1S)       | 9.45               | ~2%                              |
| 3     | ϒ(2S)       | 9.94               | ~2%                              |
| 4     | ϒ(3S)       | 10.27              | ~2%                              |
| 5     | Z boson     | 91.19              | ~4%                              |
| 6     | Background  | Elsewhere          | N/A                              |

---

## 📈 Sample Visuals

- Invariant mass plots show clear peaks near known particle masses:  
  - **J/ψ** at ~3.1 GeV  
  - **ϒ(1S)** at ~9.45 GeV  
  - **Z boson** at ~91 GeV  

- Rare particles like **ϒ(2S)** and **ϒ(3S)** are annotated with arrows for clarity.

---

## 🔬 Label Distribution vs. Real Data Expectations

Below is the distribution of labeled particle events in the educational dataset:

| Label      | Particle | Count |
|------------|----------|-------|
| 0          | J/ψ      | 7,198 |
| 1          | ψ(2S)    |   634 |
| 2          | ϒ(1S)    | 3,462 |
| 3          | ϒ(2S)    | 2,412 |
| 4          | ϒ(3S)    | 2,138 |
| 5          | Z boson  | 4,015 |
| 6          | Background | 80,141 |

> Total: 100,000 events

---

### 📉 How This Compares to Actual LHC Data

To understand how the educational dataset has been curated, we compare the observed event counts with expected counts in actual CMS Run 2011A data—assuming 100,000 randomly selected events from a general dimuon dataset.

| Label | Particle | Educational Dataset | Estimated in Real Data (per 100k events) | Difference (×) | Notes |
|-------|----------|---------------------|------------------------------------------|----------------|-------|
| 0     | J/ψ      | 7,198               | ~2,000                                    | 3.6× more      | Common resonance from QCD processes |
| 1     | ψ(2S)    | 634                 | ~200                                      | 3.2× more      | Decays into J/ψ + pions or muons |
| 2     | ϒ(1S)    | 3,462               | ~50                                       | 69× more       | Heavy bottomonium state, rare at 7 TeV |
| 3     | ϒ(2S)    | 2,412               | ~25                                       | 96× more       | Rarer than ϒ(1S) |
| 4     | ϒ(3S)    | 2,138               | ~15                                       | 142× more      | Extremely rare, harder to trigger |
| 5     | Z boson  | 4,015               | ~10–50                                    | 80× more (avg) | Typically requires high-pT trigger |
| 6     | Background | 80,141            | ~97,700                                   | 0.82× less     | Suppressed here to highlight signals |

> 💡 **Educational Total:** 100,000 events  
> 📉 **Realistic Estimate:** Based on published CMS production rates at √s = 7 TeV and typical selection criteria (triggered dimuons with |η| < 2.4 and pT thresholds).

---

### 🎯 Key Takeaways

This dataset was specifically curated for **educational use**, meaning:

- **Signal peaks are amplified** to help students see and analyze real particle signatures without needing millions of events.
- **Event selection is biased** to favor events containing interesting resonances.
- **Background is suppressed** relative to signals, whereas in real analyses it's the opposite.

---

### 🧪 Implication for Analysis

- This enhancement is ideal for **introductory physics analysis, plotting, and ML classification**.
- However, **machine learning results** or cross-section estimates based on this data **cannot be generalized** to real LHC physics.
- The correct interpretation is: *this dataset reflects the physics well enough to learn from it, but not to publish with it*.

---

## 🧠 Insights

**Physics Validation**:  
- Confirms dataset physical correctness by filtering on overall neutral charge.  
- Reveals clear resonance peaks through invariant mass visualization.  
- Demonstrates expected data composition: a large background and distinct resonance signals.  
- Provides foundation for advanced analysis like fitting resonance peaks, optimizing event selection, or machine learning classification.

**Signal vs Background**:  
- Background class captures non-resonant events or experimental noise, useful for anomaly detection or further study.

---

## 🛠️ Technologies Used

- **Python**  
- **Pandas** – for data loading and manipulation  
- **Matplotlib / NumPy** – for visualization and numerical operations  

---

## 🙋‍♂️ Author

**Ayan Gupta**  
Physics + AI enthusiast | High School Student
