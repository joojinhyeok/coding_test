def solution(x):
    n = 0
    for i in str(x):
        n += int(i)
    if x % n == 0:
        return True
    else: return False