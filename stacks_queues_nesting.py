# PROBLEM

# A string S consisting of N characters is called properly nested if:
#
# S is empty;
# S has the form "(U)" where U is a properly nested string;
# S has the form "VW" where V and W are properly nested strings.
# For example, string "(()(())())" is properly nested but string "())" isn't.
#
# Write a function:
#
# def solution(S)
#
# that, given a string S consisting of N characters, returns 1 if string S is properly nested and 0 otherwise.
#
# For example, given S = "(()(())())", the function should return 1 and given S = "())", the function should return 0, as explained above.
#
# Write an efficient algorithm for the following assumptions:
#
# N is an integer within the range [0..1,000,000];
# string S consists only of the characters "(" and/or ")".

# martin answer
#Because there is only one type of brackets, the problem is easier than Brackets. Just check if there is always a opening bracket before a closing one.

def solution(S):
    checker = 0

    for symbol in S:
        if symbol == '(':
            checker += 1
        else:
            if checker == 0:
                return 0
            checker -= 1

    if checker != 0: # if checker is not null then fail, else pass
        return 0

    return 1

print(solution("(()(())())"))

print(solution("())"))
