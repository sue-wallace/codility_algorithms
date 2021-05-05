# stack data structure that lets you organise in a certain way - can only add to the top of the stack
# push x, add x to teh top of teh stack
# pop - removes from the top
# once the array is full item a can not be added, unless you use a list
# lifo - last in first out

# queue
# add an item at the tail, or cunsume an item from the head - this is called unqueue and dequeue
# a queue is fifo - first in first out
# enqueue, adds an item at the top of the list
# dequeue takes the item from the back of the list

# that, given a string S consisting of N characters, returns 1 if S is properly nested and 0 otherwise.
#
# For example, given S = "{[()()]}", the function should return 1 and given S = "([)()]", the function should return 0, as explained above.
#
# Write an efficient algorithm for the following assumptions:
#
# N is an integer within the range [0..200,000];
# string S consists only of the following characters: "(", "{", "[", "]", "}" and/or ")".

# PROBLEM

# A string S consisting of N characters is considered to be properly nested if any of the following conditions is true:
#
# S is empty;
# S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
# S has the form "VW" where V and W are properly nested strings.
# For example, the string "{[()()]}" is properly nested but "([)()]" is not.

# string can only contain  ( ) { } [] so...
# [{}] is valid -brackets are closed
# {(}()] - this is invalid
# basically open brackets should be closed

# 1 if nested, 0 is not properly nested
# Write a function using a stack:

def solution(S):
    is_valid = True # create teh variable valid
    stack = []
    for c in S:
        if c == "[" or c == "(" or c == "{":
            stack.append(c) # if a left bracket is detected, then push it onto the stack
        elif c == ")":
            is_valid = False if not stack or stack.pop() != "(" else is_valid # if a right bracket is met then pop it, otherwise leave is_valid as it is
        elif c == "]":
            is_valid = False if not stack or stack.pop() != "[" else is_valid # if a right bracket is met then pop it
        elif c == "}":
            is_valid = False if not stack or stack.pop() != "{" else is_valid # if a right bracket is met then pop it
    return 'pass' if is_valid and not stack else 'fail' # is the var returned is_valid, or stack, if stack then fail, otherwise pass


print(solution("()[]{}()[]{}"))

print(solution("()]]"))

# martin exmaple

def isValidPair(left, right): # define teh valid pairs
    if left == '(' and right == ')':
        return True
    if left == '[' and right == ']':
        return True
    if left == '{' and right == '}':
        return True
    return False


def solution_martin(S):
    stack = []

    for symbol in S:
        if symbol == '[' or symbol == '{' or symbol == '(':
            stack.append(symbol)
        else:
            if len(stack) == 0:
                return 0
            last = stack.pop()
            if not isValidPair(last, symbol):
                return 0

    if len(stack) != 0:
        return 0

    return 1

print(solution_martin("()[]{}()[]{}"))

print(solution_martin("()]]"))








