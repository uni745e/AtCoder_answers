# coding:utf-8

import sys
from collections import Counter


input = sys.stdin.readline
INF = float('inf')
MOD = 10 ** 9 + 7


def inpl(): return list(map(int, input().split()))


# Counterを使ったD - Candy Distributionの解法
def solve(N, M, A):
    # 累積和S (mod M)を求める
    S = [0]
    for i in range(N):
        S.append((S[-1] + A[i]) % M)

    ans = 0
    # 各要素の個数を数える
    for v in Counter(S).values():
        # v個から2個選ぶ組み合わせ
        ans += v * (v - 1) // 2

    return ans


N, M = inpl()
A = inpl()
print(solve(N, M, A))
