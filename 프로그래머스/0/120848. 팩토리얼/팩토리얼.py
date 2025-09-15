import math

def solution(n):
    for i in range(10, 0, -1):
        a = math.factorial(i)
        if a <= n:
            return i