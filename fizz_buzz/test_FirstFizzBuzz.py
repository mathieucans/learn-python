from fizz_buzz.FirstFizzBuzz import FirstFizzBuzz
from fizz_buzz.FizzBuzzContractWithPyTest import FizzBuzzContractWithPyTest


class TestFirstFizzBuzz(FizzBuzzContractWithPyTest):

    def create_fizz_buzz(self):
        return FirstFizzBuzz()

