# coding:utf-8

import math

INF = float('inf')


def inpl(): return list(map(int, input().split()))

def comb(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


def pascal(x, y):
    if x == 1 or x == y:
        return 1
    else:
        return pascal(x - 1, y - 1) + pascal(x, y - 1)
        # return comb(y - 1, x - 1) + comb(y - 1, x)

N = int(input())
A = inpl()
mid = []

ans = []
for i in range(N):
    ans.append(pascal(i + 1, N))
print(ans)
print(A)

for i in range(N):
    tmp = [A[i] for _ in range(ans(i))]
    print(tmp)
    mid += tmp

print(len(mid))
print(mid[math.floor(len(mid)/2)])

