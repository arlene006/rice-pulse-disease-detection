import pytest
from unittest.mock import MagicMock
from crop_disease_detector.services.container import DependencyContainer
from crop_disease_detector.services.auth_service import IAuthService
from crop_disease_detector.services.disease_handlers import RiceDiseaseHandler, PulseDiseaseHandler

def test_container_is_singleton():
    """Verify DependencyContainer creates only one instance."""
    c1 = DependencyContainer.get_instance()
    c2 = DependencyContainer.get_instance()
    assert c1 is c2

def test_container_resolves_auth_service():
    """Verify container provides an auth service instance."""
    container = DependencyContainer.get_instance()
    assert isinstance(container.auth_service, IAuthService)

def test_container_factory_rice():
    """Verify container returns correct handler for Rice."""
    container = DependencyContainer.get_instance()
    handler = container.get_handler("🌾 Rice")
    assert isinstance(handler, RiceDiseaseHandler)

def test_container_factory_pulse():
    """Verify container returns correct handler for Pulse."""
    container = DependencyContainer.get_instance()
    handler = container.get_handler("🫘 Pulse")
    assert isinstance(handler, PulseDiseaseHandler)

def test_container_factory_invalid():
    """Verify container returns None for unknown crops."""
    container = DependencyContainer.get_instance()
    handler = container.get_handler("Unknown Crop")
    assert handler is None
