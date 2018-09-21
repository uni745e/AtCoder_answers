# coding:utf-8


def inpl(): return list(map(int, input().split()))


H, W = inpl()
board = []
for i in range(H):
    board.append(inpl())

ans = []
cnt = 0
for h in range(H):
    if h % 2 == 0:
        for w in range(W):
            if board[h][w] % 2 == 1:
                board[h][w] -= 1
                if w + 1 < W:
                    board[h][w + 1] += 1
                    ans.append([h + 1, w + 1, h + 1, w + 2])
                    cnt += 1
                elif h + 1 < H:
                    board[h + 1][w] += 1
                    ans.append([h + 1, w + 1, h + 2, w + 1])
                    cnt += 1

    else:
        for w in range(W)[::-1]:
            if board[h][w] % 2 == 1:
                board[h][w] -= 1
                if 0 < w:
                    board[h][w - 1] += 1
                    ans.append([h + 1, w + 1, h + 1, w])
                    cnt += 1
                elif h + 1 < H:
                    board[h + 1][w] += 1
                    ans.append([h + 1, w + 1, h + 2, w + 1])
                    cnt += 1

print(cnt)

for a in ans:
    print(' '.join(map(str, a)))
