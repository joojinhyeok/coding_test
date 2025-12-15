def solution(price, money, count):
    p = 0
    for i in range(1, count+1):
        p += price * i
    
    answer = p - money
    if answer < 0:
        return 0
    return answer