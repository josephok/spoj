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

from math import sqrt
primes = [2]

for i in range(3,32000,2):
    isprime = True

    cap = sqrt(i)+1

    for j in primes:
        if (j >= cap):
            break
        if (i % j == 0):
            isprime = False
            break
    if (isprime):
        primes.append(i)

T = int(input())
output = ""
for t in range(T):
    if (t > 0):
        output += "\n"

    M, N = input().split(' ')
    M = int(M)
    N = int(N)
    cap = sqrt(N) + 1

    if (M < 2):
        M = 2

    isprime = [True] * 100001

    for i in primes:
        if (i >= cap):
            break

        if (i >= M):
            start = i * 2
        else:
            start = M + ((i - M % i) % i)

        # The two below, obscure lines create a continuous
        #  block of false elements in order to set all
        #  elements correspnding to numbers divisible by i
        #  in isprime to be false
        # In turns out that this runs substantially faster
        #  than setting the elements individually using loops
        falseblock = [False] * len(isprime[start-M:N+1-M:i])
        isprime[start-M:N+1-M:i] = falseblock

    for i in range(M,N+1):
        if (isprime[i-M] == True):
            output += str(i) + "\n"

print(output[:-1])
