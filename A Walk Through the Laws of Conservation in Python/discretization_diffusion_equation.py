import numpy as np
from matplotlib import pyplot as plt
import time, sys

N = 81
h = 2 / (N-1)
T = 25
k = 0.025
c = 1

u = np.ones(N)
u[int(.5/h):int(1/h+1)] = 2

plt.plot(np.linspace(0,2,N),u)

un = np.ones(N)

nu = 1.0
for n in range(T):
    un = u.copy()
    for i in range (1, N):
        u[i] = un[i] - 0.5* nu * (un[i]+un[i-1]) * k / h * (un[i] - un[i-1])

plt.plot(np.linspace(0,2,N),u)
plt.show()