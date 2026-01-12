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
- **📄 PDF Reports**: Download comprehensive analysis reports for record-keeping
- **🤖 AI Assistant**: Integrated chatbot for instant help and guidance
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

- **Pulse Diseases** (5 classes):
  - 🍂 Angular Leaf Spot
  - 🦠 Bacterial Pathogen
  - 🔴 Cercospora Leaf Spot
  - ⚠️ Potassium Deficiency
  - ✅ No Disease (Healthy)

### Application Features
- 📸 Image upload with drag-and-drop support
- 📊 Confidence score visualization with progress bars
- 📈 Probability distribution for all disease classes
- 📚 Comprehensive disease information cards
- 📄 **PDF Report Generation**: Download detailed analysis reports
- 🤖 **AI Chatbot**: Get instant help via integrated Botpress assistant
- 💡 Best practices and tips for image capture
- 🔄 Session state management for smooth UX
- 🎨 Responsive design with gradient backgrounds

---

## 🖼️ Demo

### Login Page
Beautiful authentication interface with Lottie animations

### Disease Detection Interface
Professional gradient-based UI with card layouts. Supports switching between **Rice** and **Pulse** crops.

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
- Download `best_model.pth` and `pulse_disease_model.pth`
- Place them in the `models/` directory

**Option 2: Train Your Own**
- See training scripts: `train_pulse.py` (and similar for rice)

### Step 5: Setup Authentication

Create authentication file:
```bash
cp _secret_auth_template.json _secret_auth_.json
```

The app will create this automatically on first run.

---

## 💻 Usage

### Running the Application

**Option 1: Using the convenience script**
```bash
python run.py
```

**Option 2: Direct streamlit command**
```bash
streamlit run crop_disease_detector/app.py
```

**Option 3: After installation (pip install -e .)**
```bash
crop-disease-detector
```

The application will open in your browser at `http://localhost:8501`

### Using the App

1. **Login/Register**
   - Create a new account or login with existing credentials
   - Secure authentication with encrypted cookies

2. **Select Crop Type**
   - Choose "Rice" or "Pulse" from the sidebar
   - Switch instantly between different crop models

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
   - **Download PDF report** for your records

6. **Get Help**
   - Use the AI chatbot in the sidebar for instant assistance
   - Navigate to the Chat Help page for full-screen chatbot
   - Ask about diseases, treatments, or platform usage

### Tips for Best Results

- ✅ Use well-lit, clear images
- ✅ Focus on the affected leaf area
- ✅ Ensure leaf fills most of the frame
- ❌ Avoid blurry or dark images
- ❌ Don't include multiple leaves

---

## 🏗️ Project Structure

```
rice-pulse-disease-detection/
├── crop_disease_detector/          # Main application package
│   ├── __init__.py
│   ├── app.py                      # Main Streamlit application
│   ├── services/                   # Business Logic & Core Services
│   │   ├── __init__.py
│   │   ├── auth_service.py         # User Authentication Logic
│   │   ├── container.py            # Dependency Injection Container
│   │   ├── disease_data.py         # Disease Information Database
│   │   ├── disease_handlers.py     # AI Logic & Prediction Handlers
│   │   ├── interfaces.py           # Interface Contracts (SOLID)
│   │   └── report_generator.py     # PDF Report Generation
│   ├── models/                     # Model Storage
│   │   ├── __init__.py
│   │   ├── architecture.py         # CNN Architecture Definition
│   │   ├── best_model.pth          # Rice Model Weights
│   │   └── pulse_disease_model.pth # Pulse Model Weights
│   └── pages/                      # Multi-page app pages
│       └── 1_🤖_Chat_Help.py       # Chatbot Page
├── tests/                          # Automated Test Suite
│   ├── test_container.py
│   └── test_solid_compliance.py
├── docs/                           # Documentation
│   ├── SOLID_PRINCIPLES.md         # Architecture Analysis
│   └── PROJECT_DOCUMENTATION.md    # Full Technical Guide
├── scripts/                        # Utility Scripts
│   ├── train_pulse.py              # Training Script for Pulse Model
│   └── test_pdf_gen.py             # PDF Generation Test
├── data/                           # Training Data
├── streamlit_login_auth_ui/        # Auth UI Components (Vendored)
├── run.py                          # Convenience runner script
├── setup.py                        # Package configuration
├── requirements.txt                # Dependencies
├── LICENSE                         # MIT License
└── README.md                       # This file

```

---

## 🛡️ Enterprise Architecture

This project has been professionally re-engineered to follow **SOLID Principles** and **Enterprise Design Patterns**, making it robust, testable, and maintainable.

### Core Principles Applied:
1.  **Dependency Injection**: Controlled by `services/container.py`. The app never manually creates service instances.
2.  **Layered Architecture**: Strict separation between UI (`app.py`), Business Logic (`services/`), and Data (`data/`).
3.  **Interfaces**: Defined in `services/interfaces.py`. The app relies on contracts, not implementation details.

For a detailed technical breakdown for mentors and evaluators, please see **[PROJECT_DOCUMENTATION.md](docs/PROJECT_DOCUMENTATION.md)**.

---

## 🧠 Model Information

### Architecture
- **Type**: Convolutional Neural Network (CNN)
- **Framework**: PyTorch
- **Input Size**: 224x224 RGB images
- **Classes**: 4 (Rice), 5 (Pulse)

### Model Details
```python
- Conv Block 1: 3→32→32 channels
- Conv Block 2: 32→64→64 channels  
- Conv Block 3: 64→128→128 channels
- Fully Connected: 512 neurons
- Output: N classes (Dynamic)
- Dropout: 0.5
```

### Performance

#### Rice Model
- **Training Accuracy**: ~63%
- **Validation Accuracy**: ~53%

#### Pulse Model
- **Training Accuracy**: ~97%
- **Validation Accuracy**: ~96% (Excellent Performance)

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
- [x] Pulse disease detection
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
