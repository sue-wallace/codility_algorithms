# A non-empty array A consisting of N integers is given. Array A represents numbers on a tape.
#
# Any integer P, such that 0 < P < N, splits this tape into two non-empty parts: A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1].
#
# The difference between the two parts is the value of: |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|
#
# In other words, it is the absolute difference between the sum of the first part and the sum of the second part.
#
# For example, consider array A such that:
#
#   A[0] = 3
#   A[1] = 1
#   A[2] = 2
#   A[3] = 4
#   A[4] = 3
# We can split this tape in four places:
#
# P = 1, difference = |3 − 10| = 7
# P = 2, difference = |4 − 9| = 5
# P = 3, difference = |6 − 7| = 1
# P = 4, difference = |10 − 3| = 7
# Write a function:
#
# def solution(A)
#
# that, given a non-empty array A of N integers, returns the minimal difference that can be achieved.
#
# For example, given:
#
#   A[0] = 3
#   A[1] = 1
#   A[2] = 2
#   A[3] = 4
#   A[4] = 3
# the function should return 1, as explained above.
#
# Write an efficient algorithm for the following assumptions:
#
# N is an integer within the range [2..100,000];
# each element of array A is an integer within the range [−1,000..1,000].

# udemy

def solution(A):
    sum_left = A[0] # the sum on the left side of the array (val of 1st ent in array)
    sum_right = sum(A) - A[0] # the sum of the whole array minus the value of the 1st array
    diff = abs(sum_left - sum_right) # the absolute difference of the two
    for i in range(1, len(A)-1): # the for loop takes the sum left and right and adds/subtracts the next item in the array
        sum_left += A[i]
        sum_right -= A[i]
        current_diff = abs(sum_left - sum_right) # then gives the difference between
        if diff > current_diff: # if difference is smaller, then take this one
            diff = current_diff
    return diff

print(solution([3,1,2,4,3]))

# the answer 1 is the smallest difference that can be created, not teh position of the smallest difference

