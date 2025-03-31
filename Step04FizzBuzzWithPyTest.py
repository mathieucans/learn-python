from abc import abstractmethod

import pytest

from FizzBuzz import FirstFizzBuzz, FizzBuzz


class FizzBuzzContract:

    @abstractmethod
    def create_fizz_buzz(self):
        pass

    @pytest.mark.parametrize("input, expected", [
        (1, "1"),
        (2, "2"),
        (3, "fizz"),
        (4, "4"),
        (5, "buzz"),
        (6, "fizz"),
        (9, "fizz"),
        (10, "buzz"),
    ])
    def test_fizz_buzz(self, input, expected):
        assert self.create_fizz_buzz().say(input) == expected

class TestFizzBuzz(FizzBuzzContract):

    def create_fizz_buzz(self):
        return FirstFizzBuzz()

    @classmethod
    def setup_method(self):
        self.fizz_buzz = FirstFizzBuzz()
