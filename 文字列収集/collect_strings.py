# coding: utf-8
"""
-URL
https://paiza.jp/works/mondai/real_event/word_collection?language_uid=python3&

- 方針
1~100文字までのkeyを全て持っておく
ans で参照するときは 1発で当てられるようにする
(keyになければ 0 を返す)
"""
N, M = map(int, input().split())

key2price = {}
for i in range(N):
    key, price = input().split()
    for j in range(1,len(key)+1):
        if key[:j] in key2price:
            key2price[key[:j]] += int(price)
        else:
            key2price[key[:j]] = int(price)

for i in range(M):
    ans_key = input()
    print(key2price[ans_key] if ans_key in key2price else 0)
