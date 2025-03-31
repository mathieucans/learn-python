from FizzBuzz import FizzBuzz
from FizzBuzzContract import FizzBuzzContract

class WordParametricFizzBuzz(FizzBuzz):

    def say(self, number):
        return 'hop'


class TestWordParametricFizzBuzz(FizzBuzzContract):
    def create_fizz_buzz(self):
        return WordParametricFizzBuzz()



