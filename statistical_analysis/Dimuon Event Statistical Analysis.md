# 💡 Dimuon Event Computational Analysis - Statistical Analysis

This project analyzes real high-energy physics data from dimuon collision events, focusing on identifying and visualizing the presence of fundamental particles such as **J/ψ**, **ψ(2S)**, **ϒ(nS)** states, and the **Z boson**. These particles decay into muons, and using the muon kinematic data, we classify the originating particles by their invariant mass, taking into account realistic uncertainty ranges around nominal particle masses. Using Python, we label particle signatures dynamically based on mass windows defined by combined physics and detector uncertainties, and visualize their distributions through detailed statistical and graphical analysis. This covers the statistical analysis of the project, giving an insight into the data we are working with.

---

## 📁 Dataset

Dataset is available in CSV format here: https://opendata.cern.ch/record/5201  
The dataset, `Dimuon_DoubleMu.csv`, contains kinematic variables from dimuon decay events in a particle detector. Each row corresponds to a single event and includes:

- Energies: `E1`, `E2`  
- Momentum components: `px1`, `py1`, `pz1`, `px2`, `py2`, `pz2`  
- Charge: `Q1`, `Q2`  

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
| 5     | Z boson     | 91.19              | ~4% (physics + detector combined)|
| 6     | Background  | Elsewhere          | N/A                              |

---

### 3. Visualize Distributions

- **Scatter Plot**: Invariant mass for all events.  
- **Cumulative Plot**: Count of each particle class across the dataset.  
- **Histogram**: Colored distribution of events by class.  
- **Peak Annotation**: Labels and arrows identify significant particle peaks (e.g., ϒ(2S), Z boson).  

---

## 📈 Sample Visuals

- Invariant mass plots show clear peaks near known particle masses:  
  - **J/ψ** at ~3.1 GeV  
  - **ϒ(1S)** at ~9.45 GeV  
  - **Z boson** at ~91 GeV  

- Rare particles like **ϒ(2S)** and **ϒ(3S)** are annotated with arrows for clarity.

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
