Steps to Develop Python Framework:

1. Create new project with virtual Env
2. Install all necessary libraries Selenium, Pytest, Pytest-html,Pytest-Xdist,OpenPyxl,Allure Pytest
       Keep all the libraries in requirements.txt and run ->     pip install -r requirement/requirements.txt
3. Create all the required python packages


--------------- Run Test Cases ---------------

 pytest -v -s testCases/test_Login.py --browser chrome
 pytest -vsm sanity
 pytest -vsm regression

 ---------------------------------------------

 Allure- Report:

 allure serve C:\Vikram\Codebase\Python\PythonFramework\reports\allure-report

 ---------------------------------------------