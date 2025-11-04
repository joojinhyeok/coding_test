def solution(numbers):
    i = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    for j in numbers:
        if j in i:
            i.remove(j)
    answer = sum(i)
    return answer