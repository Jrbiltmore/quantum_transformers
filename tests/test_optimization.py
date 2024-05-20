import unittest
import numpy as np
from src.optimization import classical_optimization

class TestOptimization(unittest.TestCase):
    def test_classical_optimization(self):
        try:
            data = np.random.rand(100)
            result = classical_optimization(data)
            self.assertIsNotNone(result)
        except Exception as e:
            self.fail(f"classical_optimization() raised {e} unexpectedly")

if __name__ == "__main__":
    unittest.main()
# END