def solution(n_str):
    for i, j in enumerate(n_str):
        if j != '0':
            # [:] -> 슬라이싱은 기존 타입 그대로 반환
            return n_str[i:]
    return '0'