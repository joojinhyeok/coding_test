def solution(arr):
    answer = 0
    n = 0
    for i in arr:
        n += i
        
    answer = n / len(arr)
    return answer