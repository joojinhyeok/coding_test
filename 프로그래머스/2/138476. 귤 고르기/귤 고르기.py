from collections import Counter

def solution(k, tangerine):
    answer = 0
    # Counter({2: 2, 3: 2, 5: 2, 1: 1, 4: 1})
    cnt = Counter(tangerine)
    
    # 개수(value)만 뽑아서 내림차순으로 정렬한다.
    counts = sorted(cnt.values(), reverse=True) # 결과: [2, 2, 2, 1, 1] -> 개수
    
    # 개수가 많은 순서대로 k에서 뺀다.
    for c in counts:
        k -= c      # 귤 c개만큼 상자에 담기
        answer += 1 # 종류 하나 추가
        
        if k <= 0:
            break
            
    return answer