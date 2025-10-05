#!/usr/bin/env python3
def test_imports():
    try:
        import requests
        import pytest
        import yaml
        print("✓ All imports successful!")
        assert True
    except ImportError as e:
        print(f"✗ Import failed: {e}")
        assert False

def test_basic_request():
    import requests
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1', timeout=10)
    assert response.status_code == 200
    print("✓ Basic API request successful!")

if __name__ == "__main__":
    test_imports()
    test_basic_request()
    print("🎉 All verification tests passed!")