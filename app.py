import streamlit as st
from streamlit_login_auth_ui.widgets import __login__
import torch
import torch.nn as nn
from torchvision import transforms
from PIL import Image
import numpy as np

# Page Configuration
st.set_page_config(
    page_title="Disease Detection System",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Professional Look
def load_custom_css():
    st.markdown("""
    <style>
    /* Main Background */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    /* Header Styling */
    h1 {
        color: #1e3a8a;
        font-weight: 700;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    h2, h3 {
        color: #2563eb;
    }
    
    /* Card Containers */
    .css-1r6slb0 {
        background: white;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1e3a8a 0%, #3b82f6 100%);
    }
    
    [data-testid="stSidebar"] * {
        color: white !important;
    }
    
    /* Button Styling */
    .stButton > button {
        background: linear-gradient(135deg, #3b82f6 0%, #1e40af 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 12px 24px;
        font-weight: 600;
        box-shadow: 0 4px 6px rgba(59, 130, 246, 0.3);
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(59, 130, 246, 0.4);
    }
    
    /* File Uploader */
    [data-testid="stFileUploader"] {
        background: white;
        border-radius: 10px;
        padding: 20px;
        border: 2px dashed #3b82f6;
    }
    
    /* Info Boxes */
    .stAlert {
        border-radius: 10px;
        border-left: 5px solid;
    }
    
    /* Progress Bar */
    .stProgress > div > div {
        background: linear-gradient(90deg, #10b981 0%, #3b82f6 100%);
    }
    
    /* Metrics */
    [data-testid="stMetricValue"] {
        font-size: 2rem;
        font-weight: 700;
        color: #1e3a8a;
    }
    
    /* Custom Card */
    .custom-card {
        background: white;
        border-radius: 15px;
        padding: 25px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        margin: 10px 0;
        border-left: 5px solid #3b82f6;
    }
    
    /* Result Card */
    .result-card {
        background: linear-gradient(135deg, #ffffff 0%, #f0f9ff 100%);
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 8px 16px rgba(0,0,0,0.1);
        margin: 15px 0;
    }
    
    /* Disease Info Card */
    .disease-card {
        background: white;
        border-radius: 12px;
        padding: 20px;
        margin: 10px 0;
        box-shadow: 0 4px 8px rgba(0,0,0,0.08);
        border-top: 4px solid #3b82f6;
    }
    
    /* Welcome Banner */
    .welcome-banner {
        background: linear-gradient(135deg, #3b82f6 0%, #1e40af 100%);
        color: white;
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 30px;
        box-shadow: 0 10px 30px rgba(59, 130, 246, 0.3);
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 20px;
        color: #64748b;
        margin-top: 50px;
    }
    
    /* Image Container */
    .image-container {
        border-radius: 15px;
        overflow: hidden;
        box-shadow: 0 8px 16px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize session state
def init_session_state():
    """Initialize all session states to prevent errors"""
    if 'prediction_made' not in st.session_state:
        st.session_state.prediction_made = False
    if 'current_prediction' not in st.session_state:
        st.session_state.current_prediction = None
    if 'uploaded_image' not in st.session_state:
        st.session_state.uploaded_image = None

# Disease Classes
RICE_CLASSES = ['Bacterial leaf blight', 'Brown spot', 'Leaf smut', '_Healthy']
PULSE_CLASSES = []  # To be added when pulse model is trained

# Disease Information with enhanced details
DISEASE_INFO = {
    'Bacterial leaf blight': {
        'description': 'A bacterial disease that causes wilting of seedlings and yellowing and drying of leaves.',
        'symptoms': 'Water-soaked lesions on leaves, yellowing, wilting',
        'treatment': 'Use resistant varieties, apply copper-based bactericides, maintain proper water management',
        'severity': 'High',
        'icon': '🦠'
    },
    'Brown spot': {
        'description': 'A fungal disease causing brown spots on leaves, reducing photosynthesis.',
        'symptoms': 'Circular brown spots with gray centers on leaves',
        'treatment': 'Use disease-free seeds, apply fungicides, ensure balanced fertilization',
        'severity': 'Medium',
        'icon': '🟤'
    },
    'Leaf smut': {
        'description': 'A fungal disease that produces black powdery masses on leaves.',
        'symptoms': 'Black angular spots on leaves, reduced grain quality',
        'treatment': 'Use resistant varieties, remove infected plants, apply appropriate fungicides',
        'severity': 'Medium',
        'icon': '⚫'
    },
    '_Healthy': {
        'description': 'The plant appears healthy with no visible disease symptoms.',
        'symptoms': 'Green, vibrant leaves with no spots or discoloration',
        'treatment': 'Continue regular care and monitoring',
        'severity': 'None',
        'icon': '✅'
    }
}

# Define CNN Model Architecture
class CNNModel(nn.Module):
    def __init__(self, num_classes):
        super(CNNModel, self).__init__()
        self.conv1_1 = nn.Conv2d(3, 32, kernel_size=3, padding=1)
        self.conv1_2 = nn.Conv2d(32, 32, kernel_size=3, padding=1)
        self.conv2_1 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        self.conv2_2 = nn.Conv2d(64, 64, kernel_size=3, padding=1)
        self.conv3_1 = nn.Conv2d(64, 128, kernel_size=3, padding=1)
        self.conv3_2 = nn.Conv2d(128, 128, kernel_size=3, padding=1)
        self.pool = nn.MaxPool2d(2, 2)
        self.fc1 = nn.Linear(128 * 28 * 28, 512)
        self.fc2 = nn.Linear(512, num_classes)
        self.dropout = nn.Dropout(0.5)
        self.relu = nn.ReLU()
        
    def forward(self, x):
        x = self.relu(self.conv1_1(x))
        x = self.relu(self.conv1_2(x))
        x = self.pool(x)
        x = self.relu(self.conv2_1(x))
        x = self.relu(self.conv2_2(x))
        x = self.pool(x)
        x = self.relu(self.conv3_1(x))
        x = self.relu(self.conv3_2(x))
        x = self.pool(x)
        x = x.view(-1, 128 * 28 * 28)
        x = self.relu(self.fc1(x))
        x = self.dropout(x)
        x = self.fc2(x)
        return x

def preprocess_image(image):
    """Preprocess the uploaded image for model prediction"""
    try:
        transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        ])
        return transform(image).unsqueeze(0)
    except Exception as e:
        st.error(f"Error preprocessing image: {str(e)}")
        return None

@st.cache_resource
def load_rice_model():
    """Load the trained rice disease model"""
    try:
        model = CNNModel(num_classes=len(RICE_CLASSES))
        model.load_state_dict(torch.load('models/best_model.pth', map_location=torch.device('cpu')))
        model.eval()
        return model, None
    except Exception as e:
        return None, str(e)

def predict_disease(image, model, classes):
    """Predict disease from image"""
    try:
        img_tensor = preprocess_image(image)
        if img_tensor is None:
            return None, None, None
            
        with torch.no_grad():
            outputs = model(img_tensor)
            probabilities = torch.nn.functional.softmax(outputs, dim=1)
            confidence, predicted = torch.max(probabilities, 1)
            
        predicted_class = classes[predicted.item()]
        confidence_score = confidence.item() * 100
        all_probs = {classes[i]: probabilities[0][i].item() * 100 for i in range(len(classes))}
        
        return predicted_class, confidence_score, all_probs
    except Exception as e:
        st.error(f"Error during prediction: {str(e)}")
        return None, None, None

def display_prediction_results(predicted_class, confidence, all_probs):
    """Display prediction results in a professional format"""
    info = DISEASE_INFO.get(predicted_class, {})
    
    # Result Header
    st.markdown(f"""
    <div class="result-card">
        <h2 style='text-align: center; margin-bottom: 20px;'>
            {info.get('icon', '🔬')} Analysis Complete
        </h2>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        display_name = "Healthy Plant" if predicted_class == "_Healthy" else predicted_class
        st.metric("🎯 Prediction", display_name)
    
    with col2:
        st.metric("📊 Confidence", f"{confidence:.1f}%")
    
    with col3:
        severity = info.get('severity', 'Unknown')
        st.metric("⚠️ Severity", severity)
    
    # Confidence Progress Bar
    st.markdown("### Confidence Level")
    st.progress(confidence / 100)
    
    # All Probabilities
    with st.expander("📈 View All Disease Probabilities", expanded=False):
        for class_name, prob in sorted(all_probs.items(), key=lambda x: x[1], reverse=True):
            display_name = "Healthy" if class_name == "_Healthy" else class_name
            col_a, col_b = st.columns([3, 1])
            with col_a:
                st.write(f"**{display_name}**")
            with col_b:
                st.write(f"{prob:.2f}%")
            st.progress(prob / 100)

def display_disease_info(predicted_class):
    """Display detailed disease information"""
    info = DISEASE_INFO.get(predicted_class, {})
    
    st.markdown("---")
    st.markdown("## 📚 Disease Information")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
        <div class="disease-card">
            <h3>📖 Description</h3>
            <p>{info.get('description', 'N/A')}</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        <div class="disease-card">
            <h3>🔍 Symptoms</h3>
            <p>{info.get('symptoms', 'N/A')}</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="disease-card">
            <h3>💊 Treatment & Management</h3>
            <p>{info.get('treatment', 'N/A')}</p>
        </div>
        """, unsafe_allow_html=True)

# Main Application
def main():
    # Load custom CSS
    load_custom_css()
    
    # Initialize session state
    init_session_state()
    
    # Login Configuration
    try:
        __login__obj = __login__(
            auth_token="courier_auth_token",
            company_name="Shims",
            width=200,
            height=250,
            logout_button_name='Logout',
            hide_menu_bool=False,
            hide_footer_bool=False,
            lottie_url='https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json'
        )
        
        LOGGED_IN = __login__obj.build_login_ui()
        username = __login__obj.get_username()
    except Exception as e:
        st.error(f"Login error: {str(e)}")
        return
    
    if LOGGED_IN:
        # Welcome Banner
        st.markdown(f"""
        <div class="welcome-banner">
            <h1>🌾 Agricultural Disease Detection System</h1>
            <p style='font-size: 1.2rem; margin-top: 10px;'>Welcome back, <strong>{username}</strong>!</p>
            <p style='font-size: 0.9rem; opacity: 0.9;'>AI-Powered Crop Health Analysis</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Sidebar
        with st.sidebar:
            st.markdown("### 🔍 Detection Settings")
            crop_type = st.selectbox(
                "Select Crop Type",
                ["🌾 Rice", "🫘 Pulse (Coming Soon)"],
                help="Choose the type of crop for disease detection"
            )
            
            st.markdown("---")
            st.markdown("### 📊 Quick Stats")
            st.info("✅ Model Loaded")
            st.success(f"🎯 {len(RICE_CLASSES)} Rice Diseases")
        
        # Main Content
        if crop_type == "🌾 Rice":
            st.markdown("## 🌾 Rice Disease Detection")
            st.markdown("Upload a clear image of a rice leaf to detect potential diseases using AI.")
            
            # Load model
            model, error = load_rice_model()
            
            if model is not None:
                # File uploader
                uploaded_file = st.file_uploader(
                    "📁 Choose a rice leaf image",
                    type=["jpg", "jpeg", "png"],
                    help="Upload a clear, well-lit image of a rice leaf"
                )
                
                if uploaded_file is not None:
                    col1, col2 = st.columns([1, 1])
                    
                    with col1:
                        st.markdown("### 📸 Uploaded Image")
                        try:
                            image = Image.open(uploaded_file).convert('RGB')
                            st.image(image, use_container_width=True, caption="Your uploaded image")
                        except Exception as e:
                            st.error(f"Error loading image: {str(e)}")
                            return
                    
                    with col2:
                        st.markdown("### 🔬 Analysis")
                        if st.button("🚀 Analyze Disease", type="primary", use_container_width=True):
                            with st.spinner("🔄 Analyzing image... Please wait"):
                                predicted_class, confidence, all_probs = predict_disease(image, model, RICE_CLASSES)
                                
                                if predicted_class is not None:
                                    st.session_state.prediction_made = True
                                    st.session_state.current_prediction = {
                                        'class': predicted_class,
                                        'confidence': confidence,
                                        'probs': all_probs
                                    }
                                    st.success("✅ Analysis Complete!")
                    
                    # Display results if prediction was made
                    if st.session_state.prediction_made and st.session_state.current_prediction:
                        pred = st.session_state.current_prediction
                        display_prediction_results(pred['class'], pred['confidence'], pred['probs'])
                        display_disease_info(pred['class'])
                        
                else:
                    # Tips section
                    st.markdown("---")
                    col_tip1, col_tip2 = st.columns(2)
                    
                    with col_tip1:
                        st.markdown("""
                        <div class="custom-card">
                            <h3>💡 Tips for Best Results</h3>
                            <ul>
                                <li>Use clear, well-lit images</li>
                                <li>Focus on the affected leaf area</li>
                                <li>Avoid blurry or dark images</li>
                                <li>Ensure the leaf fills most of the frame</li>
                            </ul>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    with col_tip2:
                        st.markdown("""
                        <div class="custom-card">
                            <h3>🎯 Detectable Diseases</h3>
                            <ul>
                                <li>🦠 Bacterial Leaf Blight</li>
                                <li>🟤 Brown Spot</li>
                                <li>⚫ Leaf Smut</li>
                                <li>✅ Healthy Plants</li>
                            </ul>
                        </div>
                        """, unsafe_allow_html=True)
            else:
                st.error(f"❌ Failed to load model: {error}")
                st.info("Please ensure the model file exists at: `models/best_model.pth`")
        
        else:  # Pulse
            st.markdown("## 🫘 Pulse Disease Detection")
            st.info("🚧 Pulse disease detection model is currently under development.")
            
            st.markdown("""
            <div class="custom-card">
                <h3>🔜 Coming Soon Features:</h3>
                <ul>
                    <li>Pulse leaf disease detection</li>
                    <li>Multiple pulse varieties support</li>
                    <li>Enhanced disease classification</li>
                    <li>Treatment recommendations</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)
        
        # Footer
        st.markdown("""
        <div class="footer">
            <p>Built with ❤️ using Streamlit & PyTorch | Disease Detection System v2.0</p>
            <p style='font-size: 0.8rem; color: #94a3b8;'>© 2024 Agricultural AI Solutions</p>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
