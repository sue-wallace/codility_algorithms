# prefix is like

# 6,3,1,7,4,3
# prefixed it is like 0,6,9,10,17,21,24
# suffix is the reverse so 0, 3, 7, ,14, 15, 18, 24

# Passing cars

# A non-empty array A consisting of N integers is given. The consecutive elements of array A represent consecutive cars on a road.
#
# Array A contains only 0s and/or 1s:
#
# 0 represents a car traveling east,
# 1 represents a car traveling west.
# The goal is to count passing cars. We say that a pair of cars (P, Q), where 0 ≤ P < Q < N, is passing when P is traveling to the east and Q is traveling to the west.
#
# For example, consider array A such that:
#
#   A[0] = 0
#   A[1] = 1
#   A[2] = 0
#   A[3] = 1
#   A[4] = 1
# We have five pairs of passing cars: (0, 1), (0, 3), (0, 4), (2, 3), (2, 4).
#
# Write a function:
#
# def solution(A)
#
# that, given a non-empty array A of N integers, returns the number of pairs of passing cars.
#
# The function should return −1 if the number of pairs of passing cars exceeds 1,000,000,000.
#
# For example, given:
#
#   A[0] = 0
#   A[1] = 1
#   A[2] = 0
#   A[3] = 1
#   A[4] = 1
# the function should return 5, as explained above.
#
# Write an efficient algorithm for the following assumptions:
#
# N is an integer within the range [1..100,000];
# each element of array A is an integer that can have one of the following values: 0, 1.

# calculate the suffix  first


def solution(A): # the array to
    suffix_sum = [0] * (len(A) + 1) # create the suffix array, length or original array plus 1 (accounting for the 0)
    for i in range(len(A) - 1, -1, -1):
        suffix_sum[i] = A[i] + suffix_sum[i + 1]

    count = 0 #count the number of cars going in the opposite direction
    for i in range(len(A)):
        if A[i] == 0:
            count += suffix_sum[i] #if car is going east then update count
        if count > 1000000000: # if count is over 1 billion, return -1
            return -1

    return count #the total number of passing cars


print(solution([0, 1, 0, 1, 1]))