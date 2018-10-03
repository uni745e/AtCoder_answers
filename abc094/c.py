# coding:utf-8

INF = float('inf')


def inpl(): return list(map(int, input().split()))


N = int(input())
X = inpl()
Y = sorted(X[:])
median_l = Y[N // 2 - 1]
median_r = Y[N // 2]

for x in X:
    if x <= median_l:
        print(median_r)
    else:
        print(median_l)
