# Rain

`0-rain.py` contains `rain(walls)`, which calculates the amount of water
trapped between walls of unit width. The input is a list of non-negative
integer heights, and the result is an integer number of square units.

An empty list returns `0`. Water outside the first and last walls escapes.
The function does not change the input list and does not import any modules.

## How it works

Two positions start at opposite ends of the list. Move inward from the
shorter wall, keeping track of the tallest wall seen on each side. The
difference between that height and the current wall is the water trapped
at that position. Add these differences to get the total.

The solution takes O(n) time and O(1) extra space.

## Examples

From the `rain` directory:

```python
rain = __import__('0-rain').rain

print(rain([0, 1, 0, 2, 0, 3, 0, 4]))  # 6
print(rain([2, 0, 0, 4, 0, 0, 1, 0]))  # 6
print(rain([3, 0, 3]))                 # 3
print(rain([]))                        # 0
```

The solution is compatible with Python 3.4 and follows PEP 8 style.
