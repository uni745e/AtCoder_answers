# coding:utf-8

INF = float('inf')


def inpl(): return list(map(int, input().split()))


N = int(input())
A = inpl()

if sum(A) % N != 0:
    print(-1)
else:
    standard_num = sum(A) // N
    B = [A[i] - standard_num for i in range(N)]
    C = [0]
    for i in range(N):
        C.append(C[-1] + B[i])
    del C[0]

    left = 0
    ans = 0
    for right in range(N):
        if C[right] == 0:
            ans += right - left
            left = right + 1
    print(ans)
