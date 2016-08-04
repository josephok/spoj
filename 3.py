"""
ONP - Transform the Expression

Transform the algebraic expression with brackets into RPN form
(Reverse Polish Notation). Two-argument operators: +, -, *, /, ^
(priority from the lowest to the highest), brackets ( ). Operands:
only letters: a,b,...,z. Assume that there is only one RPN form
(no expressions like a*b*c).

Input

t [the number of expressions <= 100]
expression [length <= 400]
[other expressions]
Text grouped in [ ] does not appear in the input file.

Output

The expressions in RPN form, one per line.
Example

Input:
3
(a+(b*c))
((a+b)*(z+x))
((a+t)*((b+(a+c))^(c+d)))

Output:
abc*+
ab+zx+*
at+bac++cd+^*
"""

import sys

lines = sys.stdin.readlines()
number_of_lines = int(lines[0])
operators = ('+', '-', '*', '/', '^')
operators_stack = []


for i in range(1, number_of_lines + 1):
     output = ""
     for c in lines[i]:
         if c in operators:
             operators_stack.append(c)
         elif c == ")":
             output += operators_stack.pop()
         elif c == "(" or c == "\n":
             pass
         else:
             output += c
     print(output)
