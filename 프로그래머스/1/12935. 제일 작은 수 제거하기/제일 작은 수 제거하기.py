def solution(arr):
    answer = []
    if len(arr) <= 1:
        return [-1]

    m = min(arr)
    for i in arr:
        if i > m:
            answer.append(i)
    
    return answer