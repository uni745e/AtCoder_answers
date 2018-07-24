# coding:utf-8
'''
n : 仕事の個数
S : 仕事の開始時間
T : 仕事の終了時間
ex.
5
1 2 4 6 8
3 5 7 9 10
'''

n = int(input())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

itv = []
for i in range(n):
    itv.append([T[i], S[i]])#終了時間が早い順にソートしたいのでTを1つ目の要素に
itv.sort()

ans = 0
t = 0
for i in range(n):
    if itv[i][1] > t:
        ans += 1
        t = itv[i][0]

print(ans)
