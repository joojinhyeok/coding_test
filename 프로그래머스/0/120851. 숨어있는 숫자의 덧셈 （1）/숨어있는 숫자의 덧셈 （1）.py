def solution(my_string):
    answer = 0
    for i in my_string:
        # isdigit()으로 '1'처럼 문자형인 숫자를 찾아냄
        if i.isdigit():
            answer += int(i)
    
    return answer