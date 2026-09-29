# Minimum Operations

Starting with one `H`, find the fewest `Copy All` and `Paste` operations
needed to reach exactly `n` characters.

`0-minoperations.py` provides `minOperations(n)`, which returns an integer.
It returns `0` for non-integer inputs or values less than or equal to `1`.
One character is already present, so `n = 1` needs no operations.

## How it works

Multiplying the current number of characters by `k` takes one copy and
`k - 1` pastes, costing `k` operations. Splitting composite factors into
prime factors gives the minimum total cost. The function adds these factors
as it divides `n`.

- `4 = 2 * 2`: `2 + 2 = 4` operations.
- `9 = 3 * 3`: `3 + 3 = 6` operations.
- `12 = 2 * 2 * 3`: `2 + 2 + 3 = 7` operations.

## Usage

From the `minimum_operations` directory:

```python
minOperations = __import__('0-minoperations').minOperations

print(minOperations(4))   # 4
print(minOperations(9))   # 6
print(minOperations(12))  # 7
```

The implementation uses Python 3.4-compatible syntax, takes at most
O(sqrt(n)) time, and uses O(1) extra space.
