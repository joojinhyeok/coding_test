def solution(my_string, queries):
    # 1. 문자열을 리스트로 변환
    s_list = list(my_string)
    
    # 2. 쿼리를 하나씩 처리
    for s, e in queries:
        # 3. s부터 e까지의 부분을 잘라내서 뒤집음
        part_to_reverse = s_list[s:e+1]
        reversed_part = part_to_reverse[::-1]
        
        # 4. 뒤집은 조각으로 원래 리스트의 해당 부분을 교체
        s_list[s:e+1] = reversed_part
        
    # 5. 리스트를 다시 문자열로 합쳐서 반환
    return "".join(s_list)