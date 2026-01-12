"""
Convenience script to run the Crop Disease Detector application.

Usage:
    python run.py
"""
import subprocess
import sys
import os

def main():
    """Run the Streamlit application."""
    app_path = os.path.join("crop_disease_detector", "app.py")
    
    if not os.path.exists(app_path):
        print(f"Error: Could not find {app_path}")
        sys.exit(1)
    
    print("Starting Crop Disease Detector...")
    print(f"Running: streamlit run {app_path}")
    print("-" * 50)
    
    subprocess.run([sys.executable, "-m", "streamlit", "run", app_path])

if __name__ == "__main__":
    main()
