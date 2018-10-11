# coding:utf-8


INF = float('inf')


def inpl(): return list(map(int, input().split()))


N = int(input()) + 1
cnt = (len(bin(N)) - 2) % 2
w = [[0, 1], [1, 0]]

x = 1
player = 0  # 0: Takahashi, 1: Aoki
while x < N:
    x += x + w[cnt][player]
    player ^= 1

if player:
    print('Aoki')
else:
    print('Takahashi')

# ゲーム木の描画関数
# def left_func(n): return 2 * n
#
#
# def right_func(n): return 2 * n + 1
#
#
# def write_bi_tree(func_l, func_r, li_i, l, player):
#     if player:
#         print('T')
#     else:
#         print('A')
#     tmp = []
#     for i in range(len(li_i)):
#         if i >= l:
#             continue
#         il = func_l(li_i[i])
#         ir = func_r(li_i[i])
#         tmp.append(il)
#         tmp.append(ir)
#         print(il, end=' ')
#         print(ir, end=' ')
#         if i + 1 == len(li_i) // 2:
#             print('|', end=' ')
#
#     print('')
#     if min(tmp) < l:
#         if player:
#             write_bi_tree(func_l, func_r, tmp, l, False)
#         else:
#             write_bi_tree(func_l, func_r, tmp, l, True)
#     else:
#         return 0
#
# print(1)
# write_bi_tree(left_func, right_func, [1], N, True)
