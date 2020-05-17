
from itertools import combinations

def solution(num_buns, num_required):
    b = [[] for i in range(num_buns)]
    if num_required == 0:
        return b
    t = 0
    for c in combinations(b, num_buns - num_required + 1):
        for i in c:
            i.append(t)
        t += 1
    return num_buns