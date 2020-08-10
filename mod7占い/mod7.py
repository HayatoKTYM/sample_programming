# coding: utf-8

"""
-URL
https://paiza.jp/works/mondai/skillcheck_sample/mod7?language_uid=python3&t=ce7f5cfec317810e36c5f2af560e49b5

-入力
カード枚数
カードのの数字
3
10
4
14

-出力
7で割り切れる組み合わせ
1

- 方針
7 で割った余を格納
３枚のカードを選んで7 で割りきれるためには
- 3枚とも同じ余りカードを使用
- 2枚は同じ余りで1枚は違う余りカードを使用
- ３枚とも違う余りカードを使用
の３パターンしかない
"""
# 0 , 1-6 2-5 3-4 
import math
def combinations_count(n, r):
    # 組み合わせを返す
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

def main():
    # 余をkeyとして個数を格納しておく
    numbers = {i:0 for i in range(7)}
    for i in range(int(input())):
        numbers[int(input())%7] += 1
    print(cnt_mod7(numbers))

def cnt_mod7(numbers):
    ans = 0
    for i in range(7):
        for j in range(i, 7):
            # 2枚が決まれば残りの１種類は一意に決定
            k = (7 - i - j) % 7
            # 重複を防ぐために i <= j <= k を仮定
            # 3種類のカード
            if len(set([i, j, k])) == 3 and i < j < k:
                ans += (numbers[i]*numbers[j]*numbers[k])
            # 2種類のカード
            elif len(set([i, j, k])) == 2:
                if i < j == k:
                    ans += (numbers[i]*numbers[j]*(numbers[j]-1)//2)
                if i == j < k:
                    ans += (numbers[k]*numbers[i]*(numbers[i]-1)//2)
            # １種類のカード (0 のカード)
            elif i == j == k:
                if numbers[0] >= 3:
                    ans += combinations_count(numbers[0], 3)
        
    return ans
        
if __name__ == '__main__':
    main()