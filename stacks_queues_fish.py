# PROBLEM

# You are given two non-empty arrays A and B consisting of N integers. Arrays A and B represent N voracious fish in a river,
# ordered downstream along the flow of the river.
#
# The fish are numbered from 0 to N − 1. If P and Q are two fish and P < Q, then fish P is initially upstream of fish Q.
# Initially, each fish has a unique position.
#
# Fish number P is represented by A[P] and B[P]. Array A contains the sizes of the fish. All its elements are unique.
# Array B contains the directions of the fish. It contains only 0s and/or 1s, where:
#
# 0 represents a fish flowing upstream,
# 1 represents a fish flowing downstream.
# If two fish move in opposite directions and there are no other (living) fish between them, they will eventually meet each other.
# Then only one fish can stay alive − the larger fish eats the smaller one. More precisely, we say that two fish P and Q meet each other when P < Q, B[P] = 1 and B[Q] = 0, and there are no living fish between them. After they meet:
#
# If A[P] > A[Q] then P eats Q, and P will still be flowing downstream,
# If A[Q] > A[P] then Q eats P, and Q will still be flowing upstream.
# We assume that all the fish are flowing at the same speed. That is, fish moving in the same direction never meet.
# The goal is to calculate the number of fish that will stay alive.
#
# For example, consider arrays A and B such that:
#
#   A[0] = 4    B[0] = 0
#   A[1] = 3    B[1] = 1
#   A[2] = 2    B[2] = 0
#   A[3] = 1    B[3] = 0
#   A[4] = 5    B[4] = 0
# Initially all the fish are alive and all except fish number 1 are moving upstream. Fish number 1 meets fish number 2 and eats it, then it meets fish number 3 and eats it too. Finally, it meets fish number 4 and is eaten by it. The remaining two fish, number 0 and 4, never meet and therefore stay alive.
#
# Write a function:
#
# def solution(A, B)
#
# that, given two non-empty arrays A and B consisting of N integers, returns the number of fish that will stay alive.
#
# For example, given the arrays shown above, the function should return 2, as explained above.
#
# Write an efficient algorithm for the following assumptions:
#
# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [0..1,000,000,000];
# each element of array B is an integer that can have one of the following values: 0, 1;
# the elements of A are all distinct.

# to return: The goal is to calculate the number of fish that will stay alive

# solution

#Put all downstream swimming fishes on a stack. Any upstream swimming fish has to fight(eat) all fishes on the stack.
# If there are no fish on the stack, the fish survives. If the stack has some downstream fishes at the end, they also survive.

# big eats small

def solution(a,b): # a is the weight of teh fish, b is the direction, 0 being left, 1 being right

    return # the number of survivors

# martin solution

def solution(A, B):
    survivals = 0
    stack = []

    for idx in range(len(A)):
        if B[idx] == 0:
            while len(stack) != 0:
                if stack[-1] > A[idx]:
                    break
                else:
                    stack.pop()

            else:
                survivals += 1
        else:
            stack.append(A[idx])

    survivals += len(stack)

    return survivals

A = [4,3,2,1,5]
B = [0,1,0,0,0]

print(solution(A, B))

# udemy answer

def solution_udemy(A, B): #a is the fish size, b is the direction 0, is right, 1 is left
    stack = [] # intialise stack, fish that are moving to the right will be pushed to the stack
    fish_that_live = 0 # intialise the fish that will live starting at zero

    for i in range(len(A)): # iterate over fish size,
        weight = A[i] # take the weight and assign
        if B[i] == 1: # if the fish is going downstream then append to stack
            stack.append(weight)
        else: # otherwise pop the stack (if the fish is going right)
            weight_down_stream = stack.pop() if stack else -1 # only if the stack is not empty
            while weight_down_stream != -1 and weight_down_stream < weight: # if the stack empty, and is the weight down stream less than upstream? the pop the stack
                weight_down_stream = stack.pop() if stack else -1
            if weight_down_stream == -1: # stack is empty so add a fish to live
                fish_that_live += 1
            else:
                stack.append(weight_down_stream)
    return fish_that_live + len(stack) #return the survivors plus the fish left in the stack

print(solution_udemy([4, 8, 2, 6, 7], [0, 1, 1, 0, 0]))

print(solution_udemy(A, B))


