import unittest
from src.classical_module import ClassicalModule

class TestClassicalModule(unittest.TestCase):
    def setUp(self):
        self.cm = ClassicalModule()

    def test_classical_algorithm(self):
        try:
            self.cm.run_classical_algorithm()
        except Exception as e:
            self.fail(f"run_classical_algorithm() raised {e} unexpectedly")

if __name__ == "__main__":
    unittest.main()
# END