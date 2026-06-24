def solution(arr, divisor):
    answer = []
    arr = sorted(arr)
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    if len(answer) == 0:
        return [-1]
    return answer