def solution(cipher, code):
    answer = ''
    for i in range(code, len(cipher) + 1, code):
        # 0부터 숫자가 시작하므로 i-1을 해야함
        answer += cipher[i-1]
    return answer

    # answer = cipher[code-1::code]
    # return answer
