def solution(picture, k):
    answer = []
    for i in picture:
        new_row = ""
        
        # ex) i = ".xx." -> new_row = "..xxxx.."
        for j in i:
            new_row += j * k

        # k번 반복
        for _ in range(k):
            answer.append(new_row)
            
    return answer