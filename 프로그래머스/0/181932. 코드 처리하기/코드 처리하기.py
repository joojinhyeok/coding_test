def solution(code):
    answer = ''
    mode = 0
    for i, j in enumerate(code):
        if mode == 0:
            if j != '1':
                if i % 2 == 0:
                    answer += j
            if j == '1':
                mode = 1
        elif mode == 1:
            if j != '1':
                if i % 2 != 0:
                    answer += j
            if j == '1':
                mode = 0
    if answer == '':
        return 'EMPTY'
    return answer