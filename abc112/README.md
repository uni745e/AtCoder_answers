# ABC112
https://beta.atcoder.jp/contests/abc112/tasks

# A - Programming Education
`N = int(input())`の値を見てやるだけ。

# B - Time Limit Exceeded
t <= Tの中でmin(ci)を出力するだけ  
\[t, c]の順で配列に格納してソートするといいかも

# C - Pyramid
0 <= x, y <= 100であることから頂点(Cx, Cy)を全探索可能だということを
読み取らなければならない。（出来なかった人は反省しないとだめらしい）  
\[h, x, y]の順で配列に格納し、ソートすることで、
max(h)を用いて頂点の高さを計算する。  
(Chはmax(h) ~ max(h) + 200だけど全探索する必要はない)  
`Ch = h + abs(x - Cx) + abs(y - Cy)`を求め、N個の入力と矛盾しないかどうか判定する。
 
敗因：  
- 与えられた情報から頂点を計算することにこだわりすぎた  
- 制約を見ていなかった
# D - Partition
最大公約数をDとしたときa1 ~ aNはDで割り切れる。そしてDはMの約数である。  
a1, a2, ..., aN >= Dなので、M >= N * D  
つまり、答えはMの約数かつM//N 以下の整数の中で最大のものとなる。  

for(i = M // N; i >0; i--)をするとTLE  
そこで、M = A * B（AはMの約数）を考えた時、
必ず片方はsqrt(M)以下になる性質を用いて
（M = sqrt(M) * sqrt(M)、どちらかが大きくなったらもう片方は必ずaqrt(M)未満になる）  
したがって、O(sqrt(M))で済む。


# わかったこと

- 制約  
    - 熟練者は制約を見て全探索が見えてくるらしい  
    - 難しそうな問題をいかに簡単に考えるか（制約はちゃんと読もう）
- itemgetter  
    - X = [[a1, b1], [a2, b2], ..., [ak, bk]]に対してbiを基準にソートしたい  
    - [bi, ai]順で格納する？ -> めんどい  
    - そこで`from operator import itemgetter`  
    - `Y = sorted(X, key = itemgetter(1))`でXの2番目の要素に対してソートされる
    - `Y = sorted(X, key = lambda x:x[1])`とも書ける  
    - lambdaは見づらいし実行時間も2倍らしいのでitemgetterを使おう
- C問題 with itemgetter  
    ```Python  
    from operator import itemgetter  
    # D = [[x1, y1, h1], ...]  
    max_height_pos = sorted(D, key = itemgetter(2))[-1]  
    Ch = max_height_pos[2] + abs(x - max_height_pos[0]) + abs(y - max_height_pos[1])
    ```