def solution(citations):
    # 인용 횟수가 많은 순서대로 정렬 (내림차순)
    citations.sort(reverse=True)
    
    # 하나씩 등수랑 비교
    for idx, citation in enumerate(citations):        
        # 만약 인용 횟수가 등수보다 작아지는 순간이 오면?
        if citation < idx + 1:
            # 바로 직전 등수(idx)가 정답!
            # (현재 idx가 3이면, 앞서 0,1,2번까지 3명이 통과한 거니까 3이 답)
            return idx
            
    # 여기까지 왔다는 건, 모든 논문이 등수보다 인용이 많다는 뜻!
    # 예: [100, 100] -> 1등(100>=1), 2등(100>=2) -> 끝까지 통과 -> 답: 2(길이)
    return len(citations)