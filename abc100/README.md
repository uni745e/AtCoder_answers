# ABC100
https://beta.atcoder.jp/contests/abc100/tasks

## A
A, Bが両方共8以下ならYay!

## B
`print(100 ** D * N)`するだけ。  
N = 100の場合のみD + 1回で割り切れてしまうのを回避するために`print(100 ** D * (N + 1))`にする（1敗）  

## C
Ai (i = 1 ~ N)の各要素が2で何回割ることができるか数えて出力するだけ

## D
評価値が正の場合は`score = x + y + z`を大きい順にM個選べばよいが、今回はx, y, zそれぞれの絶対値を最大化させる問題なので、x, y, zそれぞれについて、正方向で最大値を目指すか、負の方向で最大値を目指すかの2^3通りを全探索することで最大の評価値を求める。  N <= 1000 * 2**3通りなのでPythonでも十分間に合う。
例：xとzは正方向、yは負方向に最大値を目指す場合、評価値は`x - y + z`と書くことができる。  

## まとめ  
abc101 ~ 107に比べると問題が簡単だった気がする  
D問題は問題を読むと全探索でも間に合うことがわかるので**問題はちゃんと読もう**  
評価値に絶対値が入ってくる場合は符号を[-1, 1]と切り替えて評価値を計算すればよいということを学んだ  

```
import itertools  
signs = (-1, 1)  
for a, b, c in itertools.product(* ([signs] * 3)):  
	score = a * x + b * y + c * z  
```

itertools.product便利だ......   
評価値もいちいち別に計算してappendしなくても下のように書ける  

```
for _ in range(N):
	cakes.append(inpl())
score = [a * x + b * y + c * z for x, y, z in cakes]
```