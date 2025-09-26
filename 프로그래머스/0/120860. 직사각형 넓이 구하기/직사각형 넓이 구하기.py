def solution(dots):
    a = []
    b = []
    for i, j in dots:
        a.append(i)
        b.append(j)
    c = max(a) - min(a)
    d = max(b) - min(b)
    return c*d