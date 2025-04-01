import unittest

from fizz_buzz.FirstFizzBuzz import FirstFizzBuzz
from fizz_buzz.unittest.FizzBuzzContractUnit import FizzBuzzContractUnit


class FirstFizzBuzzWithUnitTest(FizzBuzzContractUnit):
    def create(self):
        return FirstFizzBuzz()


if __name__ == '__main__':
    unittest.main()
