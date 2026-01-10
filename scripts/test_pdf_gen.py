import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from services.report_generator import ReportGenerator
from services.interfaces import PredictionResult
from PIL import Image

# Mock data
class MockHandler:
    pass

result = PredictionResult(
    predicted_class="Brown spot",
    confidence_score=95.5,
    probabilities={"Brown spot": 95.5, "Healthy": 4.5}
)

disease_info = {
    'description': 'Test Description',
    'symptoms': 'Test Symptoms',
    'treatment': 'Test Treatment',
    'severity': 'Medium'
}

# Create a dummy image
img = Image.new('RGB', (100, 100), color = 'red')

print("Generating PDF...")
try:
    pdf_bytes = ReportGenerator.generate_pdf_report(result, disease_info, "Rice", img)
    with open("test_report.pdf", "wb") as f:
        f.write(pdf_bytes)
    print("PDF generated successfully: test_report.pdf")
    print(f"Size: {len(pdf_bytes)} bytes")
except Exception as e:
    print(f"Error: {e}")
