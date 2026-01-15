def solution(n, a, b):
    answer = 0
    
    # 두 사람의 번호가 같아질 때까지 반복 (같아지면 만난 거니까 종료)
    while a != b:
        # 라운드 += 1
        answer += 1
        
        # 다음 라운드 번호 부여
        a = (a + 1) // 2
        b = (b + 1) // 2
        
    return answer