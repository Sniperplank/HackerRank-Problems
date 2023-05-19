# Probelm Description
"""
Given an array of integers, where all elements but one occur twice, find the unique element.
"""

# Output Examples
"""
a = [1, 2, 3, 4, 3, 2, 1]
The unique element is 4.
"""

# Problem Solution

def lonelyinteger(a):
    count = {}
    for i in a:
        count[i] = 1 + count.get(i, 0)
    return [x for x, v in count.items() if v == 1][0]
