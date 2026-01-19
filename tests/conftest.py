# tests/conftest.py
import pytest
from app.api_client import APIClient

@pytest.fixture
def api_client():
    return APIClient()