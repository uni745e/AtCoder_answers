# coding:utf-8


def inpl(): return list(map(int, input().split()))


N = int(input())
A = inpl()

A.sort()
print(A[-1] - A[0])
