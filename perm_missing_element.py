# An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.
#
# Your goal is to find that missing element.
#
# Write a function:
#
# def solution(A)
#
# that, given an array A, returns the value of the missing element.
#
# For example, given array A such that:
#
#   A[0] = 2
#   A[1] = 3
#   A[2] = 1
#   A[3] = 5
# the function should return 4, as it is the missing element.
#
# Write an efficient algorithm for the following assumptions:
#
# N is an integer within the range [0..100,000];
# the elements of A are all distinct;
# each element of array A is an integer within the range [1..(N + 1)].

# Execution:
# Sum all elements that should be in the list and sum all elements that actually are in the list. The sum is 0 based,
# so +1 is required. The first solution using the + operator can cause int overflow
# in not-python languages. Therefore the use of a binary XOR is adequate.

# codemity 100% answer from martin K

# https://www.martinkysel.com/codility-permmissingelem-solution/

def solution(A):
    missing_element = len(A) + 1

    for idx, value in enumerate(A):
        missing_element = missing_element ^ value ^ (idx + 1)

    return missing_element

array = [1,2,4,5]

# udemy answer

# https://github.com/cutajarj/CodilityInPython/blob/master/solutions/timecomplexity/perm_missing_elem.py

def udemy_solution(A):
    actual_sum = 0 # actual sum
    for number in A: #this will sum the input and put it into actual_sumthat, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
        actual_sum += number
    max_number = len(A) + 1 # what we are expecting from the sum
    expected_sum = (max_number * (max_number + 1) // 2)
    return expected_sum - actual_sum

print(udemy_solution([2, 3, 1, 5]))

