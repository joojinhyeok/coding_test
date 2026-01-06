def solution(a, b, n):
    answer = 0
    
    # 가지고 
    while n >= a:
        pack = n // a
        # 새로 받는 콜라의 개수
        new_cola = pack * b
        
        # 남은 빈 병 = 기존 빈 병 + 새로 받은 콜라
        n = (n%a) + new_cola
        
        answer += new_cola
    return answer