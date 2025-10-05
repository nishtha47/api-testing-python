import re
from typing import Dict, Any

def validate_email_format(email: str) -> bool:
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_response_time(response_time: float, max_time: float) -> bool:
    """Validate response time against maximum allowed time"""
    return response_time <= max_time

def validate_status_code(actual_code: int, expected_code: int) -> bool:
    """Validate status code"""
    return actual_code == expected_code

def validate_response_contains_fields(response_data: Dict, expected_fields: list) -> bool:
    """Validate that response contains expected fields"""
    return all(field in response_data for field in expected_fields)