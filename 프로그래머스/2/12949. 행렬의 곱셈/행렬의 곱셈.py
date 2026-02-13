def solution(arr1, arr2):
    # 1. 결과 행렬의 크기 미리 만들기
    # 결과 행 개수 = arr1의 행 개수
    # 결과 열 개수 = arr2의 열 개수
    row1 = len(arr1)
    col1 = len(arr1[0]) # = row2 (곱셈이 성립하려면 같아야 함)
    col2 = len(arr2[0])
    
    answer = [[0] * col2 for _ in range(row1)]
    
    # 2. 행렬 곱셈 수행 (3중 for문)
    for i in range(row1):           # arr1의 행 (가로)
        for j in range(col2):       # arr2의 열 (세로)
            for k in range(col1):   # 더하는 과정
                answer[i][j] += arr1[i][k] * arr2[k][j]
                
    return answer