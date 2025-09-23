def solution(my_string):
    answer = ''
    my_string_lower = my_string.lower()
    list_str = list(my_string_lower)
    list_str.sort()
    answer = "".join(list_str)
    return answer