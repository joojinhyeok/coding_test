def solution(numbers):
    a =  ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    # enumerate()는 순서가 있는 자료형(list, set, tuple, dictionary, string)을 입력으로 받았을 때, 
    # 인덱스와 값을 포함하여 리턴
    for i, num in enumerate(a):
        # replace()는 문자열을 변경하는 함수
        # replace('hi', 'hello') -> hi가 hello로 변경
        numbers = numbers.replace(num, str(i))
    return int(numbers)