def solution(numLog):
    answer = ''
    for i in range(1, len(numLog)):
        a = numLog[i] - numLog[i-1]
        if a == 1:
            answer += 'w'
        elif a == -1:
            answer += 's'
        elif a == 10:
            answer += 'd'
        else:
            answer += 'a'
    return answer