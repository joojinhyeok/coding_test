def solution(n, left, right):
    # 2차원 배열로 만들 필요x -> left ~ right까지 1차원 배열만 구하기
    answer = []
    
    # left부터 right까지 필요한 인덱스만 뽑아서 계산
    for i in range(left, right + 1):
        
        # 1차원 인덱스 i를 2차원 좌표(행, 열)로 변환
        row = i // n
        col = i % n
        
        # 규칙: 값 = max(행, 열) + 1
        val = max(row, col) + 1
        
        answer.append(val)
        
    return answer