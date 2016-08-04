"""
PALIN - The Next Palindrome

A positive integer is called a palindrome if its representation in the decimal
system is the same when read from left to right and from right to left. For a
given positive integer K of not more than 1000000 digits, write the value of
the smallest palindrome larger than K to output. Numbers are always displayed
without leading zeros.

Input

The first line contains integer t, the number of test cases. Integers K are
given in the next t lines.

Output

For each K, output the smallest palindrome larger than K.

Example

Input:
2
808
2133

Output:
818
2222
"""

import sys

def is_palindrome(number):
    number = str(number)
    length = len(number)
    if length % 2 == 0:
        i, j = length / 2 - 1, length / 2
    else:
        i, j = (length >> 1) - 1, (length >> 1) + 1
    while i >= 0:
        if number[i] == number[j]:
            i -= 1
            j += 1
        else:
            return False
    return True


lines = sys.stdin.readlines()
number_of_lines = int(lines[0])
for i in range(1, number_of_lines + 1):
    k = int(lines[i]) + 1
    while True:
        if is_palindrome(k):
            print(k)
            break
        else:
            k += 1
