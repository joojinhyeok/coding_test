def solution(s):
    p = 0
    y = 0
    s = s.upper()
    if 'P' not in s and 'Y' not in s:
        return True
    
    for i in s:
        if i == 'P':
            p += 1
        elif i == 'Y':
            y += 1
    
    if p == y:
        return True
    else: return False