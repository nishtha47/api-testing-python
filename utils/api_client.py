import requests
import time
import logging
from typing import Dict, Any, Optional
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

class APIClient:
    def __init__(self):
        self.session = requests.Session()
        self.logger = logging.getLogger(__name__)
        
        # Setup retry strategy
        retry_strategy = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
        )
        
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)
    
    def request(self, method: str, url: str, **kwargs) -> requests.Response:
        start_time = time.time()
        
        # Log request
        self.logger.info(f"Making {method} request to {url}")
        if 'json' in kwargs:
            self.logger.debug(f"Request payload: {kwargs['json']}")
        
        response = self.session.request(method, url, **kwargs)
        response_time = time.time() - start_time
        
        # Log response
        self.logger.info(f"Response: {response.status_code} - Time: {response_time:.2f}s")
        self.logger.debug(f"Response body: {response.text}")
        
        return response
    
    def get(self, url: str, **kwargs) -> requests.Response:
        return self.request('GET', url, **kwargs)
    
    def post(self, url: str, **kwargs) -> requests.Response:
        return self.request('POST', url, **kwargs)
    
    def put(self, url: str, **kwargs) -> requests.Response:
        return self.request('PUT', url, **kwargs)
    
    def delete(self, url: str, **kwargs) -> requests.Response:
        return self.request('DELETE', url, **kwargs)