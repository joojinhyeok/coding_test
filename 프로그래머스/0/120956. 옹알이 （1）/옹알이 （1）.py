def solution(babbling):
    answer = 0
    w = ["aya", "ye", "woo", "ma"]

    for word in babbling:
        for speak in w:
            # w에 있는 단어(발음 가능한 단어)를 공백으로 치환
            word = word.replace(speak, ' ')
        
        # 모든 공백을 제거했을 때, 아무것도 남지 않으면 발음 가능한 단어입니다.
        if word.replace(' ', '') == '':
            answer += 1
            
    return answer