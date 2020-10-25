import unittest
from Calculator import Calculator


class MyTestCase(unittest.TestCase):

    def test_instantiate_Calculator(self):
        Calculator = 'Calculator'()
        self.assertIsInstance(Calculator, Calculator)

    def test_results_prpperty_Calculator(self):
        Calculator = 'Calculator'()
        self.assertEqual(Calculator.result, 4)

    def test_add_method_Calculator(self):
        Calculator = 'Calculator'()
        self.assertEqual(Calculator.add(2, 2),4)

if '_name_' == '_main_':
    unittest.main()
