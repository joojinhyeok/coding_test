def solution(n):
    answer = []
    s_n = str(n)
    r_n = reversed(s_n)
    for i in r_n:
        answer.append(int(i))
    return answer