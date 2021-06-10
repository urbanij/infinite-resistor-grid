"""
* SImple voltage calc

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

out = f"* Infinite grid of resistors, N = {N}\n"


# put horizontal resistors in place
for i in range(N*N - 1):
    if (i+1) % N == 0:
        continue
    else:
        out += f"R{i}_{i+1} {i} {i+1} 1.0\n"

for i in range(N*N - 1):
    if (i+1) % N == 0:
        continue
    else:
        out += f"R{i}_{i+N} {i} {i+N} 1.0\n"


out += "\nV1 0 1 dc 1V\n"

out += """
.control
op
print all
.endc
"""

print(out)