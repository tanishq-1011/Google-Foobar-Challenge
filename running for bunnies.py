from itertools import permutations


def floyd_warshall(times):
    dp = times
    for k in range(len(times)):
        for i in range(len(times)):
            for j in range(len(times)):
                if(dp[i][j] > dp[i][k]+dp[k][j]):
                    dp[i][j] = dp[i][k]+dp[k][j]
    for i in range(len(times)): 
        if dp[i][i] < 0:
            return False

    return dp


def solution(times, times_limit):

    dp = floyd_warshall(times)

    ans = []
    if dp == False:
        return [i for i in range(0, len(times)-2)]

    order_of_bunny = list(permutations(range(1, len(times)-1)))

    power_set_size = 2**(len(times)-2)

    for l in order_of_bunny:

        for i in range(power_set_size): 

            bunny_picked = []
            current = 0
            cost = 0
            for j in l: 

                if i & (1 << (j-1)):
                    cost += dp[current][j]
                    bunny_picked.append(j-1)
                    current = j

            cost += dp[current][len(times)-1]

            if cost <= times_limit: 
                if len(bunny_picked) > len(ans):
                    ans = bunny_picked
                elif len(bunny_picked) == len(ans):
                    for k in range(len(ans)):
                        if bunny_picked[k] < ans[k]:
                            ans = bunny_picked
                            break
                        elif bunny_picked[k] > ans[k]:
                            break

    ans.sort()
    return ans