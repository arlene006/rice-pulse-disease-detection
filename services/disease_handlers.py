from abc import ABC, abstractmethod
import torch
from torchvision import transforms
from PIL import Image
import streamlit as st
from models.architecture import CNNModel
from services.interfaces import IDiseasePredictor, IDiseaseInfoProvider, PredictionResult
from typing import Optional, Dict, Any, Tuple

from services.disease_data import RICE_DISEASE_INFO, PULSE_DISEASE_INFO

class CropDiseaseHandler(IDiseasePredictor, IDiseaseInfoProvider):
    """
    Base implementation for Crop Disease Handlers.
    - Implements ISP interfaces.
    - Provides common functionality.
    """
    
    def _preprocess_image(self, image) -> Optional[torch.Tensor]:
        """
        Internal helper for preprocessing.
        Marked as protected (_) to imply it's an implementation detail, not part of the public API (LSP).
        """
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

class RiceDiseaseHandler(CropDiseaseHandler):
    def __init__(self, model_path='models/best_model.pth'):
        self.classes = ['Bacterial leaf blight', 'Brown spot', 'Leaf smut', '_Healthy']
        self.model_path = model_path
        self.model = None

    def load_model(self) -> Tuple[bool, Optional[str]]:
        try:
            self.model = CNNModel(num_classes=len(self.classes))
            # Use map_location='cpu' for broad compatibility
            self.model.load_state_dict(torch.load(self.model_path, map_location=torch.device('cpu')))
            self.model.eval()
            return True, None
        except Exception as e:
            return False, str(e)

    def predict(self, image) -> Optional[PredictionResult]:
        if self.model is None:
            return None
            
        try:
            img_tensor = self._preprocess_image(image)
            if img_tensor is None:
                return None
                
            with torch.no_grad():
                outputs = self.model(img_tensor)
                probabilities = torch.nn.functional.softmax(outputs, dim=1)
                confidence, predicted = torch.max(probabilities, 1)
                
            predicted_class = self.classes[predicted.item()]
            confidence_score = confidence.item() * 100
            
            # Create dictionary of all probabilities
            all_probs = {self.classes[i]: probabilities[0][i].item() * 100 for i in range(len(self.classes))}
            
            # Return standardized result object (LSP Compliance)
            return PredictionResult(
                predicted_class=predicted_class,
                confidence_score=confidence_score,
                probabilities=all_probs
            )
        except Exception as e:
            st.error(f"Error during prediction: {str(e)}")
            return None

    def get_disease_info(self, predicted_class: str) -> Dict[str, Any]:
        return RICE_DISEASE_INFO.get(predicted_class, {})

class PulseDiseaseHandler(CropDiseaseHandler):
    def __init__(self, model_path='models/pulse_disease_model.pth'):
        self.classes = ['Angular-Leaf-Spot', 'Bacterial-Pathogen', 'Cercospora-Leaf-Spot', 'No-Disease-Bean', 'Potassium-Deficiency']
        self.model_path = model_path
        self.model = None

    def load_model(self) -> Tuple[bool, Optional[str]]:
        try:
            self.model = CNNModel(num_classes=len(self.classes))
            self.model.load_state_dict(torch.load(self.model_path, map_location=torch.device('cpu')))
            self.model.eval()
            return True, None
        except Exception as e:
            return False, str(e)
            
    def predict(self, image) -> Optional[PredictionResult]:
        if self.model is None:
            return None

        try:
            img_tensor = self._preprocess_image(image)
            if img_tensor is None:
                return None
            
            with torch.no_grad():
                outputs = self.model(img_tensor)
                probabilities = torch.nn.functional.softmax(outputs, dim=1)
                confidence, predicted = torch.max(probabilities, 1)

            predicted_class = self.classes[predicted.item()]
            confidence_score = confidence.item() * 100
            
            all_probs = {self.classes[i]: probabilities[0][i].item() * 100 for i in range(len(self.classes))}
            
            return PredictionResult(
                predicted_class=predicted_class,
                confidence_score=confidence_score,
                probabilities=all_probs
            )
        except Exception as e:
            st.error(f"Error during prediction: {str(e)}")
            return None
        
    def get_disease_info(self, predicted_class: str) -> Dict[str, Any]:
        return PULSE_DISEASE_INFO.get(predicted_class, {})
