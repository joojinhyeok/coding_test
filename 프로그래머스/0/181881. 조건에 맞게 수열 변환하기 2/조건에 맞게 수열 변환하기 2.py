def solution(arr):
    answer = 0
    
    while True:
        # 변환된 결과를 담을 새 리스트를 만듦
        next_arr = []
        
        # [중요!] '이전 상태'의 배열인 before_arr를 기준으로 반복
        for num in arr:
            if num >= 50 and num % 2 == 0:
                # 50보다 크거나 같은 짝수
                new_value = int(num / 2)
            elif num < 50 and num % 2 != 0:
                # 50보다 작은 홀수
                new_value = num * 2 + 1
            else:
                # 나머지 경우는 그대로
                new_value = num
            
            next_arr.append(new_value)
        
        # 변환 전과 후가 같다면 반복 종료
        if arr == next_arr:
            break
        
        arr = next_arr    
        # 4. 다르다면 카운터 증가
        answer += 1
        
    return answer