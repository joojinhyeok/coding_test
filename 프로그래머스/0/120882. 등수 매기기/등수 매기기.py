def solution(score):
    answer = []
    for s in score:
        # answer에 평균점수가 담김
        answer.append((s[0] + s[1]) / 2)
    
    ranks = []
    for a1 in answer:
        rank = 1 
        for a2 in answer:
            # answer에 있는 평균 점수를 비교해 rank를 ranks배열에 담아줌
            if a2 > a1: 
                rank += 1 
        ranks.append(rank)
        
    return ranks