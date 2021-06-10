import os

try:
    os.remove("res.txt")
except FileNotFoundError:
    pass

for i in range(118):
    if (i < 60 and i % 2 == 0) or (i >= 60 and i % 4 == 0):
        os.system(f"python infinite_grid.py {i} | ngspice | ./process >> res.txt")

