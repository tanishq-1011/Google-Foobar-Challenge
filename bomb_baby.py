def solution(a, b):
    ons = 0
    min_max = [int(a), int(b)]
    while min_max[0] > 1 and min_max[1] > 1:
        min_max.sort()
        if min_max[1] %  min_max[0] == 0:
            return "impossible"
        ons += min_max[1] // min_max[0]
        min_max[1]  = min_max[1] %  min_max[0]
    ons += max(min_max) - 1
    return str(ons)