# coding:utf-8


INF = float('inf')


def inpl(): return list(map(int, input().split()))


N, K = inpl()

A = [i + 1 for i in range(N)]

num_K = 0
num_K_half = 0
for a in A:
    if K % 2 == 1:
        if a % K == 0:
            num_K += 1
    else:
        if a % K == 0:
            num_K += 1
        elif a % K == K // 2:
            num_K_half += 1

ans = num_K ** 3 + num_K_half ** 3
print(ans)

