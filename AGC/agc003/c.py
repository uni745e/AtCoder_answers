# coding:utf-8

INF = float('inf')


def inpl(): return list(map(int, input().split()))


N = int(input())
A = [int(input()) for _ in range(N)]
B = sorted(A)
C = A[::2] + B[1::2]
D = set(C)
# count = 0
# for i in range(N):
#     tmp = B.index(A[i])
#     diff = abs(i - tmp)
#     if diff % 2 == 1:
#         count += 1

print(N - len(D))
