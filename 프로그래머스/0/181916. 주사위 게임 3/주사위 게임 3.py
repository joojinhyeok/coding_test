def solution(a, b, c, d):
    # 1. 네 숫자를 리스트에 담기
    nums = [a, b, c, d]
    
    # 2. 각 숫자의 개수를 딕셔너리로 세기
    counts = {}
    for n in nums:
        counts[n] = counts.get(n, 0) + 1
        
    # 3. 딕셔너리의 key(나온 숫자)들을 리스트로 만듦
    keys = list(counts.keys())

    # 경우의 수에 따라 점수 계산
    # 1. 네 주사위가 모두 같은 경우 (종류 1개)
    if len(keys) == 1:
        p = keys[0]
        return 1111 * p
        
    # 2. 세 주사위가 같거나, 두 개씩 두 쌍이 같은 경우 (종류 2개)
    elif len(keys) == 2:
        # 2-1. 세 주사위가 같은 경우
        if 3 in counts.values():
            # 개수가 3인 숫자가 p, 1인 숫자가 q
            p = [k for k, v in counts.items() if v == 3][0]
            q = [k for k, v in counts.items() if v == 1][0]
            return (10 * p + q) ** 2
        # 2-2. 두 개씩 두 쌍이 같은 경우
        else:
            p, q = keys[0], keys[1]
            return (p + q) * abs(p - q)

    # 3. 두 주사위만 같은 경우 (종류 3개)
    elif len(keys) == 3:
        # 개수가 1인 숫자 두 개가 q, r
        q_r = [k for k, v in counts.items() if v == 1]
        return q_r[0] * q_r[1]
        
    # 4. 네 주사위가 모두 다른 경우 (종류 4개)
    else: # len(keys) == 4
        return min(nums)