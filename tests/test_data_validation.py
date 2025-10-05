import pytest
import time
from utils.api_client import APIClient
from config.config import config

class TestDataValidation:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.client = APIClient()
        self.gorest_url = config.get_base_url('gorest')
        self.gorest_token = config.get_auth_token('gorest')
    
    @pytest.mark.regression
    def test_missing_required_fields(self):
        """TC_VALID_001: Missing Required Fields - GoRest"""
        url = f"{self.gorest_url}/users"
        headers = {
            "Authorization": f"Bearer {self.gorest_token}"
        }
        payload = {
            "name": "John Doe"
            # Missing required email, gender, status fields
        }
        
        response = self.client.post(url, json=payload, headers=headers)
        
        # Validation points
        assert response.status_code == 422
        response_data = response.json()
        assert len(response_data) > 0
    
    @pytest.mark.regression
    def test_invalid_email_format(self, unique_email):
        """TC_VALID_002: Invalid Email Format - GoRest"""
        url = f"{self.gorest_url}/users"
        headers = {
            "Authorization": f"Bearer {self.gorest_token}"
        }
        payload = {
            "name": "John Doe",
            "email": "invalid-email-format",
            "gender": "male",
            "status": "active"
        }
        
        response = self.client.post(url, json=payload, headers=headers)
        
        # Validation points
        assert response.status_code == 422
        response_data = response.json()
        # Check for email validation error in response
        assert any('email' in str(item).lower() for item in response_data)
    
    @pytest.mark.regression
    def test_invalid_enum_values(self, unique_email):
        """TC_VALID_003: Invalid Enum Values - GoRest"""
        url = f"{self.gorest_url}/users"
        headers = {
            "Authorization": f"Bearer {self.gorest_token}"
        }
        payload = {
            "name": "John Doe",
            "email": unique_email,
            "gender": "unknown",
            "status": "maybe"
        }
        
        response = self.client.post(url, json=payload, headers=headers)
        
        # Validation points
        assert response.status_code == 422
        response_data = response.json()
        assert len(response_data) > 0