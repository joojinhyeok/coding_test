def solution(quiz):
    answer = []
    for i in quiz:
        # i는 "3 - 4 = -3"인 형태
        # a는 좌변, b는 우변
        a, b = i.split(" = ")
        
        if eval(a) == int(b):
            answer.append('O')
        else:
            answer.append('X')
    return answer