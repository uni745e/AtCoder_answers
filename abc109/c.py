# coding:utf-8

INF = float('inf')


def inpl(): return list(map(int, input().split()))


def gcd(x, y):
    if x % y == 0:
        return y
    else:
        x, y = y, x % y
        return gcd(x, y)


N, S = inpl()
X = inpl()
X = [abs(X[i] - S) for i in range(N)]

if len(X) == 1:
    ans = X[0]
else:
    X.sort()
    ans = gcd(X[0], X[1])
    for i in range(2, N):
        ans = gcd(ans, X[i])

print(ans)