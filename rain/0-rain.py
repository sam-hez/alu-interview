#!/usr/bin/python3
"""Calculate how much rainwater a row of walls can retain."""


def rain(walls):
    """Return the trapped water using the tallest walls on each side."""
    left = 0
    right = len(walls) - 1
    left_max = 0
    right_max = 0
    water = 0

    while left < right:
        if walls[left] <= walls[right]:
            left_max = max(left_max, walls[left])
            water += left_max - walls[left]
            left += 1
        else:
            right_max = max(right_max, walls[right])
            water += right_max - walls[right]
            right -= 1

    return water
