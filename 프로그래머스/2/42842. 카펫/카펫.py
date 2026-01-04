# 단순 완전 탐색 문제
import math
def solution(brown, yellow):
    total = brown + yellow # -> return의 두 수 곱하면 total이 나옴
    
    # total을 다 확인할 필요없이 루트 total까지만 확인
    t = int(math.sqrt(total)) 
    
    # (w-2) * (h-2) == yellow -> 노란색 격자 수 검증
    for h in range(1, t+1): # -> 세로는 최소 3부터 시작
        if total % h == 0:
            w = total // h
            
            if (w-2) * (h-2) == yellow:
                return [w, h]