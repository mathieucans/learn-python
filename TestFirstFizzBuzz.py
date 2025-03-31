from FirstFizzBuzz import FirstFizzBuzz
from FizzBuzzContract import FizzBuzzContract


class TestFirstFizzBuzz(FizzBuzzContract):

    def create_fizz_buzz(self):
        return FirstFizzBuzz()

    @classmethod
    def setup_method(self):
        self.fizz_buzz = FirstFizzBuzz()
