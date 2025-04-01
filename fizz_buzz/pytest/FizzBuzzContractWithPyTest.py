from abc import abstractmethod, ABC
from assertpy import assert_that
import pytest


class FizzBuzzContractWithPyTest(ABC):

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
        assert_that(self.create_fizz_buzz().say(input)).is_equal_to(expected)
