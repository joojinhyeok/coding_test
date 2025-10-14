def solution(lines):
    answer = 0
    counts = [0] * 201 # 좌표를 표시할 배열(-100 ~ 100)
    for i, j in lines:
        # +100을 해주는 이유는 음수를 표시할 수 없기 때문
        for k in range(i+100, j+100):
            counts[k] += 1
    
    # counts 배열에서 원소가 2이상이면 겹치는 부분 이므로 answer+1
    for count in counts:
        if count >= 2:
            answer += 1
    return answer