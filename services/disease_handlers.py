from abc import ABC, abstractmethod
import torch
from torchvision import transforms
from PIL import Image
import streamlit as st
from models.architecture import CNNModel

# Disease Information Dictionary (Moved here)
RICE_DISEASE_INFO = {
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

class CropDiseaseHandler(ABC):
    """
    Abstract Base Class for Crop Disease Handlers.
    Follows Open/Closed Principle (OCP): New crops can be added by extending this class.
    Follows Dependency Inversion Principle (DIP): App depends on this abstraction.
    """
    
    @abstractmethod
    def load_model(self):
        pass

    @abstractmethod
    def predict(self, image):
        pass
        
    @abstractmethod
    def get_disease_info(self, predicted_class):
        pass
    
    def preprocess_image(self, image):
        """Common preprocessing logic"""
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

    def load_model(self):
        try:
            self.model = CNNModel(num_classes=len(self.classes))
            # Use map_location='cpu' for broad compatibility
            self.model.load_state_dict(torch.load(self.model_path, map_location=torch.device('cpu')))
            self.model.eval()
            return True, None
        except Exception as e:
            return False, str(e)

    def predict(self, image):
        if self.model is None:
            return None, None, None
            
        try:
            img_tensor = self.preprocess_image(image)
            if img_tensor is None:
                return None, None, None
                
            with torch.no_grad():
                outputs = self.model(img_tensor)
                probabilities = torch.nn.functional.softmax(outputs, dim=1)
                confidence, predicted = torch.max(probabilities, 1)
                
            predicted_class = self.classes[predicted.item()]
            confidence_score = confidence.item() * 100
            all_probs = {self.classes[i]: probabilities[0][i].item() * 100 for i in range(len(self.classes))}
            
            return predicted_class, confidence_score, all_probs
        except Exception as e:
            st.error(f"Error during prediction: {str(e)}")
            return None, None, None

    def get_disease_info(self, predicted_class):
        return RICE_DISEASE_INFO.get(predicted_class, {})

# Example of how easy it is to add a new crop (OCP demonstration)
class PulseDiseaseHandler(CropDiseaseHandler):
    def load_model(self):
        return False, "Model under development"
        
    def predict(self, image):
        return None, None, None
        
    def get_disease_info(self, predicted_class):
        return {}
