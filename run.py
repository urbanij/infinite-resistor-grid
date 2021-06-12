import os


num_rows = [i*2 for i in range(1, 21)] + [60, 170]


if 1:
    try:
        os.remove("res.txt")
    except FileNotFoundError:
        pass

    for i in num_rows:
        os.system(f"python infinite_grid.py {i} | ngspice | ./parse_ngspice_output >> res.txt")



import matplotlib.pyplot as plt
import numpy as np

current = np.genfromtxt('res.txt')

n_to_resistors = lambda num_rows: (num_rows-1) * (num_rows+1) + (num_rows) * num_rows
num_total_resistors = list(map(n_to_resistors, num_rows))

def plot(x, y, label):
    plt.figure()
    plt.plot(x, y, label=label)
    plt.plot(x, y, "x")
    plt.legend()
    plt.xlabel(label.split('vs')[1])
    plt.ylabel(label.split('vs')[0])
    plt.grid()
    plt.savefig(f"{label.replace(' ', '_')}.svg", format='svg')


plot(num_total_resistors, 
    -current, 
    label="current vs # resistors")

plot(num_total_resistors, 
    -1.0/current, 
    label="resistance vs # resistors")

plot(num_rows, 
    -1.0/current, 
    label="resistance vs grid size")