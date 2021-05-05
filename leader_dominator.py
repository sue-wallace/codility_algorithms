# PROBLEM

# find teh lead element ina  list

# An array A consisting of N integers is given. The dominator of array A is the value that occurs in more than half of the elements of A.
#
# For example, consider array A such that
#
#  A[0] = 3    A[1] = 4    A[2] =  3
#  A[3] = 2    A[4] = 3    A[5] = -1
#  A[6] = 3    A[7] = 3
# The dominator of A is 3 because it occurs in 5 out of 8 elements of A (namely in those with indices 0, 2, 4, 6 and 7) and 5 is more than a half of 8.
#
# Write a function
#
# def solution(A)
#
# that, given an array A consisting of N integers, returns index of any element of array A in which the dominator of A occurs. The function should return −1 if array A does not have a dominator.
#
# For example, given array A such that
#
#  A[0] = 3    A[1] = 4    A[2] =  3
#  A[3] = 2    A[4] = 3    A[5] = -1
#  A[6] = 3    A[7] = 3
# the function may return 0, 2, 4, 6 or 7, as explained above.
#
# Write an efficient algorithm for the following assumptions:
#
# N is an integer within the range [0..100,000];
# each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].

# so if the  count of an element is greater than the length of the list divided by 2
# there can only be one leader
# more efficient if the arrasy is sorted first, then take the middle item and then see if it is bigger than the array lenth // 2

# 2 vars, count and leader

def solution(A): # a is the array given
    counter = 0 # initialise counter as 0
    leader_item = 0 # who is the leader?
    for item in A: # go over each item in array
        if counter == 0: # if counter is zero,
            leader_item = item # then this leader item is set
            counter += 1 # set the counter to 1, and add 1 thereafter
        elif leader_item == item: # is the current leader equal to teh item being iterated over?
            counter += 1 # then add one to the counter
        else:
            counter -= 1 # take one off the counter
    occurrence = A.count(leader_item) # is the leader a leader?, how many times does the candidate value occur,
    if occurrence > (len(A)/2): # if it is greater than length/2
        return A.index(leader_item)# then return index of a
    else:
        return -1 #otherwise there is no leader


print(solution([3,0,1,1,4,1,1]))

# 2 is given, because this is the index of the item leader, not the item itself

