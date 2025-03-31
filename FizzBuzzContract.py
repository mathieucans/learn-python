from abc import abstractmethod, ABC

import pytest


class FizzBuzzContract(ABC):

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

    def test_failed_base(self):
        assert self.create_fizz_buzz().say(1) == "fizz"
