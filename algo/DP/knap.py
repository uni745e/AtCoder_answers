# coding:utf-8

"""
ナップザック問題

例
input
6 8
2 3
1 2
3 6
2 1
1 3
5 85

output
91
(3,6)と(5,85)を選んだときが最大
"""


def inpl(): return list(map(int, input().split()))


def knapsack(N, W, weight, value):
    # 初期化
    inf = float("inf")
    dp = [[-inf for _ in range(W + 1)] for _ in range(N + 1)]
    for i in range(W + 1): dp[0][i] = 0

    # DP
    for i in range(N):
        for w in range(W + 1):
            if w >= weight[i]:
                dp[i + 1][w] = max(dp[i][w - weight[i]] + value[i], dp[i][w])
            else:
                dp[i + 1][w] = dp[i][w]
        # for j in range(N+1):
        # print(i,dp[j][:])
    return dp


N, W = inpl()

weight = []
value = []
for _ in range(N):
    w, v = inpl()
    weight.append(w)
    value.append(v)

dp = knapsack(N, W, weight, value)
# print(dp)
print(dp[-1][-1])
