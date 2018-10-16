# ABC105  
https://beta.atcoder.jp/contests/abc105/tasks  

## A - AtCoder Crackers  
答えが2以上になることはありえない  
`N % K == 0`を満たすなら0、満たさないなら1を出力。

## B - Cakes and Donuts  
ケーキの個数をi、ドーナツの個数をjとして2重のfor文を回すこともできるが、  
ケーキの購入数をfor文で回していき、ケーキをi個買った時の差額が7ドルで割り切れるかを判定すれば1重のfor文で解ける。

## C - Base -2 Number
入力Nが奇数であれば、ビットに1を立ててNの値を1減らす。  
入力Nが偶数であれば、ビットに0を立ててNの値はそのまま。  
そして、`N//(-2)`して同じ処理をN=0になるまで繰り返す。

*Nは処理のたびに正負が反転するのでループを書く時は`while n != 0:`みたいに書く  

## D - Candy Distribution
累積和Sを求める。  
`a1 + a2 + .. + an = X`は累積和では`Sn - S0`と表せる  
XがMで割り切れる時、`Sn ≡ S0 (mod M)`という特性がある  

累積和の各要素をMで割ったあまりを0~M-1まで数え上げる  
そして、0~M-1までのそれぞれの数に対して2個選ぶ組み合わせを足し合わせる  
```Python  
for num in dict_mod:  
    n = dict_mod[num]  
    # cmb(n, 2)
    ans += n * (n - 1) // 2
```

最後に箱単体で条件を満たす場合を足し合わせる`ans += dict_mod[0]`

d_2.pyはCounterを使った解法  
こっちのほうが速いし簡潔に書ける

## わかったこと
- 倍数と累積和
    - A1 + A2 + .. + AN = XがMの倍数の時
    - Xは累積和では`X = SN - S0`と表現できる。  
    - `SN ≡ S0 (mod M)`という性質がある
- collections.Counter
    - 辞書型のサブクラス
    - 配列の要素の数え上げが出来る
    - for v in Counter(list).value():
    - value無しならkeyのリストが選ばれる