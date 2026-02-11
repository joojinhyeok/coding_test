from collections import Counter

def solution(clothes):
    # 1. 의상 종류(category)만 모으기
    categories = [kind for name, kind in clothes]
    
    # 2. 종류별 개수 세기 (Counter가 알아서 해줌)
    # 예: {'headgear': 2, 'eyewear': 1}
    counts = Counter(categories)
    
    answer = 1
    
    # 3. 공식: (개수 + 1)을 계속 곱하기
    for count in counts.values():
        answer *= (count + 1)
    
    # 4. 아무것도 안 입은 상태 1개 빼기
    return answer - 1