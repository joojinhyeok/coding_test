def solution(a, b):
    odd = [1, 3, 5]
    even = [2, 4, 6]
    if a in odd and b in odd:
        return a**2 + b**2
    elif a in even and b in even:
        return abs(a-b)
    else: return 2*(a+b)