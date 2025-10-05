#!/usr/bin/env python3
import subprocess
import sys
import os

def verify_complete_framework():
    """Verify all framework components are working"""
    
    checks = []
    
    print("🔍 VERIFYING QA AUTOMATION FRAMEWORK")
    print("=" * 50)
    
    # Check 1: Core dependencies
    try:
        import pytest
        import requests
        import yaml
        checks.append(("✅ Core Dependencies", "PASS"))
    except ImportError as e:
        checks.append(("❌ Core Dependencies", f"FAIL: {e}"))
    
    # Check 2: Test discovery
    result = subprocess.run([
        "pytest", "--collect-only", "-q"
    ], capture_output=True, text=True)
    
    if result.returncode == 0 and "test_" in result.stdout:
        test_count = len([line for line in result.stdout.split('\n') if 'test_' in line and '::' in line])
        checks.append(("✅ Test Discovery", f"PASS ({test_count} tests found)"))
    else:
        checks.append(("❌ Test Discovery", "FAIL"))
    
    # Check 3: Smoke tests
    result = subprocess.run([
        "pytest", "-m", "smoke", "-v", "--tb=no"
    ], capture_output=True, text=True)
    
    if result.returncode == 0:
        checks.append(("✅ Smoke Tests", "PASS"))
    else:
        checks.append(("❌ Smoke Tests", "FAIL"))
    
    # Check 4: Parallel execution
    result = subprocess.run([
        "pytest", "-n", "2", "--tb=no", "-q"
    ], capture_output=True, text=True)
    
    if result.returncode == 0:
        checks.append(("✅ Parallel Execution", "PASS"))
    else:
        checks.append(("❌ Parallel Execution", "FAIL"))
    
    # Check 5: HTML reporting
    result = subprocess.run([
        "pytest", "--html=reports/verification_report.html", "--self-contained-html", "-q"
    ], capture_output=True, text=True)
    
    if os.path.exists("reports/verification_report.html"):
        checks.append(("✅ HTML Reporting", "PASS"))
    else:
        checks.append(("❌ HTML Reporting", "FAIL"))
    
    # Print results
    print("\n📋 VERIFICATION RESULTS:")
    for check, status in checks:
        print(f"  {check}: {status}")
    
    # Overall status
    all_passed = all("PASS" in status for _, status in checks)
    
    print("\n" + "=" * 50)
    if all_passed:
        print("🎉 FRAMEWORK VERIFICATION: COMPLETE SUCCESS!")
        print("🚀 Ready for production use!")
        return 0
    else:
        print("⚠️  FRAMEWORK VERIFICATION: SOME ISSUES DETECTED")
        return 1

if __name__ == "__main__":
    sys.exit(verify_complete_framework())