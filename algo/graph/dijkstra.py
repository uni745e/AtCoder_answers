#coding:utf-8

'''
最短経路問題
Dijkstra法
'''

#グラフは蟻本p96のもの
adjacent = [[0, 2, 5, 0, 0, 0, 0],  #A
            [2, 0, 4, 6, 10, 0, 0], #B
            [5, 4, 0, 2, 0, 0, 0],  #C
            [0, 6, 2, 0, 0, 1, 0],  #D
            [0, 10, 0, 0, 0, 3, 5], #E
            [0, 0, 0, 1, 3, 0, 9],  #F
            [0, 0, 0, 0, 5, 9, 0]]  #G

MAX_SIZE = 7
MAX_VALUE = 10**9

visited = [False for _ in range(MAX_SIZE)]# 探索済みの頂点を記憶
cost = [MAX_VALUE for _ in range(MAX_SIZE)]#頂点startからの各頂点の最小コストを格納
prev = [None for _ in range(MAX_SIZE)]#各頂点の直前に通った頂点を記憶

#出発点から各頂点までの最小コストと直前に通った頂点を出力
def print_path():
    for i in range(MAX_SIZE):
        print('{}: prev = {}, cost = {}'.format(i+1, prev[i]+1, cost[i]))

def dijkstra(start):
    cost[start] = 0
    prev[start] = start
    path = [str(start+1)]
    while True:
        min = MAX_VALUE
        next = -1
        visited[start] = True
        #頂点の選択
        for i in range(MAX_SIZE):
            if visited[i]: continue#探索済みは飛ばす
            if adjacent[start][i]:#頂点startと接続されている頂点を確認(0でなければ接続されている)
                dis = cost[start] + adjacent[start][i]
                if dis < cost[i]:
                    cost[i] = dis
                    prev[i] = start
            if min > cost[i]:#頂点startと接続されている頂点で一番コストの低い頂点を次に探索する
                min = cost[i]
                next = i
        start = next
        path.append(str(next+1))
        if next == -1: break
    print(' -> '.join(path))
    print_path()

if __name__ == '__main__':
    dijkstra(0)#頂点Aが出発点
