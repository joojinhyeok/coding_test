def solution(array, n):
    answer = 0
    a = 100
    array.sort()
    for i in array:
        if a > abs(i-n):
            a = abs(i-n)
            answer = i
    return answer