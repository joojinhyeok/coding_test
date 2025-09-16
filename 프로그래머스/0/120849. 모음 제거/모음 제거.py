def solution(my_string):
    # my_string 순회하면서 모음이 아니면 answer에 추가
    answer = ''
    a = 'aeiou'
    for i in my_string:
        if i not in a:
            answer += i
            
    return answer