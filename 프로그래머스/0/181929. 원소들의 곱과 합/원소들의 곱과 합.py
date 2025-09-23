def solution(num_list):
    a = 1
    b = 0
    for i in num_list:
        a *= i
        b += i
    if a > (b*b):
        return 0
    else: 
        return 1