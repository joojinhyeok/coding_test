def solution(hp):
    answer = 0
    # 탐욕(Greedy) 알고리즘 사용
    # 1) 장군개미 
    answer += hp // 5
    hp = hp % 5
    # 2) 병정개미
    answer += hp // 3
    hp = hp % 3
    # 3) 일개미
    answer += hp
    
    return answer