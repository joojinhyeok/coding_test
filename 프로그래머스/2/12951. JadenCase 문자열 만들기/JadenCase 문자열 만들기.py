def solution(s):
    answer = []
    s_split = s.split(" ") # 공백이 연속해서 나올 수 있으므로 split(" ") 사용
    
    for word in s_split:
        # capitalize()는 빈 문자열("")에도 에러 없이 ""를 반환함
        # 첫 글자가 숫자여도 알아서 처리해줌
        answer.append(word.capitalize())
        
    a = " ".join(answer)
    return a