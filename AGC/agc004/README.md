# AGC004
https://beta.atcoder.jp/contests/agc004/tasks

# A
一辺でも偶数であれば0  
無ければ昇順ソートして1番小さい辺と2番めに小さい辺の積が答えになる

# B
N >_ 2000 だったので、想定解がO(N**2)だとは思った  
シフトする回数を0 ~ N - 1回と変えていく  
シフト回数をkとすると、i色のスライムは`min([ai, ai-1, ..., ai-k])`で作成できる  
これをbiとした時、全体でかかる時間は `time = sum(bi) + k * x`[i = 0 ~ N - 1]となる

# C
平面のロシアゲー  
赤いマスをA、青いマスをBで表す  
oがAではEの形に、Bではヨの形になるように初期化する  
例:  
A  
oooooox  
oxxxxxx  
oooooox  
oxxxxxx  
oooooox  

B  
xxxxxxo  
xoooooo  
xxxxxxo  
xoooooo  
xxxxxxo  

紫色になる部分はA、Bの両方をoにする  
キモは「最も外側のマスは紫色ではない」ということ

# D


# わかったこと

- 最小値の求め方  
	- `min(a1, a2, ...ak)`：後でまとめて
	- `X[i] = min(X[i], A[i - k])`：1つ前の値と比較して常に最小値を更新
	- O(N) -> O(1)