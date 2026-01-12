# Model Files

This directory contains the trained PyTorch model files for disease detection.

## 📥 Download Pre-trained Models

The model files are too large to include in the GitHub repository (~197MB each).

### Rice Disease Model

**File**: `best_model.pth` (197.11 MB)

**Place the downloaded file in this directory**: `models/best_model.pth`

---

## 🧠 Model Information

### Architecture
- **Type**: Convolutional Neural Network (CNN)
- **Framework**: PyTorch
- **Input Size**: 224x224 RGB
- **Classes**: 4 (Bacterial leaf blight, Brown spot, Leaf smut, Healthy)

### Performance Metrics
- Training Accuracy: ~63%
- Validation Accuracy: ~53%
- Training Epochs: 30

### Training History
See `training_history.json` for detailed metrics per epoch.

---

## 🔬 Train Your Own Model

If you want to train your own model:

1. Prepare your dataset in the `data/` directory
2. Follow the instructions in [MODEL_GUIDE.md](../docs/MODEL_GUIDE.md)
3. The trained model will be saved as `best_model.pth`

---

## 📊 Model Files

- `best_model.pth` - Best performing model (gitignored)
- `crop_disease_model.pth` - Alternative model checkpoint (gitignored)
- `training_history.json` - Training metrics and loss curves
- `training_history.png` - Visualization of training progress

---

## ⚠️ Important Notes

- Model files (`.pth`) are excluded from version control via `.gitignore`
- Always download the latest model from the provided link
- Verify model file integrity after download
- Model requires PyTorch 2.9+ to load
