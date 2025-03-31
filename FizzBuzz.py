from abc import abstractmethod


class FizzBuzz:
    @abstractmethod
    def say(self, number):
        pass


class FirstFizzBuzz(FizzBuzz):
    def say(self, number):
        if number % 5 == 0:
            return "buzz"
        if number % 3 == 0:
            return "fizz"
        return "{}".format(number)
