def solution(my_string, indices):
    answer = ''
    for i, j in enumerate(my_string):
        if i not in indices:
            answer += my_string[i]
    return answer