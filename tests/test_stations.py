import pytest
from utils.api_client import APIClient
from config.config import config

class TestStations:
    """Tests for JSONPlaceholder posts (replacing station tests)"""
    
    @pytest.fixture(autouse=True)
    def setup(self):
        self.client = APIClient()
        self.jsonplaceholder_url = config.get_base_url('jsonplaceholder')
    
    def test_posts_api_returned_list_length(self):
        """Test that posts API returns expected number of items"""
        url = f"{self.jsonplaceholder_url}/posts"
        
        response = self.client.get(url)
        
        assert response.status_code == 200
        posts_data = response.json()
        
        # JSONPlaceholder should return 100 posts
        assert len(posts_data) == 100, f"Expected 100 posts, got {len(posts_data)}"
    
    def test_data_model(self):
        """Test that posts data has correct structure"""
        url = f"{self.jsonplaceholder_url}/posts"
        
        response = self.client.get(url)
        
        assert response.status_code == 200
        posts_data = response.json()
        
        # Check that we have a list of dictionaries
        assert isinstance(posts_data, list)
        assert len(posts_data) > 0
        
        # Check structure of first post
        first_post = posts_data[0]
        expected_fields = ['userId', 'id', 'title', 'body']
        
        for field in expected_fields:
            assert field in first_post, f"Missing field: {field}"
        
        # Check data types
        assert isinstance(first_post['userId'], int)
        assert isinstance(first_post['id'], int)
        assert isinstance(first_post['title'], str)
        assert isinstance(first_post['body'], str)