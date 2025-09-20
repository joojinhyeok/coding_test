def solution(array):
    max_index = 0
    max_value = array[0]
    for i, j in enumerate(array):
        if j > max_value:
            max_value = j
            max_index = i
    return [max_value, max_index]