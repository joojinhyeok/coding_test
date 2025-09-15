def solution(n):
    answer = 0
    # 합성수 - 약수의 개수가 3개 이상인 수
    for i in range(1, n+1):
        a = 0
        for j in range(1, i+1):
            if i % j == 0:
                a += 1
        if a >= 3:
            answer += 1
            
    return answer