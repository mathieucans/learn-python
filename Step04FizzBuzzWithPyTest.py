import pytest

from FizzBuzz import FizzBuzz


class TestFizzBuzz:
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
        fizz_buzz = FizzBuzz()
        assert fizz_buzz.say(input) == expected


