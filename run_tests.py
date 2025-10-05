#!/usr/bin/env python3
import subprocess
import sys
import os

def run_tests():
    """Main test runner with different configurations"""
    
    # Create reports directory if it doesn't exist
    os.makedirs('reports', exist_ok=True)
    
    print("=" * 60)
    print("API Automation Test Framework")
    print("=" * 60)
    
    # Smoke tests
    print("\n1. Running Smoke Tests...")
    smoke_result = subprocess.call([
        "pytest", 
        "-m", "smoke",
        "--html=reports/smoke_report.html",
        "--self-contained-html",
        "-v"
    ])
    
    # Regression tests
    print("\n2. Running Regression Tests...")
    regression_result = subprocess.call([
        "pytest",
        "-m", "regression", 
        "--html=reports/regression_report.html",
        "--self-contained-html",
        "-v"
    ])
    
    # Performance tests (separate execution)
    print("\n3. Running Performance Tests...")
    performance_result = subprocess.call([
        "pytest",
        "tests/test_performance.py",
        "-v",
        "--html=reports/performance_report.html",
        "--self-contained-html"
    ])
    
    # All tests in parallel
    print("\n4. Running All Tests in Parallel...")
    all_tests_result = subprocess.call([
        "pytest",
        "--html=reports/full_regression_report.html",
        "--self-contained-html",
        "-n", "auto"
    ])
    
    print("\n" + "=" * 60)
    print("Test Execution Completed!")
    print("Reports generated in 'reports' directory")
    print("=" * 60)
    
    return smoke_result + regression_result + performance_result + all_tests_result

if __name__ == "__main__":
    sys.exit(run_tests())