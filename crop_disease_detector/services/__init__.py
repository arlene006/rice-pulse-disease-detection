"""
Services package - Business logic and core services

Contains authentication, disease prediction handlers, dependency injection,
and reporting services.
"""

from crop_disease_detector.services.interfaces import IDiseasePredictor, IDiseaseInfoProvider
from crop_disease_detector.services.auth_service import IAuthService
from crop_disease_detector.services.container import DependencyContainer

__all__ = [
    "IDiseasePredictor",
    "IAuthService", 
    "IDiseaseInfoProvider",
    "DependencyContainer"
]
