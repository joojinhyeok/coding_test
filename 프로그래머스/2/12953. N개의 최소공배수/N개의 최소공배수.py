import math

def solution(arr):
    answer = arr[0]
    
    for num in arr:
        # 최소공배수를 계속 누적해서 구하기
        # 최소공배수 = 두 수의 곱 // 최대공약수
        answer = (num * answer) // math.gcd(answer, num)
    
    return answer