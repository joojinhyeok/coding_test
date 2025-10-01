def solution(intStrs, k, s, l):
    answer = []
    num = []
    for i in intStrs:
        num = i[s:s+l]
        if int(num) > k:
            answer.append(int(num))
    return answer