def solution(n):
    ans = 0
    while n > 0:
        # n이 짝수면 순간이동
        if n % 2 == 0:
            n //= 2
            
        # n이 홀수면 -1 -> 건전지 사용
        else:
            n -= 1
            ans += 1
    return ans