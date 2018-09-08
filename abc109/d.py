# coding:utf-8

INF = float('inf')


def inpl(): return list(map(int, input().split()))


H, W = inpl()
mass = []
for i in range(H):
    mass.append(inpl())

count = 0
ans = []
for i in range(H):
    for j in range(W):
        if mass[i][j] & 1:
            if j < W - 1:
                count += 1
                ans.append([i + 1, j + 1, i + 1, j + 2])
                mass[i][j] -= 1
                mass[i][j + 1] += 1
            elif i < H - 1:
                count += 1
                ans.append([i + 1, j + 1, i + 2, j + 1])
                mass[i][j] -= 1
                mass[i + 1][j] += 1

print(count)
for a in ans:
    print(' '.join(map(str, a)))
