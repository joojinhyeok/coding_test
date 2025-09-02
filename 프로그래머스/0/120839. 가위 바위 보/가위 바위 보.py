def solution(rsp):
    answer = ''
    # 가위바위보 이기는 경우 매핑
    a = {'2':'0', '0':'5', '5':'2'}
    for i in rsp:
        answer += a[i]
    return answer