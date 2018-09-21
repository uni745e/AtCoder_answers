# coding:utf-8

INF = float('inf')


def inpl(): return list(map(int, input().split()))


N, x = inpl()
A = inpl()

min_cost_s = 0
tmp = INF
for i in range(N):
    if A[i] < tmp:
        min_cost_s = i
        tmp = A[i]

A = A[min_cost_s:] + A[:min_cost_s]
B = [A[i] for i in range(N)]

ans = INF
for shift in range(N):
    for i in range(N):
        if i - shift >= 0:
            B[i] = min(B[i], A[i - shift])
    # print(B)

    ans = min(ans, shift * x + sum(B))

print(ans)
