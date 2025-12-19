def solution(t, p):
    answer = 0
    l = len(p)
    for i in range(len(t) - l + 1):
        a = t[i:i+l]
    
        if int(a) <= int(p):
            answer += 1
    return answer