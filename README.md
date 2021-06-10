## Infinite grid of resistors problem ([xkcd.com/356/](https://xkcd.com/356/))


[![](https://www.mbeckler.org/resistor_grid/nerd_sniping_s.png)](https://xkcd.com/356/)


## How to:

Install ngspice<sup>1</sup> or any other SPICE<sup>2</sup> simulator for that matter, e.g.
```
brew install ngspice
```
then compile this little script in Rust<sup>2</sup> that _parses_ ngspice outputs
```bash
rustc process.rs -C opt-level=3
```

then run it all with this python script which takes ~20 seconds or so with the current configuration
```bash
python run.py
```
If everything was a success you should have 2 `.svg` plots in your current directory.

If you want to get straight to a single figure you can just run this instead, passing a moderately big even number like 170

```bash
python infinite_grid.py 170 | ngspice
``` 

which, after processing a netlist of 57799 resistors, gives a `i(v1) = -1.29310e+00` output, meaning an equivalent resistance of 
`0.77333539556 Ω`.


![](https://github.com/urbanij/infinite-resistor-grid/blob/main/resistors_vs_resistance.svg?raw=true)


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

---
1 http://ngspice.sourceforge.net/ <br>
2 https://en.wikipedia.org/wiki/List_of_free_electronics_circuit_simulators <br>
3 https://www.rust-lang.org/tools/install