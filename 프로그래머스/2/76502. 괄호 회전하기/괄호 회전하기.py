def solution(s):
    answer = 0
    matches = {')': '(', '}': '{', ']': '['}
    
    # len(s)만큼 회전해서 스택에 넣고 비교하기
    for i in range(len(s)):
        new_s = s[i:] + s[:i] # 왼쪽으로 i만큼 회전
        
        stack = []
        is_valid = True  # 이번 회전이 올바른지 체크
        
        for char in new_s:
            # 여는 괄호면 스택에 넣기
            if char in "({[":
                stack.append(char)
            # 닫는 괄호면 검사
            else:
                # 스택이 비었거나, 짝이 안 맞으면 실패
                if not stack or stack[-1] != matches[char]:
                    is_valid = False
                    break
                else:
                    stack.pop()
        
        # 2번째 반복문 끝난 후: 스택이 비어있고, 실패 안 했으면 성공
        if is_valid and not stack:
            answer += 1
    return answer