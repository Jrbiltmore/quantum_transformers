import pennylane as qml

class QuantumModule:
    def __init__(self, config):
        """
        Initialize the quantum module with a PennyLane device and QNode.
        """
        try:
            self.dev = qml.device(config['device'], wires=config['wires'])
            self.qnode = qml.QNode(self.circuit, self.dev)
        except Exception as e:
            print(f"Failed to initialize QuantumModule: {e}")

    def circuit(self, x):
        """
        Define the quantum circuit.
        
        Args:
            x (float): Rotation angle for the CRX gate.
        
        Returns:
            float: Expectation value of PauliZ on the first qubit.
        """
        try:
            qml.Hadamard(wires=0)
            qml.CRX(x, wires=[0, 1])
            return qml.expval(qml.PauliZ(0))
        except Exception as e:
            print(f"Failed to execute circuit: {e}")

    def run_quantum_algorithm(self):
        """
        Run the quantum algorithm and return the result.
        
        Returns:
            float: Result of the quantum algorithm.
        """
        try:
            result = self.qnode(0.5)
            print(f"Quantum result: {result}")
            return result
        except Exception as e:
            print(f"Failed to run quantum algorithm: {e}")
            return None

# END