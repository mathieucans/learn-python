from fizz_buzz.WordParametricFizzBuzz import WordParametricFizzBuzz
from fizz_buzz.pytest.FizzBuzzContractWithPyTest import FizzBuzzContractWithPyTest


class TestWordParametricFizzBuzzWithPyTest(FizzBuzzContractWithPyTest):
    def create_fizz_buzz(self):
        return WordParametricFizzBuzz()





