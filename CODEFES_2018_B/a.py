# coding:utf-8

import sys


input = sys.stdin.readline
INF = float('inf')


def inpl(): return list(map(int, input().split()))


N = int(input())
cnt = 0
for i in range(1, 101):
    if i % N == 0:
        cnt += 1

print(100 - cnt)
