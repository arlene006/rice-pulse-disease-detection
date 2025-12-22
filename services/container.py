from services.auth_service import IAuthService, StreamlitAuthService
from services.disease_handlers import RiceDiseaseHandler, PulseDiseaseHandler, CropDiseaseHandler
from typing import Dict, Type

class DependencyContainer:
    """
    Dependency Injection Container.
    Centralizes object creation and management.
    Ensures 'Single Responsibility' for App: The app doesn't need to know how to create services.
    """
    _instance = None
    
    def __init__(self):
        # Register Services
        self.auth_service: IAuthService = StreamlitAuthService()
        
        # Register Handlers
        # We could use a dictionary to lazy-load or return factories
        self._handlers: Dict[str, Type[CropDiseaseHandler]] = {
            "🌾 Rice": RiceDiseaseHandler,
            "🫘 Pulse": PulseDiseaseHandler
        }

    # Singleton pattern (simplest for Streamlit session)
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = DependencyContainer()
        return cls._instance

    def get_handler(self, crop_name: str) -> CropDiseaseHandler:
        """Factory method to get the correct handler based on selection"""
        handler_class = self._handlers.get(crop_name)
        if handler_class:
            return handler_class()
        # Default fallback or error handling could go here
        return None
