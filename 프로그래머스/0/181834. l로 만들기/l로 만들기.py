def solution(myString):
    answer = ''
    # ord()로 알파벳을 숫자로 변환
    for i in myString:
        if ord(i) < ord('l'):
            answer += 'l'
        else:
            answer += i
    return answer