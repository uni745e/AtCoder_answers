# coding:utf-8

INF = float('inf')


def inpl(): return list(map(int, input().split()))


n = int(input())
A = inpl()
tmp = [i + 1 for i in range(n)]

B = [A[i] - tmp[i] for i in range(n)]
B.sort()
b = B[n // 2]

ans = 0
for i in range(n):
    ans += abs(B[i] - b)

print(ans)
