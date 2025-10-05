import requests
from config.config import config

class ServiceHealthChecker:
    """Check health of external services before running tests"""
    
    @staticmethod
    def check_service_health(service_url, timeout=5):
        """Check if a service is healthy"""
        try:
            response = requests.get(service_url, timeout=timeout)
            return response.status_code == 200
        except:
            return False
    
    @classmethod
    def get_available_services(cls):
        """Get list of available services"""
        services = {
            'jsonplaceholder': f"{config.get_base_url('jsonplaceholder')}/posts",
            'httpbin': f"{config.get_base_url('httpbin')}/get",
            'reqres': f"{config.get_base_url('reqres')}/users"
        }
        
        available = {}
        for service, url in services.items():
            available[service] = cls.check_service_health(url)
        
        return available