# coding:utf-8

INF = float('inf')


def inpl(): return list(map(int, input().split()))


a, b = inpl()
if a * b % 2 == 1:
    print('Yes')
else:
    print('No')
