def solution(s):
    answer = 0
    a = 0
    split_s = s.split(" ")
    # print(split_s)
    for i in split_s:
        if i == 'Z':
            answer -= int(a)
        else:
            answer += int(i)
            a = int(i)
            
    return answer