def solution(sides):
    # 가장 짧은 변의 길이를 찾아서 2를 곱하고 1을 빼면 끝!
    return 2 * min(sides) - 1

# max(sides)가 가장 길 때
# x의 범위: max(sides) - min(sides) < x <= max(sides)
# max(sides) - (max(sides) - min(sides)) -> x의 개수

# x가 가장 길 때
# x의 범위: max(sides) < x < max(sides) + min(sides)
# max(sides) + min(sides) - max(sides) - 1 -> x의 개수