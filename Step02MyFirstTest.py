import unittest


class Step02MyFirstTest(unittest.TestCase):
    def test_that_fails(self):
        self.assertEqual(True, False)

    def test_that_succeeds(self):
        self.assertEqual(1,1)

    def test_multiple_assertions(self):
        self.assertEqual(2,2)
        self.assertEqual(5,5)
        self.assertGreater(6,3)

    def test_array_equality(self):
        self.assertCountEqual(["a", "b", "c"], ["a", "b", "c"])

    def test_order_differs_succeedd(self):
        self.assertCountEqual(["a", "c", "b"], ["a", "b", "c"])

    def test_missing_element_fails(self):
        self.assertCountEqual(["a",  "b"], ["a", "b", "c"])

if __name__ == '__main__':
    unittest.main()
