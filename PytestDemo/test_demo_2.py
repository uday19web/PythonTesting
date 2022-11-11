# Any pytest file should start with "test_" or end with test
# Pytest method names should start with "test"
# Any code should be wrapped with method only

'''In the pytest standard we have to the write th code in "def" function only
in Pytest this function are called methods. the name of the method starts with "test" always
In pytest every method is consider as a Test Cases'''
import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_firstprogram():
    msg = "hello"
    # after the "hi" string will not print the condition is True.
    assert msg == "hi", "Test failed because strings do not match"


def test_secondcreditcard():
    a = 4
    b = 6
    assert a + 2 == b, "Addition do not match"
