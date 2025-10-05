import json
import random
import string
from typing import Dict, Any

def generate_random_string(length: int = 10) -> str:
    """Generate random string for test data"""
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def generate_random_email() -> str:
    """Generate random email for test data"""
    return f"test_{generate_random_string(8)}@example.com"

def load_test_data(file_path: str) -> Dict[str, Any]:
    """Load test data from JSON file"""
    with open(file_path, 'r') as file:
        return json.load(file)

def validate_json_schema(response_data: Dict, expected_schema: Dict) -> bool:
    """Validate response against expected JSON schema"""
    for key, expected_type in expected_schema.items():
        if key not in response_data:
            return False
        if not isinstance(response_data[key], expected_type):
            return False
    return True