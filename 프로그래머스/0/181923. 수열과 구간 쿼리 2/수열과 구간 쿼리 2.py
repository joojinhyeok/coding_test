def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        a = []
        for i in range(s, e + 1):
            # arr[i] 값이 k보다 크면 다 넣고
            if arr[i] > k:
                a.append(arr[i])
        # 리스트가 비어있으면
        if not a: 
            answer.append(-1)
        else:
            # min()으로 최소값만 append 하기
            answer.append(min(a))
            
    return answer