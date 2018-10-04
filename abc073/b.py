# coding:utf-8

INF = float('inf')


def inpl(): return list(map(int, input().split()))


N = int(input())
seat = [False] * 100000
for i in range(N):
    l, r = inpl()
    for j in range(l - 1, r):
        seat[j] = True

ans = 0
for s in seat:
    if s: ans += 1

print(ans)