def solution(n):
    n = str(n)
    n_sort = sorted(n, reverse=True)
    return int("".join(n_sort))