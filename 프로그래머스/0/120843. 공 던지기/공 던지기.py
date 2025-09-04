def solution(numbers, k):
    a =((k-1) * 2) % len(numbers)
    return numbers[a]