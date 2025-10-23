def solution(numlist, n):
    # sorted 함수의 key를 람다(lambda) 함수로 지정
    # 1순위: n과의 거리 (abs(x - n)) - 거리가 가까운 순(오름차순)
    # 2순위: 원래 값 (-x) - 1순위(거리)가 같으면, -x가 작은 순 (즉, x가 큰 순, 내림차순)
    # lambda는 이름 없는 함수를 만드는 역할
    # : 를 기준으로 앞에 x는 함수가 입력받을 값으로 numlist의 원소를 의미함
    # 뒤 abs(x-n), -x는 반환할 값을 의미
    answer = sorted(numlist, key=lambda x: (abs(x - n), -x))
    return answer