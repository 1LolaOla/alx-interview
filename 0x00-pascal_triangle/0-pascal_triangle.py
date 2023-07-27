#!/usr/bin/python3
"""Pascal's triangle"""


def pascal_triangle(a):
    """lists of integers 
    representing the Pascal’s triangle of a:
    """

    if a <= 0:
        return []

    
    """ initialize an empty resulting array """
    pascal = [[] for idx in range(a)]

    for li in range(a):
        for col in range(li+1):
            if(col < li):
                if(col == 0):
                    """ first column always set to 1 """
                    pascal[li].append(1)
                else:
                    pascal[li].append(pascal[li-1][col] + pascal[li-1][col-1])
            elif(col == li):
                """ diagonal always set to 1 """
                pascal[li].append(1)

    return pascal
