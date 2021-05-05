# An array A consisting of N integers is given. It contains daily prices of a stock share for a period of N consecutive days. If a single share was bought on day P and sold on day Q, where 0 ≤ P ≤ Q < N, then the profit of such transaction is equal to A[Q] − A[P], provided that A[Q] ≥ A[P]. Otherwise, the transaction brings loss of A[P] − A[Q].
#
# For example, consider the following array A consisting of six elements such that:
#
#   A[0] = 23171
#   A[1] = 21011
#   A[2] = 21123
#   A[3] = 21366
#   A[4] = 21013
#   A[5] = 21367
# If a share was bought on day 0 and sold on day 2, a loss of 2048 would occur because A[2] − A[0] = 21123 − 23171 = −2048. If a share was bought on day 4 and sold on day 5, a profit of 354 would occur because A[5] − A[4] = 21367 − 21013 = 354. Maximum possible profit was 356. It would occur if a share was bought on day 1 and sold on day 5.
#
# Write a function,
#
# def solution(A)
#
# that, given an array A consisting of N integers containing daily prices of a stock share for a period of N consecutive days,
# returns the maximum possible profit from one transaction during this period. The function should return 0 if
# it was impossible to gain any profit.
#
# For example, given array A consisting of six elements such that:
#
#   A[0] = 23171
#   A[1] = 21011
#   A[2] = 21123
#   A[3] = 21366
#   A[4] = 21013
#   A[5] = 21367
# the function should return 356, as explained above.
#
# Write an efficient algorithm for the following assumptions:
#
# N is an integer within the range [0..400,000];
# each element of array A is an integer within the range [0..200,000].

# the return is the maximum profit that can be gained

# This is the solution for Maximum Slice Problem > Max Profit
#
# This is marked as PAINLESS difficulty

# also known as maximum sub array problem (sub array must be continious)
# only makes sense if there are negative values, otherwise the whole array is the max sum
# max slice problem

#kadane

def solution(A): # a is the array of profits
    global_max_sum = 0
    local_max_sum = 0
    for i in range(1, len(A)): #from 1 to the length of array
        d = A[i] - A[i - 1] # d is the difference between items next to each other in the array
        local_max_sum = max(d, local_max_sum + d) # which is the maximum, is it the difference, or the local max sum plus the difference?
        global_max_sum = max(local_max_sum, global_max_sum) # take which is greater, local or global
    return global_max_sum # return the global answer, not local


#   differences, or delta                   -2160,   112,   243,  -353,   354
print(solution([23171, 21011, 21123, 21366, 21013, 21367]))

print(sum([-2160, 112, 243, -353, 354]))