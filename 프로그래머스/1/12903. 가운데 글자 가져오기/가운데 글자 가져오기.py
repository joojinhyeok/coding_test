def solution(s):
    answer = ''
    m = int(len(s) / 2)
    s = list(s)
    if len(s) % 2 == 0:
        answer += s[m-1] + s[m]
    else:
        answer += s[m]
    return answer