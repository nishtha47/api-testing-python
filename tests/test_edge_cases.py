import pytest
import time
from utils.api_client import APIClient
from config.config import config

class TestEdgeCases:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.client = APIClient()
        self.gorest_url = config.get_base_url('gorest')
        self.gorest_token = config.get_auth_token('gorest')
    
    @pytest.mark.regression
    def test_empty_request_body(self):
        """TC_EDGE_001: Empty Request Body"""
        url = f"{self.gorest_url}/users"
        headers = {
            "Authorization": f"Bearer {self.gorest_token}"
        }
        payload = {}
        
        response = self.client.post(url, json=payload, headers=headers)
        
        # Validation points
        assert response.status_code == 422  # Unprocessable Entity
    
    @pytest.mark.regression
    def test_unicode_special_characters(self, unique_email):
        """TC_EDGE_003: Unicode and Special Characters"""
        url = f"{self.gorest_url}/users"
        headers = {
            "Authorization": f"Bearer {self.gorest_token}"
        }
        payload = {
            "name": "José María González-Pérez £$%^",
            "email": unique_email.replace('@', 'josé@'),
            "gender": "male",
            "status": "active"
        }
        
        response = self.client.post(url, json=payload, headers=headers)
        
        # Validation points
        if response.status_code == 201:
            response_data = response.json()
            assert response_data['name'] == payload['name']