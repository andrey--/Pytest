import pytest
from src.main.class_under_test import under_test

# def setup():
#     print("Setup")
#
#
# def teardown():
#     print("Teardown")


@pytest.fixture(scope="module")
def setup_one():
    asd = under_test()
    print ("Setup once")
    return asd


@pytest.mark.parametrize("aaa", {"55", "123", "sdf"})
def test_alfa(setup_one, aaa):

    assert setup_one.alfa(aaa)==" ".join(aaa)
    print ("Passed")

@pytest.mark.parametrize("aaa", {"55", "123", "sdf"})
def test_alfa1(setup_one, aaa):

    assert setup_one.alfa(aaa)==" ".join(aaa)
    print ("Passed1")