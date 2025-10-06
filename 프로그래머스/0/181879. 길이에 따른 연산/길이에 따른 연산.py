def solution(num_list):
    answer = 0
    answer2 = 1
    if len(num_list) >= 11:
        return sum(num_list)
    else:
        for i in num_list:
            answer2 *= i
        return answer2