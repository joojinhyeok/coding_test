def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        count = 0
        for j in range(1, i+1):
            if i % j == 0:
                count += 1
                continue
        # 약수의 개수 = 홀수 -> 완전제곱수(1, 4, 9, 16..)
        if int(i ** 0.5) ** 2 == i:
            answer -= i
        else:
            answer += i
    return answer