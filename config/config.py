import os
import yaml
from typing import Dict, Any

class Config:
    def __init__(self):
        self.environment = os.getenv('ENVIRONMENT', 'dev')
        self.load_config()
    
    def load_config(self):
        with open('config/environments.yaml', 'r') as file:
            config_data = yaml.safe_load(file)
        
        self.base_urls = config_data['base_urls']
        self.auth_tokens = config_data['auth_tokens']
        self.timeouts = config_data['timeouts']
    
    def get_base_url(self, service: str) -> str:
        return self.base_urls[service]
    
    def get_auth_token(self, service: str) -> str:
        return self.auth_tokens.get(service, '')

config = Config()