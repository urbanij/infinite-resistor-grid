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


out = f"* Infinite grid of resistors, N = {N}, M = {M}\n\n"

resistor_number = 0

# put horizontal resistors in place
out += "* Horizontal resistors\n"
for i in range(N*M - 1):
    if (i+1) % M == 0:
        # continue
        out += "* ---\n"
    else:
        out += f"R{resistor_number} {i} {i+1} 1\n" # 1 means 1 Ohm
        resistor_number += 1

# put vertical resistors in place
out += "* Vertical resistors\n"
for i in range(N*(M-1) - 1):
    if i % M == 0:
        out += "* ---\n"
    out += f"R{resistor_number} {i} {i+M} 1\n" # 1 means 1 Ohm
    resistor_number += 1


V_pos_row, V_pos_col = N//2,     N//2 - 1
V_neg_row, V_neg_col = N//2 - 1, N//2 + 1

# print(V_pos_row, V_pos_col)
# print(V_neg_row, V_neg_col)

V_pos = (V_pos_row) * M + V_pos_col
V_neg = (V_neg_row) * M + V_neg_col

# print(V_pos, V_neg)

out += f"\nV1 {V_pos} {V_neg} dc 1V\n"

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


# since in SPICE 0 is ground we need to do a trick:
# out = out.replace(' 0 ', f" {N*M} ")
# out = out.replace(f" {V_neg} ", ' 0 ')


assert resistor_number == ( (N-1) * M + (M-1) * N )

with open("infinite_grid.cir", "w") as f: f.write(out)

# print(out)
