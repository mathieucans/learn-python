import pytest

from FirstFizzBuzz import FirstFizzBuzz

@pytest.fixture
def create_fizz_buzz():
    return FirstFizzBuzz()

class TestFizzBuzz:
    def test_one_for_one(self, create_fizz_buzz):
        fizz_buzz = create_fizz_buzz
        assert fizz_buzz.say(1) == "1"

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
    def test_fizz_buzz(self, input, expected, create_fizz_buzz):
        assert create_fizz_buzz.say(input) == expected
