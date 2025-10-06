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

  

# Results of Execution



<img width="3318" height="1080" alt="image" src="https://github.com/user-attachments/assets/e61514fc-1901-46f3-a96a-90833dd34ecc" />


<img width="3352" height="1656" alt="image" src="https://github.com/user-attachments/assets/67c0a5e8-5f45-4894-87aa-5110c57d5ac9" />

<img width="3198" height="1488" alt="image" src="https://github.com/user-attachments/assets/597ef08d-12a2-410d-a00d-afb848462900" />

<img width="3332" height="1806" alt="image" src="https://github.com/user-attachments/assets/a7dcbd17-5968-4c2d-96a0-706aaea3faef" />

<img width="3318" height="774" alt="image" src="https://github.com/user-attachments/assets/41399738-6fbb-4f0c-ba72-099f74e0c4eb" />






--------------------- Generated html report: file:///Users/nishthamishra/Desktop/api-automation/api-testing-python/reports/report.html ----------------------
=============================================================== 21 passed, 3 skipped in 6.70s ===============================================================

  

# Built With

* __[Python](https://www.python.org/downloads/)__ - Language used to build the application.
* __[Pycharm](https://www.jetbrains.com/pycharm/download/)__ - The IDE for writing Automation Test Scripts
