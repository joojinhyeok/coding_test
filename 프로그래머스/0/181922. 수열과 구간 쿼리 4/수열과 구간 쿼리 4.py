def solution(arr, queries):
    for i, j, k in queries:
        for a in range(i, j+1):
            if a % k == 0:
                arr[a] += 1
    return arr