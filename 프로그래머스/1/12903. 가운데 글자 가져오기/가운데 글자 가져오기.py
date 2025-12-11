def solution(s):
    answer = ''
    list_s = list(s)
    mid = len(s) // 2 
    
    if len(s) % 2 != 0:
        return list_s[mid]
    else:
        return list_s[mid-1] + list_s[mid]