import pytest


# define the "Fixture"
# scope = "class" - is used to run the pre requitis and tear down run only one time in multiple test case
@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    # after yield keyword below line execute after the test case ran
    yield
    print("I will execute last")


@pytest.fixture()
def dataload():
    print("User profile data is being created")
    return ["Rahul", "Shetty", "rahulshettyacademy.com"]


@pytest.fixture(params=[('chrome', 'Rahul', 'shetty'), ('Firefox', 'Rahul'), 'IE'])
def crossbrowser(request):
    return request.param

