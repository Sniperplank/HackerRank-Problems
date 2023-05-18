# Probelm Description
"""
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with 6 places after the decimal.
"""

# Output Examples
"""
Sample Input

STDIN           Function
-----           --------
6               arr[] size n = 6
-4 3 -9 0 4 1   arr = [-4, 3, -9, 0, 4, 1]
Sample Output

0.500000
0.333333
0.166667
"""

# Problem Solution

def plusMinus(arr):
    hashmap = {}
    for i in arr:
        if i < 0:
            hashmap['neg'] = 1 + hashmap.get('neg', 0)
        elif i == 0:
            hashmap['zero'] = 1 + hashmap.get('zero', 0)
        else:
            hashmap['pos'] = 1 + hashmap.get('pos', 0)
    negRatio = hashmap.get('neg', 0) / len(arr)
    zeroRatio = hashmap.get('zero', 0) / len(arr)
    posRatio = hashmap.get('pos', 0) / len(arr)
    print(f'{posRatio:.6f}')
    print(f'{negRatio:.6f}')
    print(f'{zeroRatio:.6f}')
