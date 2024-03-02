# Import necessary modules from Qiskit
from qiskit import QuantumCircuit, Aer, execute

# This example shows the basics of writing a quantum circuit
# Create a quantum circuit with 2 qubits and 2 classical bits
qc = QuantumCircuit(2, 2)

# Apply a Hadamard gate to the first qubit
qc.h(0)

# Apply a controlled-X gate (CNOT) with the first qubit as control and the second qubit as target
qc.cx(0, 1)

# Measure both qubits and store the results in classical bits
qc.measure([0, 1], [0, 1])

# Choose the simulator as the backend
backend = Aer.get_backend('qasm_simulator')

# Execute the circuit on the chosen backend
job = execute(qc, backend, shots=1000)

# Get the result of the execution
result = job.result()

# Print the counts of each measurement outcome
print(result.get_counts(qc))
