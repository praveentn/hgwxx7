# IBMQ QKD: BB84 and E91
This repository contains the code that can be used to simulate the **BB84** and **E91** protocol using IBMQ quasm simulator as well the actual hardware. 
The BB84 protocol can be simulated with and without repeaters too.

The folder contains three sub folders: *BB84*, *E91* and *BB84_with_repeaters*.
* The main focus of the *BB84* folder is to demonstrate the working of the protocol using the qasm simulator. It also demonstrates what will happen in someone tries to evesdrop/measures the superposion.
* The focus of the *E91* folder is to demonsrtate the working of the protocol using the simulator and its workings.
* The focus of the *BB84_with_repeater* folder is to show how the BB84 protocol reacts to repeaters and how error mitigation plays an important role. 
(The aim was to simulate the propogation of errors while transmitting the qubit from Alice to Bob via repeaters)
*The folder also contains our results and presentation.*

*Note : Inorder to run the code on the actual hardware, it has to be optimised and one can create a list of circuits so as to run all of them in one job.*

The references are mentioned in the pdf in the *BB84_with_repeater* folder.
