# 💡 Dimuon Event Computational Analysis - Statistical Analysis

This project analyzes real high-energy physics data from dimuon collision events, focusing on identifying and visualizing the presence of fundamental particles such as **J/ψ**, **ψ(2S)**, **ϒ(nS)** states, and the **Z boson**. These particles decayed into muons, and using the data on the muons, we are able to figure out what particles initially decayed. Using Python, we classify particle signatures, and visualize their distributions through detailed statistical and graphical analysis. This covers the statistical analysis of the project, giving an insight into the data we are working with.

---

## 📁 Dataset

Dataset is available in CSV format here: https://opendata.cern.ch/record/5201  
The dataset, `Dimuon_DoubleMu.csv`, contains kinematic variables from dimuon decay events in a particle detector. Each row corresponds to a single event and includes:

- Energies: `E1`, `E2`  
- Momentum components: `px1`, `py1`, `pz1`, `px2`, `py2`, `pz2`  
- Charge: `Q1`, `Q2`  
- Additional variables (for advanced filtering): `pt1`, `pt2`, `eta1`, `eta2`, `Type1`, `Type2`

---

## 📊 Key Objectives

### 1. Calculate Overall Charge for the Event  
Only events with an overall charge of 0 should be considered. This means the two muons must be of opposite charge. This is because all the initial particles that decayed into muons had an overall charge of 0. In this dataset, there is no event that does not have an overall charge of 0.

---

### 2. Classify Events

Events are labeled into one of **7 classes** based on the calculated invariant mass:

| Label | Particle    | Mass Range (GeV) |
|-------|-------------|------------------|
| 0     | J/ψ         | 3.0 – 3.2        |
| 1     | ψ(2S)       | 3.6 – 3.8        |
| 2     | ϒ(1S)       | 9.3 – 9.6        |
| 3     | ϒ(2S)       | 9.9 – 10.1       |
| 4     | ϒ(3S)       | 10.3 – 10.4      |
| 5     | Z boson     | 88 – 94          |
| 6     | Background  | Elsewhere        |

---

### 3. Visualize Distributions

- **Scatter Plot**: Invariant mass for all events  
- **Cumulative Plot**: Count of each particle class across dataset  
- **Histogram**: Colored distribution of events by class  
- **Peak Annotation**: Labels and arrows identify significant particle peaks (e.g., ϒ(2S), Z boson)

---

## 🔍 Z Boson Event Selection

To more precisely isolate and analyze **Z boson events**, we applied a physics-informed filtering process to ensure cleaner signal reconstruction:

### 🔬 Step-by-Step Selection Criteria

**Muon-Level Requirements (each muon in the pair):**
- Must be a **global muon**: `Type1 == 'G'` and `Type2 == 'G'`
- Transverse momentum **pT > 25 GeV** for both muons
- Pseudorapidity **|η| < 2.4**
- Muons must be of **opposite charge**: `Q1 * Q2 < 0`

**Event-Level Requirements:**
- Invariant mass must be in the Z boson region approximately: **87.5 < M < 95 GeV**
- Trigger matching is approximated by pT cuts (≥25 GeV) and not explicitly applied

This filtering improves background suppression and ensures that the selected Z boson candidates closely resemble the expected detector response for real Z decays.

These selection criteria were based on those determined in CMS Physics Analysis Summary: https://cds.cern.ch/record/2852905/files/LUM-21-001-pas.pdf
In the section: 'Z boson candidate selection and efficiency determination'.

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
- Validates the physical correctness of the dataset via charge filtering
- Reveals clear resonance signatures through invariant mass visualization
- Demonstrates expected data composition: a large background and distinct resonance signals
- Provides a foundation for advanced analysis steps like fitting resonance peaks, optimizing event selection, or training classification models

**Signal vs Background**:
- Background class captures non-resonant events or experimental noise, useful for anomaly detection

---

## 🛠️ Technologies Used

- **Python**
- **Pandas** – for data loading and manipulation  
- **Matplotlib / NumPy** – for visualizations and math operations  

---

## 🙋‍♂️ Author

**Ayan Gupta**  
Physics + AI enthusiast | High School Student
