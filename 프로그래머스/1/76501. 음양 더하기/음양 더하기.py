def solution(absolutes, signs):
    answer = 0
    for i, v in zip(absolutes, signs):
        if v:
            answer += i
        else:
            answer -= i
    return answer