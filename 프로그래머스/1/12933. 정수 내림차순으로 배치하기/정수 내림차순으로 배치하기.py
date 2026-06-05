def solution(n):
    answer = ''
    n1 = sorted(list(str(n)), reverse=True)
    
    for i in n1:
        answer += i
    return int(answer)