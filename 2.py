"""
PRIME1 - Prime Generator

Peter wants to generate some prime numbers for his cryptosystem. Help him!
Your task is to generate all prime numbers between two given numbers!

Input

The input begins with the number t of test cases in a single line (t<=10).
In each of the next t lines there are two numbers m and
n (1 <= m <= n <= 1000000000, n-m<=100000) separated by a space.

Output

For every test case print all prime numbers p such that m <= p <= n,
one number per line, test cases separated by an empty line.

Example

Input:
2
1 10
3 5

Output:
2
3
5
7

3
5
Warning: large Input/Output data, be careful with certain languages
(though most should be OK if the algorithm is well designed)
"""

import math
import sys
from collections import defaultdict


def print_primes_between_start_and_end(start, end):
    primes = defaultdict(lambda: 1)
    for p in range(2, int(math.sqrt(end)) + 1):
        if primes[p] == 1:
            i = p << 1
            while i <= end:
                primes[i] = 0
                i += p

    for k in range(start, end + 1):
        if primes[k] == 1:
            if k >= 2:
                print(k)


lines = sys.stdin.readlines()
number_of_lines = int(lines[0])

for i in range(1, number_of_lines + 1):
    m, n = lines[i].split()
    print_primes_between_start_and_end(int(m), int(n))
    print()
