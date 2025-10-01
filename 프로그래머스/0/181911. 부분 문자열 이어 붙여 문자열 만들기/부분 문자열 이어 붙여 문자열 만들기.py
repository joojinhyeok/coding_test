def solution(my_strings, parts):
    answer = []
    # 1. enumerate로 my_strings의 인덱스(i)와 값(string)을 가져옴
    for i, string in enumerate(my_strings):
        # 2. i번째 인덱스를 이용해 parts에서 s, e 값을 가져옴
        s, e = parts[i]
        
        # 3. i번째 string을 s부터 e까지 잘라서 리스트에 추가 (e 포함해야 하므로 +1)
        answer.append(string[s:e+1])
        
    # 4. 조각들을 하나의 문자열로 합쳐서 반환
    return "".join(answer)