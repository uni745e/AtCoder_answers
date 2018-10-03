# coding:utf-8

INF = float('inf')


def inpl(): return list(map(int, input().split()))


# # 2分探索でも解ける
# def binary_search(A, x):
#     low = 0
#     high = len(A) - 1
#     mid = (low + high) // 2
#
#     while low <= high:
#         print(mid)
#         if A[mid] == x:
#             break
#         elif A[mid] < x:
#             low = mid + 1
#         else:
#             high = mid - 1
#         mid = (low + high) // 2
#
#     if mid < 0:
#         return 0
#     else:
#         return mid


N, M, X = inpl()
A = inpl()

ans = 0
for i in range(M):
    if X < A[i]:
        break
    ans += 1

# ans = binary_search(A, X)

if ans > M - ans: ans = M - ans

print(ans)
