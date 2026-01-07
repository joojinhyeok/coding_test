def solution(k, score):
    answer = []
    stack = []
    
    for i in score:
        stack.append(i)
        stack.sort()
        
        if len(stack) > k:
            stack.pop(0) # = stack.remove(min(stack)) / del stack[0]
        answer.append(stack[0])
    return answer