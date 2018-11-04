# coding:utf-8

import sys
from collections import Counter

input = sys.stdin.readline
INF = float('inf')


def inpl(): return list(map(int, input().split()))


N = int(input())
S = input().strip()

num_E = Counter(S)['E']  # リーダより右側にいるEの数
num_W = 0  # リーダより左側にいるWの数

ans = N - 1
for i in range(N):
    if S[i] == 'E':
        num_E -= 1
        ans = min(ans, num_W + num_E)
    else:
        ans = min(ans, num_W + num_E)
        num_W += 1

print(ans)
