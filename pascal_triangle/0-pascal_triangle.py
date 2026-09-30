#!/usr/bin/python3
"""Build Pascal's triangle as a list of integer rows."""


def pascal_triangle(n):
    """Return n rows of Pascal's triangle, or an empty list if n <= 0."""
    triangle = []

    for row_number in range(n):
        row = [1]
        if row_number > 0:
            previous = triangle[-1]
            for column in range(1, row_number):
                row.append(previous[column - 1] + previous[column])
            row.append(1)
        triangle.append(row)

    return triangle
