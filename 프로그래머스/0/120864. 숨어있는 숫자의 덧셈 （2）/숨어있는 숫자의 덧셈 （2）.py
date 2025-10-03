def solution(my_string):
    answer = 0
    num_str = "" # 1. 숫자들을 모아둘 임시 변수
    
    for char in my_string:
        if char.isdigit():
            num_str += char # 3. 숫자면 계속 이어 붙임
        else:
            # 4. 문자를 만났을 때, 그 전까지 모인 숫자가 있다면
            if num_str:
                answer += int(num_str)
                num_str = "" # 다시 비워줌
    
    # 5. 마지막 글자가 숫자로 끝나는 경우를 위해 한 번 더 확인
    if num_str:
        answer += int(num_str)
        
    return answer