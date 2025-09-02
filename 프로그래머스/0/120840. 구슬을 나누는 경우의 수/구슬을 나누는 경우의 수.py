import math

def solution(balls, share):
    # math.comb(5, 3) -> 5중 3개를 순서 상관없이 뽑는 경우의 수
    return math.comb(balls, share)