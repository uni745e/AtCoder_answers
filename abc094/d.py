# coding:utf-8

INF = float('inf')


def inpl(): return list(map(int, input().split()))


N = int(input())
A = inpl()

n = max(A)
r = max(A)
tmp = 0
for i in range(N):
    a = A[i]
    if a == n: continue
    if a < n - a: a = n - a
    if tmp <= n - a:
        r = A[i]
        tmp = n - a

print(n, r)
