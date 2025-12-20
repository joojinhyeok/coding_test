def solution(n):
    tmp = '' # 3진법 숫자를 담을 문자열 -> int형으로는 담을 수 없기 때문
    
    while n > 0:
        # 나머지를 문자열로 바꿔서 더함
        tmp += str(n % 3)
        # 몫을 다시 n에 저장해서 계속 나눔
        n //= 3
        
    # 3진법 문자열을 10진법 숫자로 변환
    answer = int(tmp, 3)
    
    return answer