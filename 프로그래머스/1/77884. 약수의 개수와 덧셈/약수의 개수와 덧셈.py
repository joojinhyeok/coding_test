def solution(left, right):
    answer = 0
    
    # left부터 right까지 모든 수를 확인
    for num in range(left, right + 1):
        count = 0
        
        # 현재 숫자의 약수 개수 세기
        for i in range(1, num + 1):
            if num % i == 0:
                count += 1
        
        # 짝수면 더하고, 홀수면 빼기
        if count % 2 == 0:
            answer += num
        else:
            answer -= num
            
    return answer