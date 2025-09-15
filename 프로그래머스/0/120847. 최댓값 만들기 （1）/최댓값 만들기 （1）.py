def solution(numbers):
    sort_numbers = sorted(numbers, reverse=True)
    # print(sort_numbers)
    
    return sort_numbers[0] * sort_numbers[1]