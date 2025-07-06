# ImprovedBosonClassifier: Multiclass Boson Detection with Threshold Calibration

This project implements a deep learning model in PyTorch for classifying high-energy physics collision events into seven classes, with a focus on accurately detecting Z bosons. The model uses threshold-based decision calibration to improve precision-recall trade-offs, especially for underrepresented signal classes.

## Classes

The model classifies each event into one of the following categories:
- J/ψ
- ψ(2S)
- ϒ(1S)
- ϒ(2S)
- ϒ(3S)
- Z boson
- Background

## Key Features

- Fully-connected neural network built with PyTorch
- Class imbalance addressed using `compute_class_weight` from scikit-learn
- Custom thresholding applied per class to balance false positives and false negatives
- Second training loop using thresholded predictions
- Performance evaluation via:
  - Accuracy
  - Confusion Matrix
  - Precision, Recall, F1-score
  - Multiclass ROC-AUC

## Performance Summary

### Before Threshold Calibration
- **Accuracy:** 61%
- **Multiclass ROC-AUC:** 0.9339

### After Threshold Calibration
- **Accuracy:** 72%
- **Multiclass ROC-AUC:** 0.9340

| Class        | Precision | Recall | F1 Score | Support | FP Level         | FN Level           | Notes                                                  |
|--------------|-----------|--------|----------|---------|------------------|--------------------|--------------------------------------------------------|
| J/ψ          | 0.29      | 0.82   | 0.43     | 1208    | High             | Low                | Overpredicted but high recall                          |
| ψ(2S)        | 0.03      | 0.06   | 0.04     | 117     | Very High        | Very High          | Poor separation; many misclassifications               |
| ϒ(1S)        | 0.40      | 0.87   | 0.55     | 749     | Moderate         | Low                | High recall but some confusion with other classes      |
| ϒ(2S)        | 0.35      | 0.74   | 0.48     | 370     | Moderate         | Moderate           | Balanced performance                                   |
| ϒ(3S)        | 0.04      | 0.08   | 0.05     | 157     | Very High        | Very High          | Weak representation and overlap with other classes     |
| Z boson      | 0.55      | 1.00   | 0.71     | 796     | Moderate         | None               | Perfect recall; all real Z bosons detected             |
| Background   | 0.97      | 0.71   | 0.82     | 16603   | Low              | High               | Some signal leakage into background                    |

## Analysis

Even after threshold calibration, the accuracy plateaued at around 72%, suggesting the model has reached its capacity under the current architecture and data distribution. Precision for rare classes like ψ(2S) and ϒ(3S) remains low, primarily due to:
- Severe class imbalance
- Overlapping feature distributions

Despite this, **Z boson detection achieved 100% recall**, which is critical for this project's goal. False positives for Z bosons are acceptable, as post-selection can eliminate incorrect predictions, but **false negatives are not**, and the model successfully avoids them.


