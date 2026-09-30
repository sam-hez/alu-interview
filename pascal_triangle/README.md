# Pascal's Triangle

`0-pascal_triangle.py` provides `pascal_triangle(n)`, which returns the first
`n` rows of Pascal's triangle as a list of lists of integers. It returns an
empty list when `n` is zero or negative.

## How it works

The first row is `[1]`. Each following row starts and ends with `1`.
Each number between the ends is the sum of the two numbers above it in
the previous row. A new list is created for every row.

## Example

From the `pascal_triangle` directory:

```python
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

for row in pascal_triangle(5):
    print(row)
```

Output:

```text
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
```

The solution builds O(n squared) entries and stores them in the returned
triangle. It uses no imports.
