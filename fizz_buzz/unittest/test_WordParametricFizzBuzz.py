from fizz_buzz.WordParametricFizzBuzz import WordParametricFizzBuzz
from fizz_buzz.unittest.FizzBuzzContractUnit import FizzBuzzContractUnit


class TestWordParametricFizzBuzz(FizzBuzzContractUnit):
    def create(self):
        return WordParametricFizzBuzz()
