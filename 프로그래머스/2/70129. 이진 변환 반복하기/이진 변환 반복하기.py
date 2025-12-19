def solution(s):
    loop_cnt = 0  # 변환 횟수
    zero_cnt = 0  # 제거된 0의 개수
    
    # s가 "1"이 될 때까지 계속 반복
    while s != "1":
        # 0의 개수 만큼 전체 길이에서 빼주고 2진수 변환
        
        # 0의 개수 세기
        num_zeros = s.count('0')
        zero_cnt += num_zeros
        
        # 0을 뺀 나머지 길이 구하기
        # (전체 길이 - 0의 개수) = (1의 개수) = (다음 단계로 넘어갈 길이)
        length = len(s) - num_zeros
        
        # bin()을 활용해 문자열을 2진수로 변환
        # bin(4) -> '0b100' 이므로 앞의 '0b'를 떼기 위해 [2:] 사용
        s = bin(length)[2:]
        
        # 4. 변환 횟수 증가
        loop_cnt += 1
        
    return [loop_cnt, zero_cnt]