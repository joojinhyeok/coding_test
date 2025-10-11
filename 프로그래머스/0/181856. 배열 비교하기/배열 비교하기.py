def solution(arr1, arr2):
    if len(arr1) < len(arr2):
        return -1
    elif len(arr1) > len(arr2):
        return 1
    elif len(arr1) == len(arr2):
        arr1 = sum(arr1)
        arr2 = sum(arr2)
        if arr1 > arr2:
            return 1
        elif arr1 < arr2:
            return -1
        else: return 0