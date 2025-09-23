def solution(a, d, included):
    answer = 0
    for i, j in enumerate(included):
        if j:
            answer += (a + (d*i))
    return answer