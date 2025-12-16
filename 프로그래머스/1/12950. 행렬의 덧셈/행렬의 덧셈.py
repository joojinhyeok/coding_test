def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        sum = []
        
        for j in range(len(arr1[0])):
            s = arr1[i][j] + arr2[i][j]
            sum.append(s)
            
        answer.append(sum)
    return answer