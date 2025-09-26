def solution(polynomial):
    # 2. x의 계수와 상수항을 저장할 변수 초기화
    x_coeff = 0
    constant = 0
    
    # 1. " + " 기준으로 쪼개기
    terms = polynomial.split(' + ')
    
    # 3. 각 항을 순회하며 계산
    for term in terms:
        if 'x' in term:
            # x항 처리
            if term == 'x':
                x_coeff += 1
            else:
                # 'x'를 제외한 앞부분이 계수
                x_coeff += int(term[:-1])
        else:
            # 상수항 처리
            constant += int(term)
            
    # 4. 결과 문자열 조합하기
    answer_parts = []
    
    # x항 부분 만들기
    if x_coeff > 0:
        if x_coeff == 1:
            answer_parts.append("x")
        else:
            answer_parts.append(f"{x_coeff}x")
            
    # 상수항 부분 만들기
    if constant > 0:
        answer_parts.append(str(constant))
        
    # 최종 결과 조합
    return " + ".join(answer_parts)