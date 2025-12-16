def solution(s):
    answer = ''
    arr = list(map(int, s.split()))
    
    mn = str(min(arr))
    mx = str(max(arr))
    
    answer += mn + " " + mx
    return answer