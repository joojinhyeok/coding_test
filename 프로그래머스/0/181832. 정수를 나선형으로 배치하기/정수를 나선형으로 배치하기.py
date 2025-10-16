def solution(n):
    # 1. n x n 배열을 0으로 초기화
    #    (0은 아직 숫자가 채워지지 않았다는 의미로 사용)
    # answer = [[0, 0, ..], [0, 0, ..]...] 형태
    answer = [[0] * n for _ in range(n)]

    # 2. 초기 위치와 방향 설정
    x, y = 0, 0  # 시작 위치는 [0][0]
    direction = 0  # 0: 오른쪽, 1: 아래, 2: 왼쪽, 3: 위
    
    # 방향 전환을 위한 dx, dy 설정 (오른쪽 -> 아래 -> 왼쪽 -> 위)
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    # 3. 1부터 n*n 까지의 숫자를 배열에 채우기
    for i in range(1, n * n + 1):
        answer[x][y] = i # 현재 위치에 숫자 채우기
        
        # 다음 위치 계산
        nx = x + dx[direction]
        ny = y + dy[direction]

        # 4. 방향을 바꿔야 하는지 확인
        #   - 다음 위치가 배열 범위를 벗어나거나
        #   - 다음 위치에 이미 숫자가 채워져 있다면 (0이 아니라면)
        if nx < 0 or nx >= n or ny < 0 or ny >= n or answer[nx][ny] != 0:
            # 다음 이동할 방향을 정해줌
            direction = (direction + 1) % 4 # 시계방향으로 90도 회전
            
            # 바뀐 방향으로 다음 위치 다시 계산
            nx = x + dx[direction]
            ny = y + dy[direction]
        
        # 5. 다음 위치로 이동
        x, y = nx, ny
            
    return answer