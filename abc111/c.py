# coding:utf-8

import numpy as np


INF = float('inf')


def inpl(): return list(map(int, input().split()))


N = int(input())
V = inpl()

A = [0 for _ in range(10**5+1)]
for i in range(0, N, 2):
    A[V[i]] += 1

B = [0 for _ in range(10**5+1)]
for i in range(1, N, 2):
    B[V[i]] += 1

A = np.array(A)
B = np.array(B)

if A.argmax() == B.argmax():
    A.sort()
    B.sort()
    tmp = max(A[-1] + B[-2], A[-2] + B[-1])
    ans = N - tmp
else:
    A.sort()
    B.sort()
    ans = N - A[-1] - B[-1]

print(ans)
