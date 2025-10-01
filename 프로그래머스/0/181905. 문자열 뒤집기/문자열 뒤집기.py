def solution(my_string, s, e):
    answer = ''
    w = ''
    w = my_string[s:e+1]
    w = w[::-1]
    answer = my_string[:s] + w + my_string[e+1:] 
    return answer