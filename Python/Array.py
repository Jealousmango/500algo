#!/bin/python3

import sys

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
tempArr = []
str1 = ""

for i in reversed(arr):
    str1 += "%i " % i

print("%s " % str1)