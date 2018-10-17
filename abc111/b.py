# coding:utf-8

INF = float('inf')


def inpl(): return list(map(int, input().split()))


N = int(input())

for i in range(1, 10):
    tmp = int(str(i)*3)
    if N <= tmp:
        print(tmp)
        break
