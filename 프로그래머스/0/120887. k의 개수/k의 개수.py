def solution(i, j, k):
    answer = 0
    k_str = str(k)
    
    for num in range(i, j + 1):
        num_str = str(num)
        answer += num_str.count(k_str)
        
    return answer