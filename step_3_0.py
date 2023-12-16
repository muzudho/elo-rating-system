#
# python step_3_0.py
#
# プレイヤーのデータベースを連想配列で作る
#
from step_1_0 import main, on_my_tournament_executing, gyanken
from step_2_1_0 import on_my_game_over, on_my_tournament_is_over


# プレイヤーのデータベース
player_database = {
    # Id
    "player_1" : {
        # 表示名
        "display_name" : "Alice",
        # レーティング
        "rating" : 2000,
    },
    "player_2" : {
        "display_name" : "Bob",
        "rating" : 2000,
    },
    "charley" : {
        "display_name" : "Charley",
        "rating" : 2000,
    },
}


def on_my_tournament_executing(
        round,
        on_tournament_is_over,
        on_gyanken,
        on_game_over):
    """大会実行のフレームワーク

    集計は、大会の実行の外に出す

    Parameters
    ----------
    round : int
        対局数
    on_tournament_is_over : func
        大会終了時
    on_game_over : func
        対局終了時
    on_gyanken : func
        対局実行
    """

    for i in range(0, round):
        # 対局実行
        result = on_gyanken("player_1", "player_2", player_database)

        # 結果
        on_game_over(result)

    # 大会終了時
    on_tournament_is_over()


if __name__ == "__main__":

    # 集計（Totalization）
    # [0] あいこの数, [1] Aの勝利数, [2] Bの勝利数
    total_games = [0,0,0]

    # この対局でのレーティングについて
    # [0] : 未使用
    # [1] : プレイヤー１のレーティング
    # [2] : プレイヤー２のレーティング
    # 初期値：　R0 = 2000
    ratings = [0, 2000, 2000]

    # Constant K
    K = 32


    # 開始
    print(f"""\
+-------+
| start |
+-------+\
* ratings: A {ratings[1]}, B {ratings[2]}""")

    # プログラムの実行
    main(
        on_tournament_executing=on_my_tournament_executing,
        on_gyanken=gyanken,
        on_game_over=on_my_game_over,
        on_tournament_is_over=on_my_tournament_is_over)
