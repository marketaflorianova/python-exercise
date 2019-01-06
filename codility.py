# Write a function:
#     def solution(A)
# that, given an array A of N integers, returns the smallest positive integer
# (greater than 0) that does not occur in A.
# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
# Given A = [1, 2, 3], the function should return 4.
# Given A = [-1, -3], the function should return 1.
# Write an efficient algorithm for the following assumptions:
#
#         N is an integer within the range [1..100,000];
#         each element of array A is an integer within the range
#         [-1,000,000..1,000,000].

def solution(A):
    for x in A:
        if x < 1 and 1 not in A:
            return 1
        elif (x+1) not in A and (x+1) > 1:
            return x+1
print(solution(sorted([1, 3, 6, 4, 1, 2])))