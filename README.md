## Infinite grid of resistors problem ([xkcd.com/356/](https://xkcd.com/356/))


[![](https://www.mbeckler.org/resistor_grid/nerd_sniping_s.png)](https://xkcd.com/356/)

### Example generated netlist
```spice
* Infinite grid of resistors, N = 2, M = 3

* Horizontal resistors
R0 6 1 1
R1 1 0 1
* ---
R2 3 4 1
R3 4 5 1
* Vertical resistors
* ---
R4 6 3 1
R5 1 4 1
R6 0 5 1

V1 3 0 dc 1V

.control
op
print i(v1)
* print all
.endc

* Grid size = 2x3
* # resistors = 7
```

`res.txt`
```text
-7.14286e-01
-1.06674e+00
-1.18177e+00
[...]
-1.29287e+00
-1.29290e+00
-1.29292e+00
```

### How to:
rustc process.rs -C opt-level=3
python run.py # it takes ~20 seconds or so with current configuration
