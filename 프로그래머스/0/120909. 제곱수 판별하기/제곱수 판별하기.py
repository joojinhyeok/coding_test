def solution(n):
    # n의 제곱근
    sqrt = n ** 0.5
    
    # 제곱근이 정수인지 확인
    if sqrt % 1 == 0:
        return 1
    else:
        return 2