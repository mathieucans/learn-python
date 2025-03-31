from abc import ABC, abstractmethod
from unittest import TestCase

from parameterized import parameterized


class FizzBuzzContractUnit(TestCase, ABC):
    @parameterized.expand([
        ["say 1 for 1", 1, "1"],
        ["say 2 for 2", 2, "2"],
        ["say fizz for 3", 3, "fizz"],
        ["say 4 for 4", 4, "4"],
        ["say buzz for 5", 5, "buzz"],
        ["say fizz for 6", 6, "fizz"],
        ["say fizz for 9", 9, "fizz"],
        ["say buzz for 10", 10, "buzz"],
        ["say fizzbuzz for 15", 15, "fizzbuzz"],
    ])
    def test_fizz_buzz(self, name, a, expected):
        self.assertEqual(expected, self.create().say(a))

    @abstractmethod
    def create(self):
        """return the FizzBuzz implementation"""
