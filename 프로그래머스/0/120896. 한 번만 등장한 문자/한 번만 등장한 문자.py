def solution(s):
    answer = ''
    counts = {}
    # s 순회하면서 counts에 있으면 +1을 해주고 counts에 없으면 1
    for i in s:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
            
    # print(counts)
    # i는 문자 j는 개수 -> counts = {'a':2, 'b':1 ...}
    for i, j in counts.items():
        if j == 1:
            answer += i
    
    return "".join(sorted(answer))