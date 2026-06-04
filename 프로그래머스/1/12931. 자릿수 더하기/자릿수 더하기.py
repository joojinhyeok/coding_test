def solution(n):
    answer = 0
    s_n = str(n)
    for i in s_n:
        answer += int(i)
    return answer