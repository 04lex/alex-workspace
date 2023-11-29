import unittest
from number_division import division

class TestDivision(unittest.TestCase):
    def test_zero_division_error(self):
        with self.assertRaises(ZeroDivisionError):
            result = division(10, 0)
    
    def test_number_string(self):
        with self.assertRaises(TypeError):
            result = division(10, "zece")




if __name__ == "__main__":
    unittest.main()