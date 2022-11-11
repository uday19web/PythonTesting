# Any pytest file should start with "test_" or end with test
# Pytest method names should start with "test"
# Any code should be wrapped with method only
# Method name should be sense
''' command line flags
-k -> Stands for methods names execution
-s -> stands for logs in output
-v -> stands for more info metadata
-m -> stands for mark
py.test --html=report.html - stands for generate the html report
run a specific file with py.test <file name> '''
# you can mark(tag) test @pytest.mark."smoke" and then runs with -m
# you can skip the test @pytest.mark.skip
# @pytest.mark.xfail - it will run the test but will not show the status in the output
# fixture are used as setup and tear down methods for the test cases
# "conftest" file to generalize fixture and make it available to all test case
# datadriven and parameterization can be done with return statement in tuple format
# when you define fixture scope to class only, it will run before class is initiated and at the end

'''In the pytest standard we have to the write th code in "def" function only
in Pytest this function are called methods. the name of the method starts with "test" always
In pytest every method is consider as a Test Cases'''
import pytest

'''mark.nameoftest - ithu ehukku na lot test scenarios iruku like smoke, regression like that
so ipo enaku smoke test case matum run pananum na we cant include the name in the "methods name".
so we are using the "mark" in the pytest.'''


@pytest.mark.smoke
def test_firstprogram(setup):
    print("Hello")


@pytest.mark.xfail
def test_secondgreetcreditcard():
    print("Good Morning")


def test_crossbrowser(crossbrowser):
    print(crossbrowser[1])
