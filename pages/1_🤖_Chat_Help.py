import streamlit as st
import streamlit.components.v1 as components

# Page Config
st.set_page_config(
    page_title="CropAi Support",
    page_icon="🤖",
    layout="wide"
)

# Add CSS for wider sidebar and bigger text
st.markdown("""
<style>
    /* Wider Sidebar */
    [data-testid="stSidebar"] {
        width: 400px !important;
        min-width: 400px !important;
    }
    
    [data-testid="stSidebar"] > div:first-child {
        width: 400px !important;
    }
    
    /* Bigger Sidebar Navigation Text */
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
</style>
""", unsafe_allow_html=True)

st.title("🤖 CropAI Brand Support Agent")

st.markdown("""
<div style="background-color:#e0f2fe; padding:20px; border-radius:10px; margin-bottom:20px;">
    <h4>👋 Need Help?</h4>
    <p>Ask our AI agent about diseases, treatments, or how to use the platform.</p>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------------
# 🔧 DIRECT IFRAME EMBED - SIMPLEST APPROACH
# --------------------------------------------------------
# Using the shareable URL you provided directly
shareable_url = "https://cdn.botpress.cloud/webchat/v3.5/shareable.html?configUrl=https://files.bpcontent.cloud/2025/12/30/15/20251230150047-NMXIQWMA.json"

# Create a simple iframe
st.markdown(f"""
<iframe 
    src="{shareable_url}" 
    style="width: 100%; height: 700px; border: 1px solid #e5e7eb; border-radius: 10px;"
    frameborder="0"
    allow="microphone; camera"
></iframe>
""", unsafe_allow_html=True)
