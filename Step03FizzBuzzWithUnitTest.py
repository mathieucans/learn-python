import unittest


def fizzbuzz(param):
    if param == 3:
        return "fizz"
    return "{}".format(param)


class StepO3FizzBuzzWithUnitTest(unittest.TestCase):
    def test_say_1_for_1(self):
        self.assertEqual( "1", fizzbuzz(1))
    def test_say_2_for_2(self):
        self.assertEqual( "2", fizzbuzz(2))
    def test_say_fizz_for_3(self):
        self.assertEqual( "fizz", fizzbuzz(3))



if __name__ == '__main__':
    unittest.main()
