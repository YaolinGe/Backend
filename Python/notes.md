# Notes for Python from Meta backend course

## Data structures 
- `list = [1, "hello", True, [1, 2, 3], 4.5]`, can contain any type of data
- `tuple = (1, "hello", True, [1, 2, 3], 4.5)`, immutable
- `set_a.union(set_b)` to get the union elements that exist in both set_a and set_b
- `set_a | set_b` to get the same union results. 
- `set_a.intersection(set_b)` to get the intersection elements that exist in both set_a and set_b
- `set_a & set_b` to get the same intersection results.
- `set_a.difference(set_b)` to get the difference elements that exist in set_a but not in set_b
- `set_a - set_b` to get the same difference results.
- `set_a.symmetric_difference(set_b)` to get the symmetric difference elements that exist in set_a and set_b but not in both
- `set_a ^ set_b` to get the same symmetric difference results.
- `print(f"{selection}. {menu[selection]['name'] : <9} | {menu[selection]['price'] : >5}")` to print a formatted string with left and right alignment

## Functional programming 
- `map()` function applies a given function to all items in an input list
- `filter()` function creates a list of elements for which a function returns true
- `comprehensions` are a concise way to create lists, dictionaries, and sets

## Modules
- `LEGB` rule: Local, Enclosing, Global, Built-in.
- `reload` function to reload a module, it is an interesting concept to be able to dynamically reload new changes in a module.
- `python -m pytest test_module.py::test_function` to run a specific test function in a test module.
