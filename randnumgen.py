import qiskit as q
from qiskit import QuantumCircuit, execute, Aer
import numpy as np
import cmath
def randbool(): 
    qc = QuantumCircuit(1,1)
    qc.h(0)
    qc.measure(0,0)
    be = Aer.get_backend('statevector_simulator')
    jobs = execute(qc,be, shots = 1)
    results = jobs.result()
    qcm = results.get_statevector()
    return(qcm[0].real)
 
def randnum(n):
    sum = 0 
    i = 0 
    while sum < pow(10,n):
        qcm = randbool()
        rand = (pow(2,i)*qcm)
        temp = sum + rand
        if pow(10,(n-1)) < temp < pow(10,n):
            flag = randbool()
            if flag :
                sum = temp
                break
        elif sum < pow(10,(n-1)) and temp > pow(10,n):
            i = 1
            rand = (pow(2,i))*qcm
            sum = sum + rand
            i = i + 1
        else:
            sum = sum + rand
            i = i + 1
    return(sum) 
def randrange(ll,ul):
    sum = 0 
    i = 0 
    while sum < ul:
        qcm = randbool()
        rand = (pow(2,i)*qcm)
        temp = sum + rand
        if ll < temp < ul:
            flag = randbool()
            if flag :
                sum = temp
                break
        elif sum < ll and temp > ul:
            i = 1
            rand = (pow(2,i))*qcm
            sum = sum + rand
            i = i + 1
        else:
            sum = sum + rand
            i = i + 1
    return(sum) 
  
