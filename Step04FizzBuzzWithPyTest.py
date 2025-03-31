import pytest


class FizzBuzz:
    def say(self, number):
        if number % 5 == 0:
            return "buzz"
        if number % 3 == 0:
            return "fizz"
        return "{}".format(number)


def fizzbuzz(number):
    fizz_buzz = FizzBuzz()
    return fizz_buzz.say(number)

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
        assert fizzbuzz(input) == expected


