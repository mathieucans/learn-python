import pytest

from fizz_buzz.FizzBuzzContractWithPyTest import FizzBuzzContractWithPyTest
from WordParametricFizzBuzz import WordParametricFizzBuzz


class TestWordParametricFizzBuzzWithPyTest(FizzBuzzContractWithPyTest):
    def create_fizz_buzz(self):
        return WordParametricFizzBuzz()

@pytest.mark.skip('uncomment to show that actual value is no more displayed in inherited classes')
def test_failed_with_details(self):
        assert self.create_fizz_buzz().say(3) == "3"




