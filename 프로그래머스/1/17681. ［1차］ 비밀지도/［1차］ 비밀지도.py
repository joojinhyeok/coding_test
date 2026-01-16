def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        # 1. 두 숫자를 비트 OR 로 합침
        # or 연산은 bin() 사용 안해도 자동 계산
        combined = arr1[i] | arr2[i]
        
        # 2. 이진수로 변환 후 앞의 '0b' 제거
        # 3. zfill(n)으로 자릿수(n)만큼 0 채우기
        binary_str = bin(combined)[2:].zfill(n)
        
        # 4. 1은 벽(#), 0은 공백( )으로 바꾸기 (문제 요구사항)
        row = binary_str.replace('1', '#').replace('0', ' ')
        answer.append(row)
        
    return answer