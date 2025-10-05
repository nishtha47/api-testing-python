import pytest
import time
from utils.api_client import APIClient
from config.config import config

class TestErrorHandling:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.client = APIClient()
        self.jsonplaceholder_url = config.get_base_url('jsonplaceholder')
        self.httpbin_url = config.get_base_url('httpbin')
    
    @pytest.mark.regression
    def test_resource_not_found(self):
        """TC_ERROR_001: Resource Not Found - JSONPlaceholder"""
        url = f"{self.jsonplaceholder_url}/posts/99999"
        
        response = self.client.get(url)
        
        # Validation points
        assert response.status_code == 404
        assert response.json() == {}
    
    @pytest.mark.regression
    def test_method_not_allowed(self):
        """TC_ERROR_002: Method Not Allowed - HTTPBin"""
        url = f"{self.httpbin_url}/get"
        
        try:
            response = self.client.delete(url)
            # If we get here, check the status code
            if response.status_code == 503:
                pytest.skip("HTTPBin service temporarily unavailable")
            else:
                assert response.status_code == 405
        except Exception as e:
            if "503" in str(e):
                pytest.skip("HTTPBin service temporarily unavailable")
            else:
                raise
    
    @pytest.mark.regression
    def test_invalid_url_path(self):
        """TC_ERROR_003: Invalid URL Path - JSONPlaceholder"""
        url = f"{self.jsonplaceholder_url}/invalid-endpoint"
        
        response = self.client.get(url)
        
        # Validation points
        assert response.status_code == 404
        assert response.json() == {}