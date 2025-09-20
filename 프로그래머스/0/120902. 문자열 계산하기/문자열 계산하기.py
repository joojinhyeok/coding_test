def solution(my_string):
    # print(my_string.split(' '))
    a = my_string.split(' ')
    answer = int(a[0])
    for i in range(1, len(a), 2):
        # 연산자 저장
        operator = a[i]
        # 더해줄 숫자 저장
        num = a[i+1]
        
        if operator == '+':
            answer += int(num)
        else:
            answer -= int(num)
            
    return answer