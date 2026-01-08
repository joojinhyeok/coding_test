def solution(people, limit):
    answer = 0
    s = 0
    e = len(people) - 1
    people.sort()
    while s <= e:
        # 가장 무거운 사람이랑 가장 가벼운 사람 태워보기
        if people[s] + people[e] <= limit:
            s += 1
            e -= 1
        else:
            e -= 1

        answer += 1
    return answer