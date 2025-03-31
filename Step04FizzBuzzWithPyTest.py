import pytest

def fizzbuzz(param):
    if param == 3:
        return "fizz"
    return "{}".format(param)

class TestFizzBuzz:
    def test_one_for_one(self):
        assert fizzbuzz(1) == "1"

    def test_two_for_two(self):
        assert fizzbuzz(2) == "2"

    def test_fizz_for_three(self):
        assert fizzbuzz(3) == "fizz"


