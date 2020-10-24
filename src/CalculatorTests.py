import unittest
from Calculator import Calculator


class MyTestCase(unittest.TestCase):

    def test_instantiate_Calculator(self):
        Calculator = 'Calculator'()
        self.assertIsInstance(Calculator, Calculator)


if '_name_' == '_main_':
    unittest.main()
