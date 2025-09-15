def solution(numbers):
    sort_numbers = sorted(numbers, reverse=True)
    # print(sort_numbers) -> 내림차순 정렬
    # numbers.sort() -> 오름차순 정렬
    return sort_numbers[0] * sort_numbers[1]