def solution(rank, attendance):
    answer = 0
    r = []
    for i, j in enumerate(attendance):
        if j:
         r.append([rank[i], i])
    r.sort()
    print(r)
    answer = 10000 * r[0][1] + 100 * r[1][1] + r[2][1]
    return answer