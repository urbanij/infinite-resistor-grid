## Infinite grid of resistors problem ([xkcd.com/356/](https://xkcd.com/356/))


[![](https://www.mbeckler.org/resistor_grid/nerd_sniping_s.png)](https://xkcd.com/356/)


## How to:

Install a CLI [SPICE](https://en.wikipedia.org/wiki/List_of_free_electronics_circuit_simulators) simulator such as [ngspice](http://ngspice.sourceforge.net/) or [MacSpice](https://www.macspice.com/) (which also happens to run twice as fast):

```bash
brew install ngspice
```
or
```bash
brew install --cask macspice
```

then compile this [Rust](https://www.rust-lang.org/tools/install) script that _parses_ spice outputs

```bash
rustc parse_ngspice_output.rs
```

then run this python script (~40 seconds with the current configuration) to get some results and generate the plots.
```bash
python run.py
```
If everything was a success you should have some `.svg` plots in your current directory.


If you want to get straight to a single figure you can just run this instead, passing a moderately big even number like 200

```bash
python infinite_grid.py 200 | ngspice
```

or 

```bash
ln -s /Applications/MacSpice.app/Contents/MacOS/MacSpice /usr/local/bin
python infinite_grid.py 200 | MacSpice
``` 

which, after processing a netlist of 79999 resistors, gives a `i(v1) = -1.29315e+00` output, meaning an equivalent resistance of 
`0.77330549433 Ω`.


![](https://github.com/urbanij/infinite-resistor-grid/blob/main/resistance_vs_grid_size.svg?raw=true)

---
btw [the mathematical result gives 4/π - 1/2](https://www.mathpages.com/home/kmath668/kmath668.htm).