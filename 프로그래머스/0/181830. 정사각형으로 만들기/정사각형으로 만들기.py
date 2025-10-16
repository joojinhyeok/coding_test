def solution(arr):
    r = len(arr)
    c = len(arr[0])

    if r > c:
        diff = r - c  
        for row in arr:
            row += [0] * diff
    
    elif r < c:
        diff = c - r  
        new_row = [0] * c
        for _ in range(diff):
            arr.append(new_row)

    return arr