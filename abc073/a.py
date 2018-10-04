# coding:utf-8

INF = float('inf')


def inpl(): return list(map(int, input().split()))


N = int(input())


if N // 10 == 9 or N % 10 == 9:
    print('Yes')
else:
    print('No')
