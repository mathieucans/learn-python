import unittest

from FirstFizzBuzz import FirstFizzBuzz
from FizzBuzzContractUnit import FizzBuzzContractUnit


class FirstFizzBuzzWithUnitTest(FizzBuzzContractUnit):
    def create(self):
        return FirstFizzBuzz()


if __name__ == '__main__':
    unittest.main()
