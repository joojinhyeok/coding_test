# Dynamic Programming, DP문제
# 키워드: "경우의 수", "방법의 수"
# 조건: 한 번에 움직일 수 있는 거리가 정해져 있음 (1칸, 2칸 등)
# 특징: 큰 문제(4칸 가기)를 풀기 위해 작은 문제(3칸 가기, 2칸 가기)의 답이 필요함

def solution(n):
    if n < 3:
        return n
    
    dp = [0, 1, 2]
    for i in range(3, n + 1):
        next_val = (dp[i-1] + dp[i-2]) % 1234567
        dp.append(next_val)
        
    return dp[n]