from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Dict, Optional, Any, List

@dataclass
class PredictionResult:
    """
    Standardized return type for all predictors.
    This ensures Liskov Substitution Principle:
    Any handler can be swapped, and the caller always gets this known structure.
    """
    predicted_class: str
    confidence_score: float
    probabilities: Dict[str, float]

class IDiseasePredictor(ABC):
    """
    Interface for any component that can predict diseases.
    ISP: Clients that only want to predict don't need to know about disease info (descriptions, symptoms).
    """
    @abstractmethod
    def load_model(self) -> tuple[bool, Optional[str]]:
        """Loads the model. Returns (success, error_message)."""
        pass

    @abstractmethod
    def predict(self, image: Any) -> Optional[PredictionResult]:
        """Predicts disease from an image."""
        pass

class IDiseaseInfoProvider(ABC):
    """
    Interface for providing details about diseases.
    ISP: UI components that just show info don't need to depend on heavy ML models.
    """
    @abstractmethod
    def get_disease_info(self, disease_name: str) -> Dict[str, Any]:
        """Returns details like symptoms, treatment, severity."""
        pass
