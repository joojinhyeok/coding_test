def solution(n):
    # 1. "수박"을 n번 반복하면 무조건 n보다 긴 문자열이 됨
    # 예: n=3 -> "수박수박수박" (길이 6)
    full_string = "수박" * n
    
    # 2. 앞에서부터 n개만 자름
    # 예: "수박수박수박"[:3] -> "수박수"
    return full_string[:n]