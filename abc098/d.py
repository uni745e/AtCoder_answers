# coding:utf-8

INF = float('inf')


def inpl(): return list(map(int, input().split()))


N = int(input())

A = inpl()
# tmp = max(A)
# val_limit = 1
# while tmp > val_limit:
#     val_limit *= 2

right = 0
res = 0
# res_xor = None
ans = 0
for left in range(N):
    # while right < N and res + A[right] < val_limit:
    #     res += A[right]
    #
    #     if res_xor is None:
    #         res_xor = A[right]
    #     else:
    #         res_xor ^= A[right]
    #
    #     if res == res_xor and left != right:
    #         print(left, right, res)
    #         ans += 1
    #     right += 1

    while right < N and res + A[right] == res ^ A[right]:
        res += A[right]
        right += 1

    ans += right - left

    if left == right:
        right += 1
    else:
        res -= A[left]

print(ans)
