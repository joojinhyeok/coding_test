def solution(elements):
    answer = set() # 중복x -> set()사용
    n = len(elements)
    
    # 1. 원형 수열 처리를 위해 리스트를 2배로 늘림
    # -> 슬라이싱[:] 문제에서는 이렇게 2배 늘려서 풀기
    # -> deque는 실제로 rotate()하는 문제에서 사용
    extended_elements = elements * 2
    
    # 2. 길이(length)를 1부터 n까지 늘려가며 확인
    for length in range(1, n + 1):
        # 3. 시작점(start)을 0부터 n-1까지 이동(n번 반복)
        for start in range(n):
            # 슬라이싱으로 부분 수열 자르기
            sub_list = extended_elements[start : start + length]
            
            # 합 구해서 집합에 넣기 (중복 자동 제거)
            answer.add(sum(sub_list))
            
    return len(answer)