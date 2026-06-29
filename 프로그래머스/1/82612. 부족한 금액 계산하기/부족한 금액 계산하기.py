def solution(price, money, count):
    s = 0
    for i in range(1, count+1):
        s += price*i
    if money >= s:
        return 0
    else:
        return s - money