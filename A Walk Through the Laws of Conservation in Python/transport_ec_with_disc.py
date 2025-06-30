import numpy as np
from matplotlib import pyplot as plt
import time, sys

N = 41
h = 2 / (N-1)
T = 25
k = 0.025
c = 1

u = np.ones(N)
u[int(.5/h):int(1/h+1)] = 2

plt.plot(np.linspace(0,2,N),u)

un = np.ones(N)

for n in range(T):
    un = u.copy()
    for i in range (1, N):
        u[i] = un[i] - c * k / h * (un[i] - un[i-1])

plt.plot(np.linspace(0,2,N),u)
plt.show()
