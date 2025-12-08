def solution(phone_number):
    p_list = list(phone_number)
    for i in range(len(phone_number) - 4):
        p_list[i] = '*'
    return "".join(p_list)