import pytest

from FizzBuzz import FirstFizzBuzz


class TestFizzBuzz:

    @classmethod
    def setup_method(self):
        self.fizz_buzz = FirstFizzBuzz()

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
        assert self.fizz_buzz.say(input) == expected
