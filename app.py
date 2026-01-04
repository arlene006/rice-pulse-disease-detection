import streamlit as st
import streamlit.components.v1 as components
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
    
    /* ========== ENHANCED SIDEBAR STYLING ========== */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1e3a8a 0%, #3b82f6 100%);
        padding: 2rem 1rem;
    }
    
    [data-testid="stSidebar"] > div:first-child {
        /* Width handled dynamically */
    }
    
    [data-testid="stSidebar"] * {
        color: white !important;
    }
    
    /* Sidebar Section Headers */
    [data-testid="stSidebar"] h3 {
        color: white !important;
        font-size: 1.1rem !important;
        font-weight: 700 !important;
        margin-top: 1.5rem !important;
        margin-bottom: 1rem !important;
        padding-bottom: 0.5rem;
        border-bottom: 2px solid rgba(255,255,255,0.3);
    }
    
    /* Sidebar Dividers */
    [data-testid="stSidebar"] hr {
        margin: 1.5rem 0 !important;
        border-color: rgba(255,255,255,0.2) !important;
    }
    
    /* Enhanced Selectbox in Sidebar */
    [data-testid="stSidebar"] [data-baseweb="select"] {
        background: rgba(255,255,255,0.15) !important;
        border-radius: 12px !important;
        padding: 0.5rem !important;
        border: 2px solid rgba(255,255,255,0.3) !important;
        transition: all 0.3s ease !important;
    }
    
    [data-testid="stSidebar"] [data-baseweb="select"]:hover {
        background: rgba(255,255,255,0.25) !important;
        border-color: rgba(255,255,255,0.5) !important;
    }
    
    [data-testid="stSidebar"] [data-baseweb="select"] > div {
        font-size: 1.1rem !important;
        font-weight: 600 !important;
        padding: 0.5rem !important;
    }
    
    /* Sidebar Info Boxes */
    [data-testid="stSidebar"] .stAlert {
        background: rgba(255,255,255,0.15) !important;
        border: 2px solid rgba(255,255,255,0.3) !important;
        border-radius: 10px !important;
        padding: 1rem !important;
        margin: 0.5rem 0 !important;
    }
    
    /* Bigger Sidebar Navigation */
    [data-testid="stSidebarNav"] span {
        font-size: 1.5rem !important;
        font-weight: 700 !important;
        padding: 15px 0 !important;
        letter-spacing: 0.5px !important;
    }
    
    [data-testid="stSidebarNav"] svg {
        width: 2.5rem !important;
        height: 2.5rem !important;
        margin-right: 10px !important;
    }
    
    /* ========== LOGIN PAGE CENTERING ========== */
    /* Center the login container */
    [data-testid="stVerticalBlock"] > [style*="flex-direction: column;"] > [data-testid="stVerticalBlock"] {
        max-width: 500px;
        margin: 0 auto;
    }
    
    /* Login form styling */
    .stTextInput > div > div > input {
        border-radius: 10px !important;
        padding: 12px !important;
        font-size: 1rem !important;
    }
    
    /* ========== BUTTON STYLING ========== */
    .stButton > button {
        background: linear-gradient(135deg, #3b82f6 0%, #1e40af 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 12px 24px;
        font-weight: 600;
        box-shadow: 0 4px 6px rgba(59, 130, 246, 0.3);
        transition: all 0.3s ease;
        width: 100%;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(59, 130, 246, 0.4);
    }
    
    /* ========== FILE UPLOADER ENHANCEMENT ========== */
    [data-testid="stFileUploader"] {
        background: white;
        border-radius: 15px;
        padding: 30px;
        border: 3px dashed #3b82f6;
        transition: all 0.3s ease;
    }
    
    [data-testid="stFileUploader"]:hover {
        border-color: #1e40af;
        background: #f0f9ff;
    }
    
    [data-testid="stFileUploader"] section {
        border: none !important;
    }
    
    [data-testid="stFileUploader"] button {
        background: linear-gradient(135deg, #3b82f6 0%, #1e40af 100%) !important;
        color: white !important;
        border-radius: 10px !important;
        padding: 12px 24px !important;
        font-weight: 600 !important;
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
    
    /* ========== ENHANCED CUSTOM CARDS ========== */
    .custom-card {
        background: white;
        border-radius: 15px;
        padding: 30px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.08);
        margin: 15px 0;
        border-left: 5px solid #3b82f6;
        transition: all 0.3s ease;
    }
    
    .custom-card:hover {
        box-shadow: 0 15px 35px rgba(0,0,0,0.12);
        transform: translateY(-2px);
    }
    
    .custom-card h3 {
        margin-top: 0;
        margin-bottom: 1rem;
    }
    
    .custom-card ul {
        margin: 0;
        padding-left: 1.5rem;
    }
    
    .custom-card li {
        margin: 0.5rem 0;
        line-height: 1.6;
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

# Logic for displaying results using handler data
def display_prediction_results(result, handler):
    """Display prediction results in a professional format"""
    info = handler.get_disease_info(result.predicted_class)
    
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
        display_name = "Healthy Plant" if result.predicted_class == "_Healthy" else result.predicted_class
        st.metric("🎯 Prediction", display_name)
    
    with col2:
        st.metric("📊 Confidence", f"{result.confidence_score:.1f}%")
    
    with col3:
        severity = info.get('severity', 'Unknown')
        st.metric("⚠️ Severity", severity)
    
    # Confidence Progress Bar
    st.markdown("### Confidence Level")
    st.progress(result.confidence_score / 100)
    
    # All Probabilities
    with st.expander("📈 View All Disease Probabilities", expanded=False):
        for class_name, prob in sorted(result.probabilities.items(), key=lambda x: x[1], reverse=True):
            display_name = "Healthy" if class_name == "_Healthy" else class_name
            col_a, col_b = st.columns([3, 1])
            with col_a:
                st.write(f"**{display_name}**")
            with col_b:
                st.write(f"{prob:.2f}%")
            st.progress(prob / 100)

def display_disease_info(predicted_class, handler):
    """Display detailed disease information"""
    info = handler.get_disease_info(predicted_class)
    
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
    
    # Initialize session state (Keep for UI states)
    init_session_state()
    
    # DEPENDENCY INJECTION: Get Container
    # The App doesn't know HOW to create Auth or Handlers, it just asks the container.
    from services.container import DependencyContainer
    container = DependencyContainer.get_instance()
    
    # Auth Service Usage
    auth = container.auth_service
    is_logged_in = auth.login()
    
    if is_logged_in:
        username = auth.get_username()
        
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
            st.markdown("") # Spacing
            
            crop_type = st.selectbox(
                "🌾 Select Crop Type",
                ["🌾 Rice", "🫘 Pulse"],
                help="Choose the type of crop for disease detection"
            )
            
            st.markdown("---")
            st.markdown("### 📊 Model Status")
            
            # Show status for BOTH crops
            if crop_type == "🌾 Rice":
                st.success("✅ Rice Model: Ready")
                st.info("⏸️ Pulse Model: Standby")
            else:
                st.info("⏸️ Rice Model: Standby")
                st.success("✅ Pulse Model: Ready")
            
            st.markdown("---")
            st.markdown("### ℹ️ Quick Info")
            st.markdown("""
            <div style='font-size: 0.9rem; line-height: 1.6;'>
            Upload a clear image of the affected leaf for accurate AI-powered disease detection.
            </div>
            """, unsafe_allow_html=True)
            
            # Chatbot Section
            st.markdown("---")
            # Sidebar Settings
            st.markdown("---")
            with st.expander("⚙️ Sidebar & Chat Settings", expanded=False):
                # Width Control
                sidebar_width = st.slider(
                    "Sidebar Width (px)",
                    min_value=300,
                    max_value=1200,
                    value=450,
                    step=10,
                    key="sidebar_width_slider",
                    help="Adjust the width of the sidebar"
                )
                
                # Height Control for Chatbot
                chat_height = st.slider(
                    "Chatbot Height (px)",
                    min_value=400,
                    max_value=1000,
                    value=600,
                    step=50,
                    key="chat_height_slider",
                    help="Adjust the height of the chatbot window"
                )
                
                # Apply sidebar width dynamically with more specific selectors
                st.markdown(f"""
                <style>
                section[data-testid="stSidebar"] {{
                    width: {sidebar_width}px !important;
                    min-width: {sidebar_width}px !important;
                    max-width: {sidebar_width}px !important;
                }}
                
                section[data-testid="stSidebar"] > div {{
                    width: {sidebar_width}px !important;
                }}
                
                /* Ensure content fits */
                [data-testid="stSidebarNav"] {{
                    width: {sidebar_width}px !important;
                }}
                </style>
                """, unsafe_allow_html=True)

            # Chatbot Section (Moved after settings to use variables)
            # We move this visually via logic, but if we want it above, we need to declare variables first.
            # However, for simplicity let's stick to the order. But wait, if I define vars here, I can't use them above.
            # I should move the chatbot section BELOW settings or define the variables earlier using Session State.
            # Let's use Session State to persist the default values and keep chatbot above if preferred, 
            # OR just render the chatbot here with the new height.
            
            # Actually, user wants chatbot to be bigger.
            # Let's re-render the chatbot with the dynamic height. 
            # I will replace the PREVIOUS chatbot block with correct logic.
            
            # Since I am replacing lines 429-452 (Settings), I need to handle the chatbot block which was lines 419-428.
            # I will combine them.
            
            st.markdown("---")
            with st.expander("💬 Ask CropAI Assistant", expanded=True):
                # Reverting to reliable Iframe method for submission stability
                # Note: Chat history is stored in browser local storage. 
                # Different users on different machines will see separate histories.
                st.markdown(f"""
                <iframe 
                    src="https://cdn.botpress.cloud/webchat/v3.5/shareable.html?configUrl=https://files.bpcontent.cloud/2025/12/30/15/20251230150047-NMXIQWMA.json" 
                    style="width: 100%; height: {chat_height}px; border: none; border-radius: 8px;"
                    frameborder="0"
                    allow="microphone; camera"
                ></iframe>
                """, unsafe_allow_html=True)

        
        
        # Main Content
        # Use Container to get the correct handler (Factory Pattern)
        handler = container.get_handler(crop_type)
        
        if handler:
            # Polymorphism: We treat all handlers the same way
            if crop_type == "🌾 Rice":
                st.markdown("## 🌾 Rice Disease Detection")
                st.markdown("Upload a clear image of a rice leaf to detect potential diseases using AI.")
            else:
                st.markdown("## 🫘 Pulse Disease Detection")
        
            # Load model via handler
            success, error = handler.load_model()
            
            if success:
                st.success(f"🎯 {len(handler.classes) if hasattr(handler, 'classes') else 0} Diseases Support")
                
                # File uploader
                uploaded_file = st.file_uploader(
                    "📁 Choose a leaf image",
                    type=["jpg", "jpeg", "png"],
                    help="Upload a clear, well-lit image"
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
                                # LSP Correction: Handle PredictionResult object
                                result = handler.predict(image)
                                
                                if result is not None:
                                    st.session_state.prediction_made = True
                                    st.session_state.current_prediction = result
                                    st.success("✅ Analysis Complete!")
                    
                    # Display results if prediction was made
                    if st.session_state.prediction_made and st.session_state.current_prediction:
                        result = st.session_state.current_prediction
                        # Passing result object instead of unpacked values
                        display_prediction_results(result, handler)
                        display_disease_info(result.predicted_class, handler)
                        
                else:
                    # Tips section
                    st.markdown("---")
                    st.markdown("## 📋 Getting Started")
                    
                    col_tip1, col_tip2 = st.columns([1, 1], gap="large")
                    
                    with col_tip1:
                        st.markdown("""
                        <div class="custom-card">
                            <h3>💡 Tips for Best Results</h3>
                            <ul>
                                <li style='color: #4b5563; font-size: 1rem;'>📷 Use clear, well-lit images</li>
                                <li style='color: #4b5563; font-size: 1rem;'>🎯 Focus on the affected leaf area</li>
                                <li style='color: #4b5563; font-size: 1rem;'>❌ Avoid blurry or dark images</li>
                                <li style='color: #4b5563; font-size: 1rem;'>🔍 Ensure the leaf fills most of the frame</li>
                                <li style='color: #4b5563; font-size: 1rem;'>🌿 Capture multiple angles if possible</li>
                            </ul>
                        </div>
                        """, unsafe_allow_html=True)
                    
                    with col_tip2:
                        st.markdown("""
                        <div class="custom-card">
                            <h3>🎯 System Status</h3>
                            <ul>
                                <li style='color: #10b981; font-size: 1rem;'>✅ AI Model Loaded</li>
                                <li style='color: #10b981; font-size: 1rem;'>✅ Secure Login Active</li>
                                <li style='color: #10b981; font-size: 1rem;'>✅ Database Connected</li>
                                <li style='color: #10b981; font-size: 1rem;'>✅ Ready for Analysis</li>
                            </ul>
                        </div>
                        """, unsafe_allow_html=True)
            else:
                 # Handler exists but failed to load model
                 st.error(f"❌ Failed to load model: {error}")

        # Footer
        st.markdown("""
        <div class="footer">
            <p>Built with ❤️ using Streamlit & PyTorch | Disease Detection System v3.0</p>
            <p style='font-size: 0.8rem; color: #94a3b8;'>© 2024 Agricultural AI Solutions</p>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
