#!/bin/python3

import sys

def solve(a0, a1, a2, b0, b1, b2):
    arr = [a0, a1, a2]
    ar = [b0, b1, b2]
    alice = 0
    bob = 0

    for idx in range(0, len(arr)):
        if arr[idx] > ar[idx]:
            alice = alice + 1
        elif arr[idx] < ar[idx]:
            bob = bob + 1
        else:
            continue

    return alice, bob

a0, a1, a2 = input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print (" ".join(map(str, result)))
