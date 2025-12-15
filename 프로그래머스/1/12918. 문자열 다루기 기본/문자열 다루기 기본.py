def solution(s):
    # isdigit() 활용
    return (len(s) == 4 or len(s) == 6) and s.isdigit()