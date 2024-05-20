import unittest
from src.quantum_module import QuantumModule

class TestQuantumModule(unittest.TestCase):
    def setUp(self):
        self.qm = QuantumModule()

    def test_quantum_algorithm(self):
        try:
            self.qm.run_quantum_algorithm()
        except Exception as e:
            self.fail(f"run_quantum_algorithm() raised {e} unexpectedly")

if __name__ == "__main__":
    unittest.main()
# END