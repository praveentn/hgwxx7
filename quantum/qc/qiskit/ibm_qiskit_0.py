#!/usr/bin/env python
# coding: utf-8

# In[1]:


# load libraries

import qiskit
from qiskit import IBMQ


# In[2]:


IBMQ.save_account('my_api_goes_here')


# In[3]:


qiskit.__version__


# In[4]:


qiskit.__qiskit_version__


# In[5]:


import numpy as np
from qiskit import(
  QuantumCircuit,
  execute,
  Aer)
from qiskit.visualization import plot_histogram


# In[6]:


# Use Aer's qasm_simulator
simulator = Aer.get_backend('qasm_simulator')

simulator


# In[7]:


# Create a Quantum Circuit acting on the q register
circuit = QuantumCircuit(2, 2)

circuit


# In[8]:


# Add a H gate on qubit 0
circuit.h(0)

# Add a CX (CNOT) gate on control qubit 0 and target qubit 1
circuit.cx(0, 1)

# Map the quantum measurement to the classical bits
circuit.measure([0,1], [0,1])

circuit


# In[9]:


# Execute the circuit on the qasm simulator
job = execute(circuit, simulator, shots=1000)

# Grab results from the job
result = job.result()

# Returns counts
counts = result.get_counts(circuit)
print("\nTotal count for 00 and 11 are:",counts)

# Draw the circuit
circuit.draw()


# In[10]:


# Plot a histogram
plot_histogram(counts)


# In[ ]:




