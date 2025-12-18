def solution(s):
    count = 0
    for i in s:
        if i == '(':
            count += 1
        else:
            count -= 1
        # 양수인 경우는 뒤에서 닫는 괄호가 나올 수 있으니 음수인 경우만 False 리턴
        if count < 0:
            return False
    return count == 0