def solution(array, commands):
    answer = []
    for i in commands:
        r = []
        a = i[0] - 1
        b = i[1]
        c = i[2] - 1
        for j in range(a, b):
            r.append(array[j])
        r.sort()
        answer.append(r[c])        

    return answer