# ABC105  
https://beta.atcoder.jp/contests/abc105/tasks  

## A  
答えが2以上になることはありえない  
`N % K == 0`を満たすなら0、満たさないなら1を出力。

## B  
ケーキの個数をi、ドーナツの個数をjとして2重のfor文を回すこともできるが、  
ケーキの購入数をfor文で回していき、ケーキをi個買った時の差額が7ドルで割り切れるかを判定すれば1重のfor文で解ける。

## C
入力Nが奇数であれば、ビットに1を立ててNの値を1減らす。  
入力Nが偶数であれば、ビットに0を立ててNの値はそのまま。  
そして、`N//(-2)`して同じ処理をN=0になるまで繰り返す。

*Nは処理のたびに正負が反転するのでループを書く時は`while n != 0:`みたいに書く  

## D
普通に累積和求めて全探索しようとしたがTLE  
問題の条件だと計算数は最大4999950000になるのでPythonだと無理だ  
**要勉強**