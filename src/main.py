from quantum_module import QuantumModule
from classical_module import ClassicalModule
from hybrid_module import HybridModule
from visualization import plot_results
from optimization import classical_optimization
from config import load_config

def main():
    """
    Main function to run quantum, classical, and hybrid algorithms.
    """
    config = load_config()
    if not config:
        print("Failed to load configuration. Exiting.")
        return
    
    try:
        qm = QuantumModule(config['quantum'])
        cm = ClassicalModule(config['classical'])
        hm = HybridModule(qm, cm)

        quantum_result = qm.run_quantum_algorithm()
        classical_result = cm.run_classical_algorithm()
        hybrid_result = hm.run_hybrid_algorithm()

        optimized_result = classical_optimization(classical_result)

        results = {
            'Quantum': quantum_result,
            'Classical': classical_result,
            'Hybrid': hybrid_result,
            'Optimized': optimized_result
        }

        plot_results(results)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
# END