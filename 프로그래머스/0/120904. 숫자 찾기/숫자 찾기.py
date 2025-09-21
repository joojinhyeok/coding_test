def solution(num, k):
    str_num = str(num)
    str_k = str(k)
    if str_k in str_num:
        # 1부터 시작하므로 인덱스 + 1
        return str_num.find(str_k) + 1
    else:
        return -1