def solution(n, words):
    for i, word in enumerate(words):
        # 처음엔 패스
        if i == 0:
            continue
            
        # 앞 단어 가져오기    
        prev_word = words[i-1]
        
        # 앞 단어 맨 끝글자 != 현재 단어 첫글자
        # 현재 단어가 이미 나왔다면(words[:i])
        if (prev_word[-1] != word[0]) or (word in words[:i]):
            return [(i % n) + 1, (i // n) + 1]
        
    
    return [0, 0]