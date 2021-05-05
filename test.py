from typing import List
def solution(A, B, N):
    if N > 1000:
        print('wrong')
    else:
        unit = [0] * (N + 1) # initialise var to 0, multiply by no of cities
    for a, b in zip(A, B): # pair items
        unit[a] += 1
        unit[b] += 1

    full_rank = 0 # intilise var to be returned

    for a, b in zip(A, B):
        full_rank = max(full_rank, unit[a] + unit[b]-1) # which is higher, full_rank, or a +b -1
    return full_rank

A = [1,2,3,3]
B = [2,3,1,4]
N = 4

testA = [1,2,4,8]
testB = [2,3,5,7]
testN = 1001

print(solution (testA, testB, 9))