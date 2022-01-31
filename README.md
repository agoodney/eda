# eda

tl;dr A collection of libraries available for use with KiCad 6 and some Python scripts to *generate* symbols programatically.

## Intro
The default paradigm for working with schematic symbols in KiCad (especially for simple parts like resistors and capacitors) is a 1:N mapping where one symbol is used for many different parts.

I do not grok this method, so as I started to explore KiCad 6 I needed a way to easily create symbol libraries with a 1:1 mapping between symbols and BOM parts.

For example I'd like to add an entire series of SMT resistors like the ERJ-6ENF series. After creating a template part I could have used a templating system or something similar to modify the template... or we could create them programatically!

I nerd-sniped myself into writing some Python that lets you create parts programatically and it is at the point where it can be shared.

KiCad 6 introduces file formats based on S-expressions, which are a tree-structured way to represent data using plain text. They are well known and used widely and there is a Python library that will turn nested lists into s-expressions (`sexpdata`).

We do depend on `sexpdata` so make sure to `pip install sexpdata` 

Then all that is required to create a symbol library is the following:

```python
import KiCadLib
import Templates

id = "TEMPLATE"
p = Templates.Resistor(id)
s = KiCadLib.SymbolLib(symbols=[p])
print(s.to_sexp())
```
This will create a KiCad 6 library with one resistor symbol named "TEMPLATE". If you save it to a file with the .kicad_sym extension you will be able to open it in KiCad 6 by adding it to your symbol libaries.

## Contributing
I am 100% interested in contributions, please submit PRs!

If you use this code to create a library, please consider adding the script that creates it to the scripts directory and the library to the libraries heirarchy.

### Things to work on:
- Importer so we can import existing symbols
- More templates
- Error check 'enum' like tokens that have a set of valid values (e.g. pin types, pin styles)
- Generate s-expressions natively so we don't depend on `sexpdata`
- Documentation

## Notes
I know I write ugly, imperitive style Python! You can help me fix it :-)

I haven't tested all of the graphic primitives.


