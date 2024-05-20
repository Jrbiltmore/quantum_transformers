import matplotlib.pyplot as plt
import numpy as np

def plot_results(results):
    """
    Plot the results using matplotlib.

    Args:
        results (dict): Dictionary of results to plot.
    """
    try:
        for label, data in results.items():
            plt.plot(data, label=label)
        plt.legend()
        plt.xlabel('Iteration')
        plt.ylabel('Value')
        plt.title('Algorithm Results')
        plt.show()
    except Exception as e:
        print(f"Failed to plot results: {e}")

# END