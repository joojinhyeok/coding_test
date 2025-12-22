def solution(number):
    answer = 0
    length = len(number)
    
    # 첫 번째 학생 뽑기 (처음부터 끝까지)
    for i in range(length):
        # 두 번째 학생 뽑기 (첫 번째 학생의 다음부터 끝까지)
        for j in range(i + 1, length):
            # 세 번째 학생 뽑기 (두 번째 학생의 다음부터 끝까지)
            for k in range(j + 1, length):
                
                # 세 명의 합이 0인지 확인
                if number[i] + number[j] + number[k] == 0:
                    answer += 1
                    
    return answer

# 라이브러리 사용
# from itertools import combinations

# def solution(number):
#     answer = 0
    
#     # number 리스트에서 3개를 뽑는 모든 경우의 수(three)를 하나씩 꺼냄
#     for three in combinations(number, 3):
#         # 뽑힌 3명의 합(sum)이 0이면 카운트
#         if sum(three) == 0:
#             answer += 1
            
#     return answer