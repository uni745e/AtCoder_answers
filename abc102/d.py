# coding:utf-8

INF = float('inf')


def inpl(): return list(map(int, input().split()))


N = int(input())

A = inpl()
B = A[:]

# 累積和
for i in range(1, N):
    B[i] = B[i] + B[i - 1]

ans = INF
mid_l = 0
mid_r = 2
t = B[-1]
for mid in range(1, N - 1):

    # |P - Q|と|R - S|がそれぞれ最小になるような区切りを見つける
    # while mid_l < mid and abs(2 * B[mid_l] - B[mid]) >= abs(2 * B[mid_l + 1] - B[mid]):
    #     mid_l += 1
    # while mid_r < N - 1 and abs(2 * B[mid_r] - B[mid] - t) >= abs(2 * B[mid_r + 1] - B[mid] - t):
    #     mid_r += 1

    # 上のような区切りは隣り合う2つの要素の和が区間全体の総和より大きくなる部分
    while B[mid] > B[mid_l] + B[mid_l + 1]:
        mid_l += 1
    while t > B[mid_r] + B[mid_r + 1] - B[mid]:
        mid_r += 1
    # print(mid_l, mid, mid_r)

    p = B[mid_l]
    q = B[mid] - p
    r = B[mid_r] - p - q
    s = t - r - p - q
    # print(p, q, r, s)

    ans = min(ans, max(p, q, r, s) - min(p, q, r, s))

print(ans)
