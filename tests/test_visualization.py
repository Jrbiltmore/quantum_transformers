import unittest
from src.visualization import plot_results

class TestVisualization(unittest.TestCase):
    def test_plot_results(self):
        try:
            results = {'Test': [1, 2, 3, 4, 5]}
            plot_results(results)
        except Exception as e:
            self.fail(f"plot_results() raised {e} unexpectedly")

if __name__ == "__main__":
    unittest.main()
# END