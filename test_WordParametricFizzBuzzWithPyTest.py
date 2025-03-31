from FizzBuzzContract import FizzBuzzContract
from WordParametricFizzBuzz import WordParametricFizzBuzz


class TestWordParametricFizzBuzzWithPyTest(FizzBuzzContract):
    def create_fizz_buzz(self):
        return WordParametricFizzBuzz()



