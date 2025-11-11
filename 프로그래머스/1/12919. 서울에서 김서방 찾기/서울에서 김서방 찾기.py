def solution(seoul):
    x = 0 
    for i, j in enumerate(seoul):
        if j == 'Kim':
            x = i
            break

    answer = f'김서방은 {x}에 있다'
    return answer