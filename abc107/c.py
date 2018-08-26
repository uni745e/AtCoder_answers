# coding:utf-8

INF = float('inf')


def inpl(): return list(map(int, input().split()))


N, K = inpl()
X = inpl()

A = [0]
B = []
for i in range(N):
    if X[i] >= 0:
        A.append(X[i])
    else:
        B.append(-X[i])
B.append(0)
B = B[::-1]

ans = INF
for i in range(K + 1):
    cost = INF
    j = K - i
    if i > len(A) - 1 or j > len(B) - 1: continue

    cost = A[i] + B[j] + min(A[i], B[j])
    ans = min(ans, cost)

print(ans)
