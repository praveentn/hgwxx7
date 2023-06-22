# load libraries
import numpy as np
from qiskit.circuit import QuantumCircuit
from qiskit.opflow import MatrixOp, StateFn

# let's first define a projector via the matrix you specified above
matrix = np.zeros((4,4))
matrix[1:3, 1:3] = np.array([[1, -1], [-1, 1]]) /2
proj = MatrixOp(matrix)

# and now a state (given as a circuit) that we want to project
circuit = QuantumCircuit(2)
circuit.ry(0.2, 0)
circuit.ry(0.3, 1)

# then just evaluate the result
result = (StateFn(proj, is_measurement=True) @ StateFn(circuit)).eval()
print(result)
# (0.001248958680493557+0j)

# convert matrix to sums of Paulis
print(proj.to_pauli_op())  
# SummedOp([
#   0.25 * II,
#   -0.25 * XX,
#   -0.25 * YY,
#   -0.25 * ZZ
# ]) 
