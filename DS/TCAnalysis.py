#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np

n=np.linspace(9.9, 10)
logn=np.log2(n)

plt.plot(n,n,color='#149c36',label='$n$')
plt.plot(n,logn,color='#000',label='$logn$')
plt.plot(n,n**.5,color="#168fb8",label='$\sqrt{n}$')
plt.plot(n,n*logn,color="#6b1b94",label="$nlogn$")
plt.plot(n,n**2,color='#d63c09',label='$n^2$')
plt.plot(n,n**3,color="#b39814",label="$n^3$")
plt.plot(n,2**n,color="#101887",label='$2^n$')
plt.title("Graph plots of various TC's")
plt.xlabel("$Input Size - (n)$")
plt.ylabel("$Time Complexity - (T(n))$")
plt.legend(loc="upper left")
plt.show()
