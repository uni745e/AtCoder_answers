# coding:utf-8

INF = float('inf')


def inpl(): return list(map(int, input().split()))


n = int(input())
s = input()

a, b = inpl()

if a == b:
    print('Yes')
else:
    print('No')
