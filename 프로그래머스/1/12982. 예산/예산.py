def solution(d, budget):
    answer = 0
    sort_d = sorted(d)

    for i in sort_d:
        budget -= i
        if budget >= 0:
            answer += 1
    
    return answer