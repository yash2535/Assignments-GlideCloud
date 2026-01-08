import sys
import os
import pytest
from fastapi.testclient import TestClient

# Add project root to PYTHONPATH
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from main import app


@pytest.fixture(scope="session")
def client():
    return TestClient(app)
