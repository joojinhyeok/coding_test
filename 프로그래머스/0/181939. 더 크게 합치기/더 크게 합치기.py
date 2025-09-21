def solution(a, b):
    A = str(a) + str(b)
    B = str(b) + str(a)
    if A > B:
        return int(A)
    else:
        return int(B)