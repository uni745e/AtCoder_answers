# coding:utf-8


def inpl(): return list(map(int, input().split()))


N, M = inpl()
A = inpl()

S = [0]
for i in range(N):
    S.append((S[-1] + A[i]) % M)
del S[0]

D = dict()
D[0] = 0
for i in range(N):
    if S[i] in D:
        D[S[i]] += 1
    else:
        D[S[i]] = 1
print(D)
ans = 0
for num in D:
    tmp = D[num]
    # cmb(x, 2)を計算
    ans += tmp * (tmp - 1) // 2

# l, rが等しく（1箱で）分配できるパターンを最後に足す
ans += D[0]
print(ans)
