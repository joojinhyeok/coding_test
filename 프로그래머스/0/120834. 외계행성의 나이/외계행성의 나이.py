def solution(age):
    answer = ''
    for d in str(age):
        # ord('a')는 97이므로 뒤에 d 값을 더해서 나머지 숫자도 문자로 바꿈
        answer += chr(ord('a') + int(d))
    return answer

# ord(): 문자 -> 유니코드 정수값으로 변경 
# ex) a는 유니코드 97, b = 98, c = 99 ...
# chr(): 정수 -> 문자로 변경