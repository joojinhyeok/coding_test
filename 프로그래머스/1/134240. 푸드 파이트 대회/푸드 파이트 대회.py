def solution(food):
    answer = ''
    l = ''
    # food의 원소는 음식의 개수
    for i in range(1, len(food)):
        count = food[i] // 2
        
        l += str(i) * count
        
    answer = l + "0" + l[::-1]
    return answer