# coding:utf-8

import sys
from operator import itemgetter

input = sys.stdin.readline
INF = float('inf')


def inpl(): return list(map(int, input().split()))


N, X = inpl()
AB = [inpl() for _ in range(N)]
AB.sort(key=itemgetter(1))
AB[-1][0] += X

ans = 0
for a, b in AB:
    ans += a * b

print(ans)
