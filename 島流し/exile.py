# coding: utf-8
""" 
-URL
https://paiza.jp/works/mondai/skillcheck_sample/search-island?language_uid=python3&t=17366051bd5d60f78f52f0a134e1c737

-入力例
横 縦　の数
島があるところは1 それ以外は0

4 5
0 1 1 0
1 0 1 0
1 0 0 0
0 0 1 1
0 1 1 1

-出力
3

-方針
for で全探索
1 を見つけたら 行けるところまで深堀 >> それが一つの島となる
探索したところは Register に追加していく
0 のところは情報がないので何もしない

"""
def exile(map_lst):
    M = len(map_lst[0])
    N = len(map_lst)
    # 島の数
    ans = 0
    # 探索した座標を格納
    Register = {}
    for i in range(N):
        for j in range(M):
            # すでに探索済み
            if (i,j) in Register:
                continue

            # 情報なし
            if map_lst[i][j] == 0:
                Register[(i,j)]=0
                continue
            # 幅優先探索で実装
            # 1 ならば 行けるところまで突き進む
            ans += 1
            queue = [(i,j)]
            while True:
                if len(queue) == 0:
                    break
                x, y = queue.pop(0)
                # 上下左右方向を探索
                if x > 0:
                    if map_lst[x-1][y]:
                        if (x-1, y) not in Register:
                            queue.append((x-1,y))
                    Register[(x-1,y)]=0
                if x < N-1:
                    if map_lst[x+1][y]:
                        if (x+1, y) not in Register:
                            queue.append((x+1,y))  
                    Register[(x+1,y)]=0
                if y > 0:
                    if map_lst[x][y-1]:
                        if (x, y-1) not in Register:
                            queue.append((x,y-1))  
                    Register[(x,y-1)]=0
                if y < M-1:
                    if map_lst[x][y+1]:
                        if (x, y+1) not in Register:
                            queue.append((x,y+1))  
                    Register[(x,y+1)]=0
    return ans

def main():
    M, N = map(int, input().split())
    map_lst = [list(map(int, input().split())) for i in range(N)]
    print(exile(map_lst))

if __name__ == '__main__':
    main()


