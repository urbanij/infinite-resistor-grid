## Infinite grid of resistors problem ([xkcd.com/356/](https://xkcd.com/356/))


[![](https://www.mbeckler.org/resistor_grid/nerd_sniping_s.png)](https://xkcd.com/356/)


## How to:

Install [ngspice](http://ngspice.sourceforge.net/) or any other [SPICE](https://en.wikipedia.org/wiki/List_of_free_electronics_circuit_simulators) simulator for that matter, e.g.
```
brew install ngspice
```
then compile this little script in [Rust](https://www.rust-lang.org/tools/install) that _parses_ ngspice outputs
```bash
rustc parse_ngspice_output.rs
```

then run it all with this python script which takes ~40 seconds or so with the current configuration
```bash
python run.py
```
If everything was a success you should have two `.svg` plots in your current directory.

If you want to get straight to a single figure you can just run this instead, passing a moderately big even number like 200

```bash
python infinite_grid.py 200 | ngspice
``` 

which, after processing a netlist of 79999 resistors, gives a `i(v1) = -1.29315e+00` output, meaning an equivalent resistance of 
`0.77330549433 Ω`.


![](https://github.com/urbanij/infinite-resistor-grid/blob/main/%23_resistors_vs_resistance.svg?raw=true)


<!-- 
### Example generated netlist
```spice
* Infinite grid of resistors* Grid size = 2x3; # resistors = 7

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
``` -->
