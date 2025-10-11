def solution(arr):
    current_len = len(arr)
    target_len = 1

    while target_len < current_len:
        target_len *= 2

    num_zeros_to_add = target_len - current_len
    arr += [0] * num_zeros_to_add
    
    return arr