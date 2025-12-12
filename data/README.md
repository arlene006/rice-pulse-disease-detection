# Dataset Information

This directory contains the training and validation datasets for rice and pulse disease detection.

## 📁 Directory Structure

```
data/
├── rice_leaf_diseases/
│   ├── Bacterial leaf blight/    (40 images)
│   ├── Brown spot/                (40 images)
│   ├── Leaf smut/                 (40 images)
│   └── _Healthy/                  (40 images)
└── pulse_leaf_diseases/
    └── (Coming soon)
```

---

## 🌾 Rice Leaf Disease Dataset

### Classes (4 total)
1. **Bacterial Leaf Blight** - 40 images
2. **Brown Spot** - 40 images  
3. **Leaf Smut** - 40 images
4. **Healthy** - 40 images

**Total Images**: 160

### Image Specifications
- **Format**: JPG/PNG
- **Size**: Variable (resized to 224x224 during training)
- **Color**: RGB

---

## 🫘 Pulse Leaf Disease Dataset

Coming soon! This section will be updated when pulse disease data is collected.

---

## 📥 Dataset Download

The dataset is excluded from the repository due to size constraints.

**Download Link**: [Add your dataset link here]

After downloading:
1. Extract the zip file
2. Place folders in the `data/` directory
3. Ensure the structure matches the layout above

---

## 📊 Dataset Statistics

### Rice Dataset
- Total samples: 160
- Classes: 4
- Images per class: 40
- Train/Val split: 80/20 (recommended)

---

## 🔍 Data Collection Guidelines

If you're collecting your own data:

1. **Image Quality**
   - Clear, well-lit images
   - Focus on diseased area
   - Avoid blurry photos

2. **Diversity**
   - Different lighting conditions
   - Various disease stages
   - Multiple leaf angles

3. **Labeling**
   - Accurate disease identification
   - Consistent naming convention
   - Verified by experts

---

## ⚠️ Important Notes

- Dataset files are excluded from Git via `.gitignore`
- Large image collections should be hosted externally
- Always verify data quality before training
- Maintain balanced class distribution
