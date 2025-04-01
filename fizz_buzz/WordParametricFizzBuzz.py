from fizz_buzz.FizzBuzz import FizzBuzz


class Rule:
    def __init__(self, modulo, word):
        self.word = word
        self.modulo = modulo

    def match(self, number):
        return number % self.modulo == 0



class WordParametricFizzBuzz(FizzBuzz):

    def __init__(self):
        self.rules = [
            Rule(3, "fizz"),
            Rule(5, "buzz"),
        ]

    def say(self, number):
        word = ""
        for rule in self.rules:
            if rule.match(number):
                word += rule.word

        if word != "":
            return word

        return "{}".format(number)
