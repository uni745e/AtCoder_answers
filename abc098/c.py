# coding:utf-8

INF = float('inf')


def inpl(): return list(map(int, input().split()))


N = int(input())
S = input()

num_E = S[:].count('E')
num_W = S[:].count('W')


e = num_E
w = num_W
ans = INF
for s in S:
    cost = 0
    if s == 'E':
        e -= 1
        cost = e + (num_W - w)
    else:
        w -= 1
        cost = e + (num_W - w - 1)
    ans = min(ans, cost)

print(ans)
