def solution(keyinput, board):
    answer = [0, 0]

    # //2를 하는 이유: x, y축이기 때문에 +- 고려
    max_x = board[0] // 2
    max_y = board[1] // 2
    
    for i in keyinput:
        if i == 'up' and answer[1] < max_y:
            answer[1] += 1
        elif i == 'down' and answer[1] > -max_y:
            answer[1] -= 1
        elif i == 'left' and answer[0] > -max_x:
            answer[0] -= 1
        elif i == 'right' and answer[0] < max_x:
            answer[0] += 1
            
    return answer