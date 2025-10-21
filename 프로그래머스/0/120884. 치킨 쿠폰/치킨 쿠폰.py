def solution(chicken):
    answer = 0
    c = 0
    for i in range(chicken):
        c += 1
        if c % 10 == 0:
            answer += 1
            c += 1
    return answer