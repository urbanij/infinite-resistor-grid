"""
V1 0 1 dc 1V
R1 1 0 1.0 

.control
op
print all
.endc

* ngspice 33 -> simple_resistor.cir
* ngspice 33 -> op
* ngspice 33 -> print i(v1)
"""

import sys

N = int(sys.argv[1])
if N % 2 != 0: raise("Give me an even number")
M = N + 1


out = f"* Infinite grid of resistors, N = {N}, M = {M}\n"

# put horizontal resistors in place
resistor_number = 0

for i in range(N*M - 1):
    if (i+1) % M == 0:
        continue
    else:
        out += f"R{resistor_number} {i} {i+1} 1.0\n"
        resistor_number += 1

# put vertical resistors in place
for i in range(N*M - 1):
    if (i+1) % N == 0:
        continue
    else:
        out += f"R{resistor_number} {i} {i+M} 1.0\n"
        resistor_number += 1


Vx = 11
Vy = 8

out += f"\nV1 {Vx} {Vy} dc 1V\n"

out += """
.control
op
print i(v1)
* print all
.endc
\n"""

# add some commentary at the end of the file
out += f"* Grid size = {N} * {M}\n"
out += f"* # resistors = {resistor_number}\n"


assert resistor_number == ( (N-1) * M + (M-1) * N )

with open("infinite_grid.cir", "w") as f: f.write(out)

print(out)
