import pytest


# passing the fixture to all method in the way of class
@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixturedemo1(self):
        print("I will execute steps in fixturedemo method")


    def test_fixturedemo2(self):
        print("I will execute steps in fixturedemo method")


    def test_fixturedemo(self):

        print("I will execute steps in fixturedemo method")


    def test_fixturedemo3(self):
        print("I will execute steps in fixturedemo method")
