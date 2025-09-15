def solution(box, n):
    # 가로, 세로, 높이 다 각각 생각하기
    a = box[0] // n
    b = box[1] // n
    c = box[2] // n
    
    # 각각의 결과를 곱해주면 주사위 최대 개수를 구할 수 있음
    return a * b * c