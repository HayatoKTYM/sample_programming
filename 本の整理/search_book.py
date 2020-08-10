# coding: utf-8
"""
-URL
https://paiza.jp/works/mondai/real_event/book_sort?language_uid=python3

-入力
本の数, その並び
10
8 7 9 1 5 6 2 10 4 3

-出力
入れ替える回数
6
-方針
index i において 
 (1) 本番号が "i" なら OK
 (2-1) 違うなら "i" のある位置と入れ替える
 (2-2) "i" のあった位置の本を index i の本に置き換え 
"""
N = int(input())
# index に対応する本の情報
num_list = list(map(int,input().split()))

# 本番号: その本の位置 の辞書
key2num = {a:b for a,b in zip(num_list,list(range(1,N+1)))}
cnt = 0
for i in range(1,N+1):
    if key2num[i] == i:
        continue
    cnt += 1
    # i 番目の本を key2num[i] の位置に移動
    key2num[num_list[i-1]] = key2num[i]
    # key2num[i] の本情報を更新
    num_list[key2num[i]-1] = num_list[i-1]
print(cnt)