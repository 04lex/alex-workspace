import unittest
from fibonacci import *

# fibonacci(0) = 1 
# fibonacci(1) = 1 
# fibonacci(2) = 2 
# fibonacci(3) = 3 
# fibonacci(4) = 5 
# fibonacci(5) = 8 
# fibonacci(6) = 13 
# fibonacci(7) = 21

# asta trebuie sa returneze codul

### TESTARE / QA

class TestFibonacci(unittest.TestCase):
    def test_fibonacci(self):
        for fibonacci in (fibonacci_v1, fibonacci_v2):
            self.assertEqual(fibonacci(0), 1 )
            self.assertEqual(fibonacci(1), 1 )
            self.assertEqual(fibonacci(2), 2 )
            self.assertEqual(fibonacci(3), 3 )
            self.assertEqual(fibonacci(4), 5 )
            self.assertEqual(fibonacci(5), 8 )
            self.assertEqual(fibonacci(6), 13 )
            self.assertEqual(fibonacci(20), 10946 )

    def test_fibonacci_valori_negative(self):
        # Cand este chemat cu valoare negativa, apare exceptie ValueError codata in main.
        for fibonacci in (fibonacci_v1, fibonacci_v2):
            self.assertRaises(ValueError, fibonacci, -1)
            self.assertRaises(ValueError, fibonacci, -2)
            self.assertRaises(ValueError, fibonacci, -3)


if __name__ == "__main__":
    unittest.main()