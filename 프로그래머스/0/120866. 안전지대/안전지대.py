def solution(board):
    n = len(board)
    answer = 0

    # 1. 모든 칸을 하나씩 확인 (r행, c열)
    for r in range(n):
        for c in range(n):
            
            # 2. 일단 현재 칸은 안전하다고 가정
            is_safe = True
            
            # 3. 현재 칸의 주변 3x3 구역을 탐색
            for dr in range(-1, 2):
                for dc in range(-1, 2):
                    nr, nc = r + dr, c + dc
                    
                    # 지도 범위를 벗어나지 않는지 확인
                    if 0 <= nr < n and 0 <= nc < n:
                        # 주변에 지뢰(1)가 하나라도 있으면
                        if board[nr][nc] == 1:
                            # 이 칸은 안전하지 않음!
                            is_safe = False
                            break # 더 찾아볼 필요 없으니 탐색 중단
                if not is_safe:
                    break
            
            # 4. 모든 주변 칸을 확인했는데도 is_safe가 True라면, 진짜 안전한 지역임
            if is_safe:
                answer += 1
                
    return answer