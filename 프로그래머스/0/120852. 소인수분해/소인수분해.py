def solution(n):
    answer = []
    a = 2
    
    while a <= n:
        if n % a == 0: # a가 n의 약수
            if a not in answer:
                answer.append(a)
            n /= a
        else:
            a += 1
    return answer