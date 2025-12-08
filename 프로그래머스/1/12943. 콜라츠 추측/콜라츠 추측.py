def solution(num):
    answer = 0
    if num == 1:
        return 0
    
    for i in range(500):
        if num % 2 == 0:
            num /= 2
        else:
            num = num * 3 + 1
        if num == 1:
            return i + 1
    # for문 다 돌았는데 끝나지 않음
    return -1  