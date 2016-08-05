# FCTRL2 - Small factorials
#
# You are asked to calculate factorials of some small positive integers.
#
# Input
#
# An integer t, 1<=t<=100, denoting the number of testcases, followed by t lines,
#  each containing a single integer n, 1<=n<=100.
#
# Output
#
# For each integer n given at input, display a line with the value of n!
#
# Example
#
# Sample input:
# 4
# 1
# 2
# 5
# 3
# Sample output:
# 1
# 2
# 120
# 6


function factorials(number) {
    n = 1
    while (number > 1) {
        n *= number--
    }
    return n
}

NR > 1 {print factorials($1)}
