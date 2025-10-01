def solution(my_string, is_prefix):
    s = []
    for i in range(len(my_string)):
        s.append(my_string[:i])
    if is_prefix in s:
        return 1
    else:
        return 0