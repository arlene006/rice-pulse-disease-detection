<div align="center">

# 🌾 Rice & Pulse Disease Detection System

### AI-Powered Crop Health Analysis using Deep Learning

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.52-FF4B4B.svg)](https://streamlit.io/)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.9-EE4C2C.svg)](https://pytorch.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

[Features](#-features) • [Demo](#-demo) • [Installation](#-installation) • [Usage](#-usage) • [Model](#-model-information) • [Contributing](#-contributing)

</div>

---

## 📋 Overview

An intelligent web application that detects diseases in rice and pulse crops using Convolutional Neural Networks (CNN). Built with Streamlit and PyTorch, this system provides farmers and agricultural professionals with instant disease diagnosis and treatment recommendations.

### 🎯 Key Highlights

- **🔬 AI-Powered Detection**: Deep learning model trained on thousands of crop images
- **📊 High Accuracy**: Achieves 63% accuracy on rice disease classification
- **🚀 Real-time Analysis**: Instant disease prediction with confidence scores
- **💊 Treatment Guidance**: Detailed symptoms and management recommendations
- **🎨 Professional UI**: Modern, gradient-based interface with smooth animations
- **🔐 Secure Authentication**: User login system with encrypted cookies

---

## ✨ Features

### Disease Detection
- **Rice Diseases** (4 classes):
  - 🦠 Bacterial Leaf Blight
  - 🟤 Brown Spot
  - ⚫ Leaf Smut
  - ✅ Healthy Plants

- **Pulse Diseases**: Coming Soon! 🚧

### Application Features
- 📸 Image upload with drag-and-drop support
- 📊 Confidence score visualization with progress bars
- 📈 Probability distribution for all disease classes
- 📚 Comprehensive disease information cards
- 💡 Best practices and tips for image capture
- 🔄 Session state management for smooth UX
- 🎨 Responsive design with gradient backgrounds

---

## 🖼️ Demo

### Login Page
Beautiful authentication interface with Lottie animations

### Disease Detection Interface
Professional gradient-based UI with card layouts

### Results Display
Detailed analysis with confidence metrics and disease information

<img width="1899" height="857" alt="Screenshot 2025-12-12 180847" src="https://github.com/user-attachments/assets/3c4f5aeb-b997-4069-9905-1e55010b2e7e" />


---

## 🚀 Installation

### Prerequisites

- Python 3.11 or higher
- pip package manager
- Virtual environment (recommended)

### Step 1: Clone the Repository

```bash
git clone https://github.com/arlene006/rice-pulse-disease-detection.git
cd rice-pulse-disease-detection
```

### Step 2: Create Virtual Environment

```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Download Model Files

The trained model files are too large for GitHub. Download them from:

**Option 1: Pre-trained Model**
- Download `best_model.pth` from [Google Drive/Dropbox Link]
- Place it in the `models/` directory

**Option 2: Train Your Own**
- See [MODEL_GUIDE.md](docs/MODEL_GUIDE.md) for training instructions

### Step 5: Setup Authentication

Create authentication file:
```bash
cp _secret_auth_template.json _secret_auth_.json
```

The app will create this automatically on first run.

---

## 💻 Usage

### Running the Application

```bash
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`

### Using the App

1. **Login/Register**
   - Create a new account or login with existing credentials
   - Secure authentication with encrypted cookies

2. **Select Crop Type**
   - Choose "Rice" from the sidebar
   - (Pulse detection coming soon)

3. **Upload Image**
   - Click the file uploader
   - Select a clear image of the crop leaf
   - Supported formats: JPG, JPEG, PNG

4. **Analyze**
   - Click "🚀 Analyze Disease" button
   - Wait for AI analysis (takes 1-2 seconds)

5. **View Results**
   - See prediction with confidence score
   - Review disease information
   - Read treatment recommendations

### Tips for Best Results

- ✅ Use well-lit, clear images
- ✅ Focus on the affected leaf area
- ✅ Ensure leaf fills most of the frame
- ❌ Avoid blurry or dark images
- ❌ Don't include multiple leaves

---

## 🏗️ Project Structure

```
rice-disease-detection/
├── app.py                          # Main Streamlit application
├── streamlit_login_auth_ui/        # Authentication UI package
│   ├── __init__.py
│   ├── widgets.py                  # Login widgets
│   └── utils.py                    # Utility functions
├── models/                         # Model files (gitignored)
│   ├── best_model.pth             # Trained CNN model
│   └── training_history.json      # Training metrics
├── data/                           # Dataset (gitignored)
│   ├── rice_leaf_diseases/        # Rice disease images
│   └── pulse_leaf_diseases/       # Pulse disease images
├── docs/                           # Documentation
│   ├── SETUP.md                   # Detailed setup guide
│   └── MODEL_GUIDE.md             # Model training guide
├── .gitignore                      # Git ignore rules
├── requirements.txt                # Python dependencies
├── README.md                       # This file
├── LICENSE                         # MIT License
└── _secret_auth_template.json     # Auth template

```

---

## 🧠 Model Information

### Architecture
- **Type**: Convolutional Neural Network (CNN)
- **Framework**: PyTorch
- **Input Size**: 224x224 RGB images
- **Classes**: 4 (Rice diseases + Healthy)

### Model Details
```python
- Conv Block 1: 3→32→32 channels
- Conv Block 2: 32→64→64 channels  
- Conv Block 3: 64→128→128 channels
- Fully Connected: 512 neurons
- Output: 4 classes
- Dropout: 0.5
```

### Performance
- **Training Accuracy**: ~63%
- **Validation Accuracy**: ~53%
- **Training Epochs**: 30
- **Optimizer**: Adam
- **Loss Function**: Cross Entropy

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat&logo=python&logoColor=white) | Core programming language |
| ![PyTorch](https://img.shields.io/badge/-PyTorch-EE4C2C?style=flat&logo=pytorch&logoColor=white) | Deep learning framework |
| ![Streamlit](https://img.shields.io/badge/-Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white) | Web application framework |
| ![Pillow](https://img.shields.io/badge/-Pillow-3776AB?style=flat) | Image processing |
| ![NumPy](https://img.shields.io/badge/-NumPy-013243?style=flat&logo=numpy&logoColor=white) | Numerical computing |

---

## 📦 Dependencies

Main packages (see `requirements.txt` for complete list):

```
streamlit>=1.52.0
torch>=2.9.0
torchvision>=0.24.0
pillow>=12.0.0
numpy>=2.3.0
streamlit-login-auth-ui
streamlit-lottie
streamlit-option-menu
streamlit-cookies-manager
argon2-cffi
trycourier
```

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit your changes**
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open a Pull Request**

### Areas for Contribution
- 🎯 Improve model accuracy
- 🫘 Add pulse disease detection
- 🌍 Multi-language support
- 📱 Mobile responsiveness
- 📊 Add analytics dashboard
- 🧪 Expand test coverage

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Arlene**
- GitHub: [@arlene006](https://github.com/arlene006)
- LinkedIn: [Connect with me](https://linkedin.com/in/arlene006)

---

## 🙏 Acknowledgments

- Dataset: [Rice Leaf Disease Dataset]
- Inspiration: Agricultural AI research community
- UI Components: Streamlit community packages
- Icons: Emoji and custom designs

---

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/arlene006/rice-pulse-disease-detection/issues) page
2. Create a new issue with detailed description
3. Contact: your.email@example.com

---

## 🗺️ Roadmap

- [x] Rice disease detection
- [x] Professional UI with gradients
- [x] User authentication
- [ ] Pulse disease detection
- [ ] Mobile app version
- [ ] API endpoint for integration
- [ ] Multi-language support
- [ ] Batch image processing
- [ ] Export results to PDF

---

<div align="center">

### ⭐ Star this repository if you find it helpful!

Made with ❤️ for farmers and agricultural professionals

</div>
