#!/usr/bin/env python3
import subprocess
import sys

def run_command(command):
    """Run a shell command and return success status"""
    try:
        result = subprocess.run(command, shell=True, check=True, 
                              capture_output=True, text=True)
        print(f"✓ {command}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ {command}")
        print(f"Error: {e.stderr}")
        return False

def main():
    print("Setting up API Testing Framework...")
    print("=" * 50)
    
    # Install packages individually to avoid conflicts
    packages = [
        "pip install pytest==7.4.4",
        "pip install requests==2.31.0", 
        "pip install PyYAML==6.0.1",
        "pip install pytest-html==4.1.1",
        "pip install pytest-xdist==3.5.0",
        "pip install pytest-timeout==2.2.0"
    ]
    
    all_success = True
    for package in packages:
        if not run_command(package):
            all_success = False
    
    if all_success:
        print("\n" + "=" * 50)
        print("✓ All dependencies installed successfully!")
        print("Testing imports...")
        
        # Test imports
        try:
            import requests
            import pytest
            import yaml
            print("✓ All imports working!")
            
            # Run a quick test
            print("\nRunning quick verification test...")
            subprocess.run([sys.executable, "-c", 
                          "import requests; r = requests.get('https://httpbin.org/get'); print(f'Test request: {r.status_code}')"], 
                         check=True)
            
        except ImportError as e:
            print(f"✗ Import error: {e}")
            all_success = False
    
    print("\n" + "=" * 50)
    if all_success:
        print("🎉 Setup completed successfully!")
        print("You can now run: pytest -m smoke -v")
    else:
        print("❌ Setup encountered issues. Please check the errors above.")
    
    return 0 if all_success else 1

if __name__ == "__main__":
    sys.exit(main())