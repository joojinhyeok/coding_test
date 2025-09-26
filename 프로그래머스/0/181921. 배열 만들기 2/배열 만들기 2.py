def solution(l, r):
    answer = []
    for i in range(l, r + 1):
        s = str(i)
        is_valid = True 
        
        for char in s:
            if char != '0' and char != '5':
                is_valid = False
                break
        if is_valid:
            answer.append(i)

    if not answer:
        return [-1]
    else:
        return answer