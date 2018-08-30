# coding:utf-8

import itertools

INF = float('inf')


def inpl(): return list(map(int, input().split()))


N, M = inpl()

X = []
Y = []
Z = []
cakes = []
for i in range(N):
    x, y, z = inpl()
    X.append(x)
    Y.append(y)
    Z.append(z)
    cakes.append([x, y, z])

ans = -INF
sign = [-1, 1]


# for a in sign:
#     for b in sign:
#         for c in sign:
#             score = []
#             for i in range(N):
#                 tmp = a * X[i] + b * Y[i] + c * Z[i]
#                 score.append(tmp)
#             score.sort()
#             score.reverse()
#             ans = max(ans, sum(score[:M]))
#
# print(ans)

# itertoolsを使った解法。ネストが浅くて良い
for a, b, c in itertools.product(*([sign] * 3)):
    score = [a * x + b * y + c * z for x, y, z in cakes]
    score.sort()
    score.reverse()
    ans = max(ans, sum(score[:M]))

print(ans)
