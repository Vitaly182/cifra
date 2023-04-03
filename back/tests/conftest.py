import pytest
from fastapi.testclient import TestClient

from main import create_app


@pytest.fixture(scope='module')
def test_client():
    """Create test app"""
    yield TestClient(create_app())

