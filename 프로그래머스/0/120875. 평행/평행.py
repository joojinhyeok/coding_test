def solution(dots):
    # 기울기가 같다면 평행
    dx1 = dots[1][0] - dots[0][0]
    dy1 = dots[1][1] - dots[0][1]
    dx2 = dots[3][0] - dots[2][0]
    dy2 = dots[3][1] - dots[2][1]
    if (dy1/dx1) == (dy2/dx2):
        return 1
    
    dx1 = dots[2][0] - dots[0][0]
    dy1 = dots[2][1] - dots[0][1]
    dx2 = dots[3][0] - dots[1][0]
    dy2 = dots[3][1] - dots[1][1]
    if (dy1/dx1) == (dy2/dx2):
        return 1
    
    dx1 = dots[3][0] - dots[0][0]
    dy1 = dots[3][1] - dots[0][1]
    dx2 = dots[2][0] - dots[1][0]
    dy2 = dots[2][1] - dots[1][1]
    if (dy1/dx1) == (dy2/dx2):
        return 1
    
    return 0