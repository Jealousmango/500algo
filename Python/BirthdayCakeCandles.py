#!/bin/python3

import sys

def birthdayCakeCandles(n, ar):
    # Store the largest number
    max = 0
    # Store number of candles of the same max height
    total = 0
    # Loop through the array
    for idx in range(0, len(ar)):
        # Check if current value is the largest value yet
        if ar[idx] > max:
            max = ar[idx]
            # Set, or reset the total
            total = 1
        elif ar[idx] == max:
            # Increment total if multiple max values are equal
            total = total + 1
        else:
            continue
    return total

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(n, ar)
print(result)