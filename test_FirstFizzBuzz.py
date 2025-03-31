from FirstFizzBuzz import FirstFizzBuzz
from FizzBuzzContractWithPyTest import FizzBuzzContractWithPyTest


class TestFirstFizzBuzz(FizzBuzzContractWithPyTest):

    def create_fizz_buzz(self):
        return FirstFizzBuzz()

