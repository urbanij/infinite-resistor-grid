import sys

try:
    N = int(sys.argv[1])
    if N % 2 != 0: raise("Give me an even number")
    M = N + 1
except TypeError:
    raise("Give me an even number")

out  = f"* Infinite grid of resistors"
out += f"* Grid size = {N}x{M}; # resistors = { (N-1) * M + (M-1) * N }; # nodes = {N*M}\n\n"

resistor_count = 1

# add 1 Ohm horizontal resistors
out += "* Horizontal resistors\n"
for i in range(N*M - 1):
    if (i+1) % M == 0:
        out += "* ---\n"
    else:
        out += f"R{resistor_count} {i} {i+1} 1\n"
        resistor_count += 1

# add 1 Ohm vertical resistors
out += "* Vertical resistors\n"
for i in range(N*(M-1) - 1):
    if i % M == 0:
        out += "* ---\n"
    out += f"R{resistor_count} {i} {i+M} 1\n"
    resistor_count += 1


V_pos_row, V_pos_col = N//2,     N//2 - 1
V_neg_row, V_neg_col = N//2 - 1, N//2 + 1

V_pos = V_pos_row * M + V_pos_col
V_neg = V_neg_row * M + V_neg_col

out += f"""
V1 {V_pos} {V_neg} dc 1V"""

out += """
.control
op
print i(v1)

* equivalent resistance:
print -1.0/i(v1)
* print all
.endc"""


# since in SPICE 0 is ground we need to swap 2 node values.
# Node called 0 will be called V_neg at the end and vice versa.
TMP_NODE_VAL = f" TMP_NODE "
out = out.replace(' 0 ', TMP_NODE_VAL) \
         .replace(f" {V_neg} ", ' 0 ') \
         .replace(TMP_NODE_VAL, f" {V_neg} ")


assert resistor_count - 1 == ( (N-1)*M + (M-1)*N )

with open(f"grid_{N}.cir", "w") as f: f.write(out)

print(out)
