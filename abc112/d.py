# coding:utf-8


def inpl(): return list(map(int, input().split()))


N, M = inpl()

A = 1
ans = 1
while A * A <= M:
    # 約数判定
    if M % A != 0:
        A += 1
        continue
    B = M // A

    # dはM // N以下
    if A * N <= M:
        ans = max(ans, A)
    # M = A * BでAはsqrt(M)までしか探索しない
    # 答えがsqrt(M)以上M // N以下のときWAになるので
    # AだけではなくBでも判定を行う
    # だから全探索の時は必要なかったのか...
    if B * N <= M:
        ans = max(ans, B)

    A += 1

print(ans)
