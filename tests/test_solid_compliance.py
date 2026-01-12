
import pytest
from crop_disease_detector.services.interfaces import IDiseasePredictor, IDiseaseInfoProvider, PredictionResult
from crop_disease_detector.services.disease_handlers import RiceDiseaseHandler, PulseDiseaseHandler

def test_handlers_implement_interfaces():
    """Verify that handlers implement the required ISP interfaces."""
    rice_handler = RiceDiseaseHandler()
    pulse_handler = PulseDiseaseHandler()
    
    assert isinstance(rice_handler, IDiseasePredictor)
    assert isinstance(rice_handler, IDiseaseInfoProvider)
    
    assert isinstance(pulse_handler, IDiseasePredictor)
    assert isinstance(pulse_handler, IDiseaseInfoProvider)

def test_lsp_compliance_rice_handler():
    """Verify Rice handler returns standardized PredictionResult or None."""
    handler = RiceDiseaseHandler()
    
    # Test with dummy image (None) -> Should return None safely
    result = handler.predict(None)
    assert result is None or isinstance(result, PredictionResult)

def test_lsp_compliance_pulse_handler():
    """
    Verify Pulse handler (placeholder) returns standardized type (None)
    instead of crashing or returning odd tuples.
    """
    handler = PulseDiseaseHandler()
    result = handler.predict(None)
    
    # LSP: Must be None or PredictionResult. 
    # Pulse handler explicitly returns None, which matches Optional[PredictionResult]
    assert result is None

def test_interface_segregation_info_only():
    """
    Verify we can use the Info Provider interface without loading the model.
    This demonstrates ISP.
    """
    handler = RiceDiseaseHandler()
    
    # We should be able to get info WITHOUT calling load_model()
    info = handler.get_disease_info("Bacterial leaf blight")
    assert info['severity'] == "High"
