# ABC098  
https://beta.atcoder.jp/contests/abc098/tasks

## A
`max(a + b, a - b, a * b)するだけ`

## B
文字列SをLとRに分割する。  
Lに含まれる文字がRにも含まれるかどうか探索する。  
種類数を数える問題なので、一度探索したものは配列に保存しておく。  
文字列の長さは100以下なので全探索でも間に合う。

## C
自分より東側にいるEの人数と西側にいるWの人数の和が最小になる人をリーダにする問題  
まず最初にEとWの人数を数える。  
左から順に探索していき、リーダの向いている方向の人数を一人減らしていく  
（リーダが東を向いているならE--、西を向いているならW--）  
そうすることで、リーダより東側にEが、西側にWが何人存在するかわかる。  
*リーダ自身がWのときは、Wが東でも西でもない場所にいることになるためさらに-1

## D
500点問題  

しゃくとり法を用いた全ての要素の総和とxor和が等しい区間の数え上げ問題  

**要素の総和とxor和が等しくなる場合、要素の総和をとった時、bitの繰り上がりが発生しない**  
例：  
5 + 2  
101 + 010 = 111 = 7  
101 xor 010 = 111 = 7

5 + 3  
101 + 011 = 1000 = 8  
101 xor 011 = 110 = 6  

1 + 2 + 8  
0001 + 0010 +1000 = 1011 = 11  
xor -> 1011 = 11  

bitの繰り上がりが発生した時点で、それ以上の要素を足し合わせても総和とxor和は一致しない。  

区間の左端をleft、右端をright、区間内の総和をresとした時、  
`right < N and res + A[right] == res xor A[right]`という条件でしゃくとり法を実装すれば、条件を満たす区間をO(N)で数え上げることができる。


## わかったこと  
しゃくとり法  

* 累積和とごっちゃになってたけどなんとなく理解した
* 単調増加、単調減少の時に使える
* 総和、積、xor和いろいろパターンはあるけど条件とleftのインクリメント時の処理が変わるだけ[*1](https://twitter.com/uni745e/status/1037738443642523648)
* **問題を読んで求めるものが数え上げか最長かちゃんと確認しましょう**


