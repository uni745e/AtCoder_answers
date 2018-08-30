# coding:utf-8


def inpl(): return list(map(int, input().split()))


n = int(input())
A = inpl()

ans = 0
for i in range(n):
    tmp = A[i]
    while tmp % 2 == 0:
        tmp //= 2
        ans += 1

print(ans)

# # 別解
# # 偶数の要素A[k]を一つ見つけて2で割る。
# # i = k以外の要素を全て3倍。
# ans = 0
# while True:
#     for i in range(n):
#         if A[i] % 2 == 0:
#             tmp = i
#             A[i] //= 2
#             break
#     else:
#         break
#
#     ans += 1
#     for i in range(n):
#         if i != tmp:
#             A[i] *= 3
#
# print(ans)
