from FizzBuzzContract import FizzBuzzContract
from WordParametricFizzBuzz import WordParametricFizzBuzz


class TestWordParametricFizzBuzzWithPyTest(FizzBuzzContract):
    def create_fizz_buzz(self):
        return WordParametricFizzBuzz()

    def test_failed_with_details(self):
        assert self.create_fizz_buzz().say(3) == "3"




