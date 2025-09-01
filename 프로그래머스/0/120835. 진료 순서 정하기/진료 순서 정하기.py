def solution(emergency):
    answer = []
    sorted_emergency = sorted(emergency, reverse=True)
    for i in emergency:
        # index는 0부터 시작하므로 +1
        answer.append(sorted_emergency.index(i) + 1)
    return answer