# Write a function:
#
# def solution(A, B, K)
#
# that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:
#
# { i : A ≤ i ≤ B, i mod K = 0 }
#
# For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 with
# # in the range [6..11], namely 6, 8 and 10.
#
# Write an efficient algorithm for the following assumptions:
#
# A and B are integers within the range [0..2,000,000,000];
# K is an integer within the range [1..2,000,000,000];
# A ≤ B.

from math import ceil, floor


def solution(A, B, K): # a is the start of teh sequence, b is the end of teh sequence, a and b are inclusive
    n_start = ceil(A / K) # take top range when decimal given
    n_end = floor(B / K) # take bottom when given decimal
    return n_end - n_start + 1


print(solution(6, 11, 2))

print((4/3)-(17/3)+1)

