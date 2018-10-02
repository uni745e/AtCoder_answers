# coding:utf-8

INF = float('inf')
MOD = 10 ** 9 + 7


def inpl(): return list(map(int, input().split()))


S = input()

A = [-INF for _ in range(len(S))]
C = A[:]
Q = A[:]

A[0] = 1 if S[0] == 'A' else 0
C[0] = 1 if S[0] == 'C' else 0
Q[0] = 1 if S[0] == '?' else 0

for i in range(1, len(S)):
    A[i] = A[i - 1] + 1 if S[i] == 'A' else A[i - 1]
    C[i] = C[i - 1] + 1 if S[i] == 'C' else C[i - 1]
    Q[i] = Q[i - 1] + 1 if S[i] == '?' else Q[i - 1]

# TLEになるので3^X%MODを予め計算
pow_three = [1]
for i in range(Q[-1]):
    tmp = pow_three[-1] * 3
    tmp %= MOD
    pow_three.append(tmp)

ans = 0
for i in range(1, len(S) - 1):
    if S[i] == 'A' or S[i] == 'C':
        continue

    # A, B, Cの個数
    tmp = Q[i - 1] + Q[-1] - Q[i]
    if tmp < 0: tmp = 0
    ans += A[i - 1] * (C[-1] - C[i]) * pow_three[tmp]
    # ?, B, Cの個数
    tmp = Q[i - 1] - 1 + Q[-1] - Q[i]
    if tmp < 0: tmp = 0
    ans += Q[i - 1] * (C[-1] - C[i]) * pow_three[tmp]
    # A, B, ?の個数
    tmp = Q[i - 1] + Q[-1] - Q[i] - 1
    if tmp < 0: tmp = 0
    ans += A[i - 1] * (Q[-1] - Q[i]) * pow_three[tmp]
    # ?, B, ?の個数
    tmp = Q[i - 1] + Q[-1] - Q[i] - 2
    if tmp < 0: tmp = 0
    ans += Q[i - 1] * (Q[-1] - Q[i]) * pow_three[tmp]

    ans %= MOD

print(ans)
