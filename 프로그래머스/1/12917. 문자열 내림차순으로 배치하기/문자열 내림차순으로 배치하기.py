def solution(s):
    # 1. 문자열 s를 내림차순 정렬 (결과는 리스트 형태 ['g', 'f', 'e', ...])
    sorted_list = sorted(s, reverse=True)
    
    answer = "".join(sorted_list)
    
    return answer