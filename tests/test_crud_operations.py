import pytest
import time
from utils.api_client import APIClient
from config.config import config

class TestCRUDOperations:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.client = APIClient()
        self.jsonplaceholder_url = config.get_base_url('jsonplaceholder')
        self.gorest_url = config.get_base_url('gorest')
        self.gorest_token = config.get_auth_token('gorest')
    
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_create_resource_jsonplaceholder(self):
        """TC_CRUD_001: Create Resource - JSONPlaceholder"""
        url = f"{self.jsonplaceholder_url}/posts"
        payload = {
            "title": "Test Post Title",
            "body": "This is a test post body content for automation testing",
            "userId": 1
        }
        
        start_time = time.time()
        response = self.client.post(url, json=payload)
        response_time = time.time() - start_time
        
        # Validation points
        assert response.status_code == 201
        assert 'id' in response.json()
        assert response.json()['id'] == 101
        assert response.json()['title'] == payload['title']
        assert response.json()['body'] == payload['body']
        assert response.json()['userId'] == payload['userId']
        assert response_time < 1
    
    @pytest.mark.regression
    def test_create_user_gorest(self, unique_email):
        """TC_CRUD_002: Create User - GoRest (Requires Token)"""
        url = f"{self.gorest_url}/users"
        headers = {
            "Authorization": f"Bearer {self.gorest_token}"
        }
        payload = {
            "name": "John Doe Automation",
            "email": unique_email,
            "gender": "male",
            "status": "active"
        }
        
        response = self.client.post(url, json=payload, headers=headers)
        
        # Validation points
        assert response.status_code == 201
        response_data = response.json()
        assert 'id' in response_data
        assert response_data['name'] == payload['name']
        assert response_data['email'] == payload['email']
        assert response_data['gender'] == payload['gender']
        assert response_data['status'] == payload['status']
    
    @pytest.mark.smoke
    @pytest.mark.regression
    def test_read_single_resource(self):
        """TC_CRUD_003: Read Single Resource - JSONPlaceholder"""
        url = f"{self.jsonplaceholder_url}/posts/1"
        
        response = self.client.get(url)
        
        # Validation points
        assert response.status_code == 200
        response_data = response.json()
        assert 'id' in response_data
        assert 'title' in response_data
        assert 'body' in response_data
        assert 'userId' in response_data
        assert isinstance(response_data['id'], int)
        assert isinstance(response_data['userId'], int)
        assert isinstance(response_data['title'], str)
        assert isinstance(response_data['body'], str)

    @pytest.mark.smoke
    @pytest.mark.regression
    def test_read_single_resource(self):
        """TC_CRUD_003: Read Single Resource - JSONPlaceholder"""
        # ... existing code ...

    @pytest.mark.smoke  
    @pytest.mark.regression
    def test_create_resource_jsonplaceholder(self):
        """TC_CRUD_001: Create Resource - JSONPlaceholder"""
        # ... existing code ...    