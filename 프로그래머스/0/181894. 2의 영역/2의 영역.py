def solution(arr):
    answer = []
    for i, j in enumerate(arr):
        if j == 2:
            answer.append(i)
    if not answer:
        return [-1]
    
    s = answer[0]
    e = answer[-1]
    return arr[s:e+1]