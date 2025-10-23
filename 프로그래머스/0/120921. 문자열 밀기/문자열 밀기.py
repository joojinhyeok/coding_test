def solution(A, B):
    if A == B:
        return 0
    
    for i in range(1, len(A)):
        # 우측으로 밀기(맨 마지막 글자를 맨 앞으로 이동)
        # 1번밀었을 때 A == B가 되면 바로 i를 return 
        A = A[-1] + A[:-1]
    
        if A == B:
            return i 
    return -1