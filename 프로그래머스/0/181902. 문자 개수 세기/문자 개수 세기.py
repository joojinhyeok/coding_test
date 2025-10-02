def solution(my_string):
    answer = []
    a = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    
    for i in a:
        c = my_string.count(i)
        answer.append(c)
    return answer