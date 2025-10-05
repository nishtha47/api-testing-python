import pytest
import time
from utils.api_client import APIClient
from config.config import config

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def setup_teardown():
    # Setup code if needed
    yield
    # Teardown code if needed

@pytest.fixture
def unique_email():
    return f"testuser{int(time.time())}@example.com"