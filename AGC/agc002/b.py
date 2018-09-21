# coding:utf-8

INF = float('inf')


def inpl(): return list(map(int, input().split()))


N, M = inpl()
# move = [inpl() for _ in range(M)]

ans = [0 for _ in range(N)]
ans[0] = 1
box = [1 for _ in range(N)]
# print(ans, box)
for i in range(M):
    # x, y = move[i]
    x, y = inpl()
    box[x - 1] -= 1
    box[y - 1] += 1
    if ans[x - 1]:
        ans[y - 1] = 1
        if box[x - 1] == 0:
            ans[x - 1] = 0
    # print(ans, box)


print(sum(ans))