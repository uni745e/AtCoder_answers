# coding:utf-8

import sys


input = sys.stdin.readline
INF = float('inf')


def inpl(): return list(map(int, input().split()))


N = int(input())

if N == 1:
    ans = ['X']
elif N == 2:
    ans = [['X', '.'], ['.', 'X']]
else:
    ans = [['.'] * N for _ in range(N)]
    tmp = [1, 3, 0, 2, 4]
    for i in range(N):
        for j in range(tmp[i % 5], N, 5):
            ans[i][j] = 'X'

    # 上下左右の端の処理
    for j in range(4, N, 5):
        ans[0][j] = 'X'
    for i in range(4, N, 5):
        ans[i][0] = 'X'
    tmp = [2, 5, 3, 1, 4]
    for i in range(tmp[N % 5], N, 5):
        ans[i][-1] = 'X'
    tmp = [1, 3, 0, 2, 4]
    for j in range(tmp[N % 5], N, 5):
        ans[-1][j] = 'X'

for a in ans:
    print(''.join(map(str, a)))

