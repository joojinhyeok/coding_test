def solution(strings, n):
    answer = []
    s = []
    for i in strings:
        a = i[n] + i
        s.append(a)
    s.sort()

    for i in s:
        answer.append(i[1:])
    return answer