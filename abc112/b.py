# coding:utf-8

INF = float('inf')


def inpl(): return list(map(int, input().split()))


N, T = inpl()
X = []
for i in range(N):
    c, t = inpl()
    X.append([t, c])

X.sort()
ans = INF
for i in range(N):
    if X[i][0] > T:
        break
    if X[i][1] < ans:
        ans = X[i][1]

if ans == INF:
    print('TLE')
else:
    print(ans)
