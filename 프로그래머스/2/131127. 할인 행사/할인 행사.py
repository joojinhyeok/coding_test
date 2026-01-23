from collections import Counter

def solution(want, number, discount):
    answer = 0
    target = dict(zip(want, number))
        
    # discount를 10일씩 잘라서 확인하기
    for i in range(len(discount) - 9):
        
        # i일 부터 10일 간의 할인 품목 자르기 (Slicing)
        ten_days = discount[i : i+10]
        
        # 자른 10일 치의 개수 세기 (Counter가 자동으로 해줌!)
        # Counter(['apple', 'apple', ...]) -> {'apple': 2, ...}
        current_counter = Counter(ten_days)
        
        # 순서 상관없이 key 값 같은 것끼리 value 비교
        if current_counter == target:
            answer += 1
            
    return answer