# coding:utf-8

INF = float('inf')


def inpl(): return list(map(int, input().split()))


A, B, X = inpl()

if A + B >= X >= A:
    print('YES')
else:
    print('NO')
