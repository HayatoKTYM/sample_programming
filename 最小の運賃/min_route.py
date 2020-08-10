"""
-URL
https://paiza.jp/works/mondai/real_event/min_fare?language_uid=python3

-入力
エッジ数, 地点数, ゴール地点
5 5 3
0 1 200
0 4 500
0 2 200
1 4 200
4 3 300

-出力
ゴールまでの最短コスト
700

-方針
ダイクストラ法？
0 から startして，最小コストの地点を順次登録していく
最初各地点へのコストは無限大で初期化する
(適当にでかい数字で初期化したら大規模入力で超えられた)
"""
import numpy as np
E, V, T = map(int, input().split())
Graph = np.zeros((V,V))
# コストの初期化 : 十分大きい値で初期化
Cost = np.zeros(V) + np.inf
# グラフの作成
for i in range(E):
    start, end, cost = map(int, input().split())
    Graph[start,end] = cost
    Graph[end,start] = cost

# 確定した地点を格納
Register = {}
# 候補地を格納
Queue = [0]
Queue_c = [0]

while True:
    state = Queue.pop(0)
    cost = Queue_c.pop(0)
    # 確定地点を追加
    Register[state] = 1
    if len(Register) == V:
        break
    # 確定地点につながっている地点のコストを更新
    for i in range(V):
        if Graph[state,i] > 0 and i not in Register:
            Cost[i] = min(Cost[i], cost+Graph[state,i])

    # 登録されていない && 最も小さい値をQueue に追加する
    index = [i for i in range(V) if i not in Register]
    min_cost_state = index[Cost[index].argmin()]
    
    Queue.append(min_cost_state)
    Queue_c.append(Cost[index].min())


print(int(Cost[T]))