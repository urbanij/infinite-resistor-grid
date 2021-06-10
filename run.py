import os

try:
    os.remove("res.txt")
except FileNotFoundError:
    pass

num_rows = [i*2 for i in range(1, 20)] + [i*4 for i in range(20, 25)] + [120]

for i in num_rows:
    if (i < 60 and i % 2 == 0) or (i >= 60 and i % 4 == 0):
        os.system(f"python infinite_grid.py {i} | ngspice | ./process >> res.txt")




import matplotlib.pyplot as plt
import numpy as np

current = np.genfromtxt('res.txt')

n_to_resistors = lambda num_rows: (num_rows-1) * (num_rows+1) + (num_rows) * num_rows
num_total_resistors = list(map(n_to_resistors, num_rows))


plt.figure()
plt.plot(num_total_resistors, -current, label='# resistors vs current')
plt.legend()
plt.savefig("resistors_vs_current.svg", format='svg')

plt.figure()
plt.plot(num_total_resistors, -1.0/current, label='# resistors vs resistance')
plt.legend()
plt.savefig("resistors_vs_resistance.svg", format='svg')
