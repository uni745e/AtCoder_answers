# coding:utf-8

import sys
from collections import Counter


input = sys.stdin.readline


def inpl(): return list(map(int, input().split()))


def solve(N, V):
    v_even = [V[i] for i in range(0, N, 2)]
    v_odd = [V[i] for i in range(1, N, 2)]

    # 出現回数の多い上位2つの要素と出現回数を取得
    v_even_most = Counter(v_even).most_common()[:2]
    v_odd_most = Counter(v_odd).most_common()[:2]

    # 最頻値が被っていなければそのまま採用
    if v_even_most[0][0] != v_odd_most[0][0]:
        return N - v_even_most[0][1] - v_odd_most[0][1]
    else:
        # 数字が1種類しか登場しない場合は、0を追加
        # list index out of range対策
        if len(v_even_most) == 1 or len(v_odd_most) == 1:
            v_even_most.append((0, 0))
            v_odd_most.append((0, 0))

        # 書き換え回数が少ない方を採用
        return N - max(v_even_most[0][1] + v_odd_most[1][1],
                       v_even_most[1][1] + v_odd_most[0][1])


N = int(input())
V = inpl()
print(solve(N, V))
