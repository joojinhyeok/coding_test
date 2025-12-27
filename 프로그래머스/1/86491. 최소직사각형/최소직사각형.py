def solution(sizes):
    w = 0
    h = 0
    
    for i in sizes:
        w = max(w, max(i)) # 60 -> 70 -> 70 -> 80
        h = max(h, min(i)) # 50 -> 50 -> 50 -> 50
    
    return w * h