import math

def solution(a, b):
    g = math.gcd(a, b)
    # 기약분수로 만듦
    b = b // g 

    # 분모(b)를 2와 5로 계속 나누기
    while b % 2 == 0:
        b = b // 2
    
    while b % 5 == 0:
        b = b // 5
        
    # b가 1이면 -> 유한소수
    if b == 1:
        return 1
    # b가 1이 아닌 수면 -> 무한소수
    else:
        return 2