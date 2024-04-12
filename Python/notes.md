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