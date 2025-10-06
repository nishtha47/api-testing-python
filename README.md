<h1 align="center">PyRestAPITest</h1>

<p align="center">  
This application is built to do REST API testing using python scripts along with the use of Pytest module as our testing framework.
</p>

<p align="center">
  <a href="https://opensource.org/licenses/Apache-2.0"><img alt="License" src="https://img.shields.io/badge/License-Apache%202.0-blue.svg"/></a>
</p>

# Demo
![Page-Object-Model-Demo-Gif.gif](demo/pyrestapitest_demo.gif)


## Languages, libraries and tools used

* __[Python](https://www.python.org/downloads/)__
* __[Pytest](https://docs.pytest.org/en/6.2.x/getting-started.html)__
* __[Requests](https://docs.python-requests.org/en/master/)__
* __[JsonPath](https://pypi.org/project/jsonpath/)__
* __[Pycharm](https://www.jetbrains.com/pycharm/download/)__

Above Features are used to make code simple, generic, understandable, clean and easily maintainable for future development.

## Installation

Install the dependencies and start the testing.

 __Install Pytest__:
```sh
pip install -U pytest
```
 __Install Requests__:
```sh
pip install requests
```

 __Install Json Path__:
```sh
pip install jsonpath
```
## Automated tests

__To run a test, you can simply write the following command on Terminal__:
```sh
pytest
```

```
 # Run the robust test suite         
python run_robust_tests.py

# Or run specific reliable test groups
pytest tests/test_crud_operations.py tests/test_error_handling.py tests/test_data_validation.py -v

# Run with detailed output
pytest -v --tb=short

```

__To run and get details of all the executed test, you can simply write the following command on Terminal__:
```sh
pytest -rA
```

__To run and generate full HTML details report of all the executed test, you can simply write the following commands on Terminal__:

__But first install [Pytest-HTML](https://pypi.org/project/pytest-html/) by writing the following command on Terminal__
```sh
pip install pytest-html
```
__Then write the following command on Terminal__
```sh
pytest --html==YOUR_REPORT_FILE_NAME.html
```

__To see the reports, open the Project window, and then right-click then click on refresh then right-click on __StationReport.html__ to open the file on the default browser.__

![Page-Object-Model-Demo-Gif.gif](demo/pyrestapitest-report-file.png)

# Prerequisites
* __Python__
* __Any IDE__

  __ Results of Execution

==================================================================== test session starts ====================================================================
platform darwin -- Python 3.13.3, pytest-7.4.4, pluggy-1.6.0 -- /Users/nishthamishra/Desktop/api-automation/api-testing-python/venv/bin/python3.13
cachedir: .pytest_cache
metadata: {'Python': '3.13.3', 'Platform': 'macOS-14.4-arm64-arm-64bit-Mach-O', 'Packages': {'pytest': '7.4.4', 'pluggy': '1.6.0'}, 'Plugins': {'timeout': '2.2.0', 'html': '4.1.1', 'metadata': '3.1.1', 'xdist': '3.5.0'}}
rootdir: /Users/nishthamishra/Desktop/api-automation/api-testing-python
configfile: pytest.ini
testpaths: tests
plugins: timeout-2.2.0, html-4.1.1, metadata-3.1.1, xdist-3.5.0
12 workers [24 items]     
scheduling tests via LoadScheduling

tests/test_authentication.py::TestAuthentication::test_missing_password 
tests/test_performance.py::TestPerformance::test_pagination_performance 
tests/test_performance_stable.py::TestPerformanceStable::test_pagination_performance_stable 
tests/test_performance.py::TestPerformance::test_response_time_validation 
tests/test_stations.py::TestStations::test_posts_api_returned_list_length 
tests/test_authentication.py::TestAuthentication::test_valid_authentication 
tests/test_error_handling.py::TestErrorHandling::test_method_not_allowed 
tests/test_data_validation.py::TestDataValidation::test_missing_required_fields 
tests/test_crud_operations.py::TestCRUDOperations::test_create_user_gorest 
tests/test_edge_cases.py::TestEdgeCases::test_unicode_special_characters 
tests/test_performance_stable.py::TestPerformanceStable::test_response_time_validation_stable 
tests/test_data_validation.py::TestDataValidation::test_invalid_enum_values 
[gw11] [  4%] PASSED tests/test_stations.py::TestStations::test_posts_api_returned_list_length 
tests/test_stations.py::TestStations::test_data_model 
[gw7] [  8%] FAILED tests/test_performance.py::TestPerformance::test_response_time_validation 
tests/test_performance.py::TestPerformance::test_concurrent_request_handling 
[gw0] [ 12%] SKIPPED tests/test_authentication.py::TestAuthentication::test_valid_authentication 
tests/test_authentication.py::TestAuthentication::test_invalid_credentials 
[gw3] [ 16%] PASSED tests/test_data_validation.py::TestDataValidation::test_missing_required_fields 
tests/test_data_validation.py::TestDataValidation::test_invalid_email_format 
[gw1] [ 20%] SKIPPED tests/test_authentication.py::TestAuthentication::test_missing_password 
tests/test_crud_operations.py::TestCRUDOperations::test_create_resource_jsonplaceholder 
[gw1] [ 25%] PASSED tests/test_crud_operations.py::TestCRUDOperations::test_create_resource_jsonplaceholder 
[gw0] [ 29%] SKIPPED tests/test_authentication.py::TestAuthentication::test_invalid_credentials 
[gw4] [ 33%] PASSED tests/test_data_validation.py::TestDataValidation::test_invalid_enum_values 
tests/test_edge_cases.py::TestEdgeCases::test_empty_request_body 
[gw5] [ 37%] PASSED tests/test_edge_cases.py::TestEdgeCases::test_unicode_special_characters 
tests/test_error_handling.py::TestErrorHandling::test_resource_not_found 
[gw11] [ 41%] PASSED tests/test_stations.py::TestStations::test_data_model 
[gw10] [ 45%] PASSED tests/test_performance_stable.py::TestPerformanceStable::test_pagination_performance_stable 
tests/test_performance_stable.py::TestPerformanceStable::test_stress_test_stable 
[gw9] [ 50%] PASSED tests/test_performance_stable.py::TestPerformanceStable::test_response_time_validation_stable 
tests/test_performance_stable.py::TestPerformanceStable::test_concurrent_request_handling_stable 
[gw2] [ 54%] PASSED tests/test_crud_operations.py::TestCRUDOperations::test_create_user_gorest 
tests/test_crud_operations.py::TestCRUDOperations::test_read_single_resource 
[gw2] [ 58%] PASSED tests/test_crud_operations.py::TestCRUDOperations::test_read_single_resource 
[gw8] [ 62%] FAILED tests/test_performance.py::TestPerformance::test_pagination_performance 
tests/test_performance.py::TestPerformance::test_stress_test 
[gw5] [ 66%] PASSED tests/test_error_handling.py::TestErrorHandling::test_resource_not_found 
[gw3] [ 70%] PASSED tests/test_data_validation.py::TestDataValidation::test_invalid_email_format 
[gw4] [ 75%] PASSED tests/test_edge_cases.py::TestEdgeCases::test_empty_request_body 
[gw9] [ 79%] PASSED tests/test_performance_stable.py::TestPerformanceStable::test_concurrent_request_handling_stable 
[gw10] [ 83%] PASSED tests/test_performance_stable.py::TestPerformanceStable::test_stress_test_stable 
[gw6] [ 87%] PASSED tests/test_error_handling.py::TestErrorHandling::test_method_not_allowed 
tests/test_error_handling.py::TestErrorHandling::test_invalid_url_path 
[gw6] [ 91%] PASSED tests/test_error_handling.py::TestErrorHandling::test_invalid_url_path 
[gw8] [ 95%] PASSED tests/test_performance.py::TestPerformance::test_stress_test 
[gw7] [100%] PASSED tests/test_performance.py::TestPerformance::test_concurrent_request_handling 

========================================================================= FAILURES ==========================================================================
_______________________________________________________ TestPerformance.test_response_time_validation _______________________________________________________
[gw7] darwin -- Python 3.13.3 /Users/nishthamishra/Desktop/api-automation/api-testing-python/venv/bin/python3.13
tests/test_performance.py:30: in test_response_time_validation
    assert response_time < max_time, f"Response time {response_time:.2f}s exceeds {max_time}s for {endpoint}"
E   AssertionError: Response time 0.50s exceeds 0.5s for https://jsonplaceholder.typicode.com/posts/1
E   assert 0.501694917678833 < 0.5
________________________________________________________ TestPerformance.test_pagination_performance ________________________________________________________
[gw8] darwin -- Python 3.13.3 /Users/nishthamishra/Desktop/api-automation/api-testing-python/venv/bin/python3.13
tests/test_performance.py:99: in test_pagination_performance
    assert max_time <= min_time * 4, \
E   AssertionError: Response times vary too much: min=0.14s, max=0.86s
E   assert 0.8592240810394287 <= (0.14125800132751465 * 4)
--------------------- Generated html report: file:///Users/nishthamishra/Desktop/api-automation/api-testing-python/reports/report.html ----------------------
================================================================== short test summary info ==================================================================
FAILED tests/test_performance.py::TestPerformance::test_response_time_validation - AssertionError: Response time 0.50s exceeds 0.5s for https://jsonplaceholder.typicode.com/posts/1
FAILED tests/test_performance.py::TestPerformance::test_pagination_performance - AssertionError: Response times vary too much: min=0.14s, max=0.86s
========================================================== 2 failed, 19 passed, 3 skipped in 7.84s ==========================================================
(venv) nishthamishra@Nishthas-MacBook-Pro api-testing-python % # Run the robust test suite
python run_robust_tests.py

# Or run specific reliable test groups
pytest tests/test_crud_operations.py tests/test_error_handling.py tests/test_data_validation.py -v

# Run with detailed output
pytest -v --tb=short
zsh: command not found: #
🔍 SERVICE HEALTH CHECK
==================================================
  jsonplaceholder: ✅ AVAILABLE
  httpbin: ✅ AVAILABLE
  reqres: ❌ UNAVAILABLE

🚀 RUNNING ROBUST TEST SUITE
==================================================
1. Running Core API Tests...
==================================================================== test session starts ====================================================================
platform darwin -- Python 3.13.3, pytest-7.4.4, pluggy-1.6.0 -- /Users/nishthamishra/Desktop/api-automation/api-testing-python/venv/bin/python3.13
cachedir: .pytest_cache
metadata: {'Python': '3.13.3', 'Platform': 'macOS-14.4-arm64-arm-64bit-Mach-O', 'Packages': {'pytest': '7.4.4', 'pluggy': '1.6.0'}, 'Plugins': {'timeout': '2.2.0', 'html': '4.1.1', 'metadata': '3.1.1', 'xdist': '3.5.0'}}
rootdir: /Users/nishthamishra/Desktop/api-automation/api-testing-python
configfile: pytest.ini
plugins: timeout-2.2.0, html-4.1.1, metadata-3.1.1, xdist-3.5.0
12 workers [11 items]     
scheduling tests via LoadScheduling

tests/test_crud_operations.py::TestCRUDOperations::test_read_single_resource 
tests/test_crud_operations.py::TestCRUDOperations::test_create_user_gorest 
tests/test_crud_operations.py::TestCRUDOperations::test_create_resource_jsonplaceholder 
tests/test_edge_cases.py::TestEdgeCases::test_empty_request_body 
tests/test_error_handling.py::TestErrorHandling::test_invalid_url_path 
tests/test_data_validation.py::TestDataValidation::test_invalid_enum_values 
tests/test_error_handling.py::TestErrorHandling::test_resource_not_found 
tests/test_data_validation.py::TestDataValidation::test_missing_required_fields 
tests/test_data_validation.py::TestDataValidation::test_invalid_email_format 
tests/test_edge_cases.py::TestEdgeCases::test_unicode_special_characters 
tests/test_error_handling.py::TestErrorHandling::test_method_not_allowed 
[gw3] [  9%] PASSED tests/test_error_handling.py::TestErrorHandling::test_resource_not_found 
[gw2] [ 18%] PASSED tests/test_crud_operations.py::TestCRUDOperations::test_read_single_resource 
[gw5] [ 27%] PASSED tests/test_error_handling.py::TestErrorHandling::test_invalid_url_path 
[gw0] [ 36%] PASSED tests/test_crud_operations.py::TestCRUDOperations::test_create_resource_jsonplaceholder 
[gw9] [ 45%] PASSED tests/test_edge_cases.py::TestEdgeCases::test_empty_request_body 
[gw10] [ 54%] PASSED tests/test_edge_cases.py::TestEdgeCases::test_unicode_special_characters 
[gw6] [ 63%] PASSED tests/test_data_validation.py::TestDataValidation::test_missing_required_fields 
[gw7] [ 72%] PASSED tests/test_data_validation.py::TestDataValidation::test_invalid_email_format 
[gw1] [ 81%] PASSED tests/test_crud_operations.py::TestCRUDOperations::test_create_user_gorest 
[gw8] [ 90%] PASSED tests/test_data_validation.py::TestDataValidation::test_invalid_enum_values 
[gw4] [100%] PASSED tests/test_error_handling.py::TestErrorHandling::test_method_not_allowed 

---------------- Generated html report: file:///Users/nishthamishra/Desktop/api-automation/api-testing-python/reports/core_tests_report.html ----------------
==================================================================== 11 passed in 2.73s =====================================================================

2. Running Performance Tests...
==================================================================== test session starts ====================================================================
platform darwin -- Python 3.13.3, pytest-7.4.4, pluggy-1.6.0 -- /Users/nishthamishra/Desktop/api-automation/api-testing-python/venv/bin/python3.13
cachedir: .pytest_cache
metadata: {'Python': '3.13.3', 'Platform': 'macOS-14.4-arm64-arm-64bit-Mach-O', 'Packages': {'pytest': '7.4.4', 'pluggy': '1.6.0'}, 'Plugins': {'timeout': '2.2.0', 'html': '4.1.1', 'metadata': '3.1.1', 'xdist': '3.5.0'}}
rootdir: /Users/nishthamishra/Desktop/api-automation/api-testing-python
configfile: pytest.ini
plugins: timeout-2.2.0, html-4.1.1, metadata-3.1.1, xdist-3.5.0
12 workers [4 items]      
scheduling tests via LoadScheduling

tests/test_performance.py::TestPerformance::test_response_time_validation 
tests/test_performance.py::TestPerformance::test_pagination_performance 
tests/test_performance.py::TestPerformance::test_stress_test 
tests/test_performance.py::TestPerformance::test_concurrent_request_handling 
[gw0] [ 25%] PASSED tests/test_performance.py::TestPerformance::test_response_time_validation 
[gw2] [ 50%] PASSED tests/test_performance.py::TestPerformance::test_pagination_performance 
[gw1] [ 75%] PASSED tests/test_performance.py::TestPerformance::test_concurrent_request_handling 
[gw3] [100%] PASSED tests/test_performance.py::TestPerformance::test_stress_test 

--------------- Generated html report: file:///Users/nishthamishra/Desktop/api-automation/api-testing-python/reports/performance_report.html ----------------
===================================================================== 4 passed in 6.87s =====================================================================

3. Running Authentication Tests...
==================================================================== test session starts ====================================================================
platform darwin -- Python 3.13.3, pytest-7.4.4, pluggy-1.6.0 -- /Users/nishthamishra/Desktop/api-automation/api-testing-python/venv/bin/python3.13
cachedir: .pytest_cache
metadata: {'Python': '3.13.3', 'Platform': 'macOS-14.4-arm64-arm-64bit-Mach-O', 'Packages': {'pytest': '7.4.4', 'pluggy': '1.6.0'}, 'Plugins': {'timeout': '2.2.0', 'html': '4.1.1', 'metadata': '3.1.1', 'xdist': '3.5.0'}}
rootdir: /Users/nishthamishra/Desktop/api-automation/api-testing-python
configfile: pytest.ini
plugins: timeout-2.2.0, html-4.1.1, metadata-3.1.1, xdist-3.5.0
12 workers [3 items]      
scheduling tests via LoadScheduling

tests/test_authentication.py::TestAuthentication::test_missing_password 
tests/test_authentication.py::TestAuthentication::test_invalid_credentials 
tests/test_authentication.py::TestAuthentication::test_valid_authentication 
[gw1] [ 33%] SKIPPED tests/test_authentication.py::TestAuthentication::test_invalid_credentials 
[gw2] [ 66%] SKIPPED tests/test_authentication.py::TestAuthentication::test_missing_password 
[gw0] [100%] SKIPPED tests/test_authentication.py::TestAuthentication::test_valid_authentication 

---------------- Generated html report: file:///Users/nishthamishra/Desktop/api-automation/api-testing-python/reports/auth_tests_report.html ----------------
==================================================================== 3 skipped in 1.76s =====================================================================

==================================================
📊 TEST EXECUTION SUMMARY
==================================================
  Core Tests: ✅ PASSED
  Performance Tests: ✅ PASSED
  Authentication Tests: ✅ PASSED

🌐 SERVICE AVAILABILITY:
  2/3 services available

🎉 ALL TESTS COMPLETED SUCCESSFULLY!
zsh: command not found: #
==================================================================== test session starts ====================================================================
platform darwin -- Python 3.13.3, pytest-7.4.4, pluggy-1.6.0 -- /Users/nishthamishra/Desktop/api-automation/api-testing-python/venv/bin/python3.13
cachedir: .pytest_cache
metadata: {'Python': '3.13.3', 'Platform': 'macOS-14.4-arm64-arm-64bit-Mach-O', 'Packages': {'pytest': '7.4.4', 'pluggy': '1.6.0'}, 'Plugins': {'timeout': '2.2.0', 'html': '4.1.1', 'metadata': '3.1.1', 'xdist': '3.5.0'}}
rootdir: /Users/nishthamishra/Desktop/api-automation/api-testing-python
configfile: pytest.ini
plugins: timeout-2.2.0, html-4.1.1, metadata-3.1.1, xdist-3.5.0
12 workers [9 items]      
scheduling tests via LoadScheduling

tests/test_data_validation.py::TestDataValidation::test_missing_required_fields 
tests/test_error_handling.py::TestErrorHandling::test_resource_not_found 
tests/test_data_validation.py::TestDataValidation::test_invalid_email_format 
tests/test_crud_operations.py::TestCRUDOperations::test_create_resource_jsonplaceholder 
tests/test_error_handling.py::TestErrorHandling::test_method_not_allowed 
tests/test_crud_operations.py::TestCRUDOperations::test_read_single_resource 
tests/test_crud_operations.py::TestCRUDOperations::test_create_user_gorest 
tests/test_error_handling.py::TestErrorHandling::test_invalid_url_path 
tests/test_data_validation.py::TestDataValidation::test_invalid_enum_values 
[gw2] [ 11%] PASSED tests/test_crud_operations.py::TestCRUDOperations::test_read_single_resource 
[gw3] [ 22%] PASSED tests/test_error_handling.py::TestErrorHandling::test_resource_not_found 
[gw5] [ 33%] PASSED tests/test_error_handling.py::TestErrorHandling::test_invalid_url_path 
[gw0] [ 44%] PASSED tests/test_crud_operations.py::TestCRUDOperations::test_create_resource_jsonplaceholder 
[gw6] [ 55%] PASSED tests/test_data_validation.py::TestDataValidation::test_missing_required_fields 
[gw8] [ 66%] PASSED tests/test_data_validation.py::TestDataValidation::test_invalid_enum_values 
[gw1] [ 77%] PASSED tests/test_crud_operations.py::TestCRUDOperations::test_create_user_gorest 
[gw7] [ 88%] PASSED tests/test_data_validation.py::TestDataValidation::test_invalid_email_format 
[gw4] [100%] PASSED tests/test_error_handling.py::TestErrorHandling::test_method_not_allowed 

--------------------- Generated html report: file:///Users/nishthamishra/Desktop/api-automation/api-testing-python/reports/report.html ----------------------
===================================================================== 9 passed in 2.21s =====================================================================
zsh: command not found: #
==================================================================== test session starts ====================================================================
platform darwin -- Python 3.13.3, pytest-7.4.4, pluggy-1.6.0 -- /Users/nishthamishra/Desktop/api-automation/api-testing-python/venv/bin/python3.13
cachedir: .pytest_cache
metadata: {'Python': '3.13.3', 'Platform': 'macOS-14.4-arm64-arm-64bit-Mach-O', 'Packages': {'pytest': '7.4.4', 'pluggy': '1.6.0'}, 'Plugins': {'timeout': '2.2.0', 'html': '4.1.1', 'metadata': '3.1.1', 'xdist': '3.5.0'}}
rootdir: /Users/nishthamishra/Desktop/api-automation/api-testing-python
configfile: pytest.ini
testpaths: tests
plugins: timeout-2.2.0, html-4.1.1, metadata-3.1.1, xdist-3.5.0
12 workers [24 items]     
scheduling tests via LoadScheduling

tests/test_data_validation.py::TestDataValidation::test_missing_required_fields 
tests/test_crud_operations.py::TestCRUDOperations::test_create_user_gorest 
tests/test_stations.py::TestStations::test_posts_api_returned_list_length 
tests/test_data_validation.py::TestDataValidation::test_invalid_enum_values 
tests/test_authentication.py::TestAuthentication::test_valid_authentication 
tests/test_authentication.py::TestAuthentication::test_missing_password 
tests/test_edge_cases.py::TestEdgeCases::test_unicode_special_characters 
tests/test_performance.py::TestPerformance::test_pagination_performance 
tests/test_performance.py::TestPerformance::test_response_time_validation 
tests/test_performance_stable.py::TestPerformanceStable::test_pagination_performance_stable 
tests/test_performance_stable.py::TestPerformanceStable::test_response_time_validation_stable 
tests/test_error_handling.py::TestErrorHandling::test_method_not_allowed 
[gw11] [  4%] PASSED tests/test_stations.py::TestStations::test_posts_api_returned_list_length 
tests/test_stations.py::TestStations::test_data_model 
[gw0] [  8%] SKIPPED tests/test_authentication.py::TestAuthentication::test_valid_authentication 
tests/test_authentication.py::TestAuthentication::test_invalid_credentials 
[gw1] [ 12%] SKIPPED tests/test_authentication.py::TestAuthentication::test_missing_password 
tests/test_crud_operations.py::TestCRUDOperations::test_create_resource_jsonplaceholder 
[gw9] [ 16%] PASSED tests/test_performance_stable.py::TestPerformanceStable::test_response_time_validation_stable 
tests/test_performance_stable.py::TestPerformanceStable::test_concurrent_request_handling_stable 
[gw10] [ 20%] PASSED tests/test_performance_stable.py::TestPerformanceStable::test_pagination_performance_stable 
tests/test_performance_stable.py::TestPerformanceStable::test_stress_test_stable 
[gw7] [ 25%] PASSED tests/test_performance.py::TestPerformance::test_response_time_validation 
tests/test_performance.py::TestPerformance::test_concurrent_request_handling 
[gw0] [ 29%] SKIPPED tests/test_authentication.py::TestAuthentication::test_invalid_credentials 
[gw5] [ 33%] PASSED tests/test_edge_cases.py::TestEdgeCases::test_unicode_special_characters 
tests/test_error_handling.py::TestErrorHandling::test_resource_not_found 
[gw4] [ 37%] PASSED tests/test_data_validation.py::TestDataValidation::test_invalid_enum_values 
tests/test_edge_cases.py::TestEdgeCases::test_empty_request_body 
[gw3] [ 41%] PASSED tests/test_data_validation.py::TestDataValidation::test_missing_required_fields 
tests/test_data_validation.py::TestDataValidation::test_invalid_email_format 
[gw2] [ 45%] PASSED tests/test_crud_operations.py::TestCRUDOperations::test_create_user_gorest 
tests/test_crud_operations.py::TestCRUDOperations::test_read_single_resource 
[gw8] [ 50%] PASSED tests/test_performance.py::TestPerformance::test_pagination_performance 
tests/test_performance.py::TestPerformance::test_stress_test 
[gw11] [ 54%] PASSED tests/test_stations.py::TestStations::test_data_model 
[gw1] [ 58%] PASSED tests/test_crud_operations.py::TestCRUDOperations::test_create_resource_jsonplaceholder 
[gw5] [ 62%] PASSED tests/test_error_handling.py::TestErrorHandling::test_resource_not_found 
[gw2] [ 66%] PASSED tests/test_crud_operations.py::TestCRUDOperations::test_read_single_resource 
[gw9] [ 70%] PASSED tests/test_performance_stable.py::TestPerformanceStable::test_concurrent_request_handling_stable 
[gw4] [ 75%] PASSED tests/test_edge_cases.py::TestEdgeCases::test_empty_request_body 
[gw3] [ 79%] PASSED tests/test_data_validation.py::TestDataValidation::test_invalid_email_format 
[gw10] [ 83%] PASSED tests/test_performance_stable.py::TestPerformanceStable::test_stress_test_stable 
[gw6] [ 87%] PASSED tests/test_error_handling.py::TestErrorHandling::test_method_not_allowed 
tests/test_error_handling.py::TestErrorHandling::test_invalid_url_path 
[gw6] [ 91%] PASSED tests/test_error_handling.py::TestErrorHandling::test_invalid_url_path 
[gw8] [ 95%] PASSED tests/test_performance.py::TestPerformance::test_stress_test 
[gw7] [100%] PASSED tests/test_performance.py::TestPerformance::test_concurrent_request_handling 

--------------------- Generated html report: file:///Users/nishthamishra/Desktop/api-automation/api-testing-python/reports/report.html ----------------------
=============================================================== 21 passed, 3 skipped in 6.70s ===============================================================

  

# Built With

* __[Python](https://www.python.org/downloads/)__ - Language used to build the application.
* __[Pycharm](https://www.jetbrains.com/pycharm/download/)__ - The IDE for writing Automation Test Scripts
