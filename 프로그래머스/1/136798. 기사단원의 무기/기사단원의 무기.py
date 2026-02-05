def solution(number, limit, power):
    answer = 0
    
    # 1번 기사부터 number번 기사까지 검사
    for i in range(1, number + 1):
        
        # [약수 개수 구하기 로직]
        count = 0
        
        # 1부터 i의 제곱근까지만 반복 (int(i**0.5))
        for j in range(1, int(i**0.5) + 1):
            if i % j == 0:
                count += 1          # j는 약수 (앞쪽 짝꿍)
                
                # 제곱수(예: 3x3=9)가 아니라면 뒷쪽 짝꿍도 존재함
                if j**2 != i: 
                    count += 1
        
        # [제한 수치 확인]
        if count > limit:
            answer += power  # 제한 넘으면 정해진 파워(벌칙) 적용
        else:
            answer += count  # 안 넘으면 그대로 적용
            
    return answer