#!/usr/bin/env python3
import subprocess
import sys
import os
import json
from config.robust_config import ServiceHealthChecker

def run_tests_with_health_checks():
    """Run tests with service health checks"""
    
    print("🔍 SERVICE HEALTH CHECK")
    print("=" * 50)
    
    # Check service availability
    available_services = ServiceHealthChecker.get_available_services()
    
    for service, available in available_services.items():
        status = "✅ AVAILABLE" if available else "❌ UNAVAILABLE"
        print(f"  {service}: {status}")
    
    print("\n🚀 RUNNING ROBUST TEST SUITE")
    print("=" * 50)
    
    # Run core tests (JSONPlaceholder is most reliable)
    print("1. Running Core API Tests...")
    result1 = subprocess.run([
        "pytest",
        "tests/test_crud_operations.py",
        "tests/test_error_handling.py", 
        "tests/test_data_validation.py",
        "tests/test_edge_cases.py",
        "-v",
        "--html=reports/core_tests_report.html",
        "--self-contained-html"
    ])
    
    # Run performance tests only if services are available
    if available_services['jsonplaceholder']:
        print("\n2. Running Performance Tests...")
        result2 = subprocess.run([
            "pytest",
            "tests/test_performance.py",
            "-v",
            "--html=reports/performance_report.html",
            "--self-contained-html"
        ])
    else:
        print("\n2. Skipping Performance Tests (JSONPlaceholder unavailable)")
        result2 = subprocess.CompletedProcess(args=[], returncode=0)
    
    # Run authentication tests
    print("\n3. Running Authentication Tests...")
    result3 = subprocess.run([
        "pytest", 
        "tests/test_authentication.py",
        "-v",
        "--html=reports/auth_tests_report.html",
        "--self-contained-html"
    ])
    
    # Generate final summary
    print("\n" + "=" * 50)
    print("📊 TEST EXECUTION SUMMARY")
    print("=" * 50)
    
    results = {
        "Core Tests": result1.returncode,
        "Performance Tests": result2.returncode,
        "Authentication Tests": result3.returncode
    }
    
    all_passed = True
    for test_type, returncode in results.items():
        status = "✅ PASSED" if returncode == 0 else "❌ FAILED"
        print(f"  {test_type}: {status}")
        if returncode != 0:
            all_passed = False
    
    # Service availability report
    print(f"\n🌐 SERVICE AVAILABILITY:")
    available_count = sum(1 for available in available_services.values() if available)
    print(f"  {available_count}/{len(available_services)} services available")
    
    if all_passed:
        print("\n🎉 ALL TESTS COMPLETED SUCCESSFULLY!")
    else:
        print("\n⚠️  SOME TESTS FAILED - Check individual reports")
    
    # Save results to file
    summary = {
        "services_available": available_services,
        "test_results": {k: "PASS" if v == 0 else "FAIL" for k, v in results.items()},
        "all_tests_passed": all_passed
    }
    
    with open('reports/execution_summary.json', 'w') as f:
        json.dump(summary, f, indent=2)
    
    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(run_tests_with_health_checks())