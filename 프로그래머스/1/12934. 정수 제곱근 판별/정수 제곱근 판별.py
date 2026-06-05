def solution(n):
    i = n ** (1/2)
    if i == int(i):
        return (i+1) ** 2
    else:
        return -1