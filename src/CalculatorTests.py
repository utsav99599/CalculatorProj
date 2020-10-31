import unittest
from Calculator import Calculator
from CsvReader import CsvReader


class MyTestCase(unittest.TestCase):

    def test_instantiate_Calculator(self):
        Calculator = 'Calculator'();
        self.assertIsInstance(Calculator, Calculator)

    def test_results_property_Calculator(self):
        Calculator = 'Calculator'();
        self.assertEqual(Calculator.result, 4)

    def test_add_method_Calculator(self):
        Calculator = 'Calculator'();
        test_input = CsvReader('/src/Unit Test Addition.csv').data
        for row in test_input:
            self.assertEqual(Calculator.add(row['Value 1'], row['Value 2']),int(row['Result']))

    def test_sub_calculator(self):
        Calculator = 'Calculator'();
        test_input = CsvReader('/src/Unit Test Subtraction.csv').data
        for row in test_input:
            self.assertEqual(Calculator.sub(row['Value 1'], row['Value 2']), int(row['Result']))

    def test_mul_calculator(self):
        Calculator = 'Calculator'();
        test_input = CsvReader('/src/Unit Test Multiplication.csv').data
        for row in test_input:
            self.assertEqual(Calculator.mul(row['Value 1'], row['Value 2']), int(row['Result']))

    def test_div_calculator(self):
        Calculator = 'Calculator'();
        test_input = CsvReader('/src/Unit Test Division.csv').data
        for row in test_input:
            self.assertEqual(Calculator.div(row['Value 1'], row['Value 2']), float(row['Result']))

    def test_sq_calculator(self):
        test_input = CsvReader('/src/Unit Test Square.csv').data
        for row in test_input:
            self.assertEqual(Calculator.sq(row['Value 1']), int(row['Result']))

    def test_sqroot_calculator(self):
        test_input = CsvReader('/src/Unit Test Square Root.csv').data
        for row in test_input:
            result = round(Calculator.sqroot(int(row['Value 1'])), 8)
            self.assertEqual(result, round(float(row['Result']), 8))

if '_name_' == '_main_':
    unittest.main()
