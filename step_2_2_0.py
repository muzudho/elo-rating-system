#
# python step_2_2_0.py
#
# プレイヤーのデータベースを連想配列で作る
#

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
