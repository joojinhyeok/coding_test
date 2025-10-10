def solution(arr, flag):
    answer = []
    for i, j in enumerate(flag):
        num = arr[i]
        
        if j:
            answer += [num] * (num * 2)
        else:
            # answer의 마지막 num개의 원소를 제거 (슬라이싱)
            answer = answer[:-num]
            
    return answer