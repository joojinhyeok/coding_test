def solution(num, total):
    avg = total / num
    
    if num % 2 == 1: # num이 홀수일 때
        # avg가 4.0이면 start는 3
        start = int(avg - (num // 2))
        
    else: # num이 짝수일 때
        # avg가 3.5이면 start는 2
        start = int(avg - (num // 2) + 0.5)
        
    # 3. start부터 num개의 연속된 숫자를 리스트로 만듦
    answer = [start + i for i in range(num)]
    
    return answer