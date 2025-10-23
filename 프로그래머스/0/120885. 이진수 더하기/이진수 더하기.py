def solution(bin1, bin2):
    # 1. 'int(문자열, 2)'를 사용해 10진수 숫자로 변환
    dec1 = int(bin1, 2)
    dec2 = int(bin2, 2)
    
    # 2. 10진수끼리 그냥 더하기
    sum_dec = dec1 + dec2
    
    # 3. 'bin()'을 사용해 다시 2진수 문자열로 변환
    # bin(5)의 결과는 '0b101' 이렇게 앞에 '0b'가 붙음
    answer_with_prefix = bin(sum_dec)
    
    # 4. 앞에 붙은 '0b' 두 글자를 잘라내고 반환
    # [2:]는 "인덱스 2번부터 끝까지"라는 뜻
    answer = answer_with_prefix[2:]
    
    return answer