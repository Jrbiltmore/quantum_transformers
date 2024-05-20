import unittest
from src.hybrid_module import HybridModule

class TestHybridModule(unittest.TestCase):
    def setUp(self):
        self.hm = HybridModule()

    def test_hybrid_algorithm(self):
        try:
            self.hm.run_hybrid_algorithm()
        except Exception as e:
            self.fail(f"run_hybrid_algorithm() raised {e} unexpectedly")

if __name__ == "__main__":
    unittest.main()
# END