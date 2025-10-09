def solution(n):
    count = 0 # 3x 마을 숫자의 순서로 n과 비교
    num = 0   # 1부터 확인할 실제 숫자
    
    while count < n:
        num += 1 # 다음 숫자로 넘어감
        
        # 3의 배수이거나, 숫자에 '3'이 포함되면 통과
        if num % 3 == 0 or '3' in str(num):
            continue
            
        # 위 조건에 걸리지 않은 착한 숫자이므로 카운트
        count += 1
        
    return num # count가 n이 되었을 때의 num을 반환