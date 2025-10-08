def solution(myString, pat):
    # last_index는 myString에 pat이 있는 시작 인덱스
    last_index = myString.rfind(pat)
    answer = myString[:last_index + len(pat)]
    
    return answer