# ABC073
https://beta.atcoder.jp/contests/abc073/tasks  

# A - September 9
`N // 10 == 9 or N % 10 == 9`を満たすならYes


# B - Theater
seat[100000] = Falseを用意  
seat[l - 1: r] = Trueに置き換えるをN回行う  
Trueの数が答え

# C - Write and Erase
辞書型を使って出てきた数字と回数を数える  
`dict[number] % 2 == 1`を満たす物の個数が答えとなる

# D - joisino's travel
すべての町を通過したい。この時、スタート地点に町の無い頂点を選ぶことはない。  
町のある頂点をスタート地点としてR回ダイクストラ方を適用する。  
これで、それぞれの町riからスタートしたときの最短経路が求まる。

次にどの順に町を通過するかを考える。  
町がRヶ所存在する場合、R!通りの方法がある。  
R!通りを全探索して一番コストの低かったものが答えとなる。

順列の生成にはitertoolsのpermutationsを使用した  
```Python  
# R : int 町の個数  
# r : list 町のある頂点
for root in itertools.permutations(r, R):  
    print(root)
```

# わかったこと
- 数学問題よりグラフ問題のほうが方針を立てやすい？
    - 現状BFS, DFS, ダイクストラしか使えないので勉強が必要  
    - コストが負のグラフが出てきたときのために**ベルマンフォード**を学ぶべき？  
- パターン列挙にはitertoolsが便利  
    - 組み合わせ：itertools.combinations(iterable, r)  
    combinations(ABCD, 2) -> AB AC AD BC BD CD  
    combinations(range(4), 3) -> 012 013 023 123  
    - 順列：itertools.permutations(iterable, r)  
    permutations(\[1, 2, 3], 3) -> 123, 132, 213, 231, 312, 321  
    - デカルト積：itertools.product(iterable, repeat = 1)  
    product([-1, 1], repeat=3) -> (-1, -1, -1), (-1, -1, -1), 
    (-1, -1, 1),   
    (-1, 1, -1), (-1, 1, 1), (1, -1, -1), (1, -1, 1), (1, 1, -1), (1, 1, 1)