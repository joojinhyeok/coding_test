def solution(nums):
    target = len(nums) // 2
    target2 = len(set(nums))
    
    return min(target, target2)