def solution(my_string, num1, num2):
    answer = ''
    # my_string을 리스트 형태로 변환
    my_string_list = list(my_string)
    my_string_list[num1], my_string_list[num2] = my_string_list[num2], my_string_list[num1]
    
    # my_string_list를 다시 문자열로 변환
    answer = "".join(my_string_list)
    return answer