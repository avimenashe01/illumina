import pytest
from app import create_app
from svc.services.store_service import StoreService


@pytest.fixture(scope="class")
def store_service():
    """Fixture to provide a fresh instance of StoreService for each test."""
    return StoreService()


@pytest.fixture(scope="class")
def app():
    """Fixture to provide a Flask app instance for testing."""
    app = create_app(testing=True)
    yield app

