def solution(rny_string):
    answer = ''
    for i in rny_string:
        if i == 'm':
            answer += 'rn'
        elif i != 'm':
            answer += i
    return answer