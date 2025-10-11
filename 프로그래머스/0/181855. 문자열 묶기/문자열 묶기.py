def solution(strArr):
    counts = {}
    for i in strArr:
        l = len(i)
        counts[l] = counts.get(l, 0) + 1
    
    return max(counts.values())