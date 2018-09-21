# coding:utf-8

INF = float('inf')


def inpl(): return list(map(int, input().split()))


N = int(input())
A = [int(input()) for _ in range(N)]

ans = 0
prev = 0
for i in range(N):
    if prev == 1 and A[i] > 0:
        A[i] -= 1
        ans += 1
    q, mod = divmod(A[i], 2)
    # print(q, mod, prev)
    ans += q
    prev = mod

print(ans)