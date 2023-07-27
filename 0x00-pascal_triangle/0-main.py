#!/usr/bin/python3
"""
0-main
"""
from 0-pascal_triangle import pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    triangle = pascal_triangle(5)
    print_triangle(triangle)