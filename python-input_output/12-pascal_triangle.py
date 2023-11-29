#!/usr/bin/python3
"""Pascal triangle."""


def pascal_triangle(n):
    """Pascal triangle Method."""
    empty_list = []
    if n <= 0:
        return empty_list
    p_triangle = [
        [1],
        [1, 1],
        [1, 2, 1],
        [1, 3, 3, 1],
        [1, 4, 6, 4, 1]
    ]
    for idx in range(1, n +1):
        empty_list.append(p_triangle[idx - 1])
    return empty_list
