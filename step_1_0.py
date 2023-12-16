#
# python step_1_0.py
#
import random


def main(
        on_tournament_executing,
        on_tournament_is_over,
        on_gyanken,
        on_game_over):
    """プログラムのフレームワーク
    
    集計は、このプログラムのフレームワークの外に出す

    Parameters
    ----------
    on_tournament_executing : func
        大会のフレームワーク
    on_tournament_is_over: func
        大会終了時
    on_gyanken:
        対局実行
    on_game_over: func
        対局終了時
    """

    # ラウンド数を入力
    print("Please input round number(1-100):")
    round = int(input())

    # 大会の実行
    on_tournament_executing(
        round=round,
        on_tournament_is_over=on_tournament_is_over,
        on_gyanken=on_gyanken,
        on_game_over=on_game_over)


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
        # プレイヤーのデータベース（まだない）
        player_database = {}

        # 対局実行
        result = on_gyanken("player_1", "player_2", player_database)

        # 結果
        on_game_over(result)

    # 大会終了時
    on_tournament_is_over()


def gyanken(player_1_id, player_2_id, player_database):
    """ジャンケンをする。

    Returns
    -------
    0: あいこ
    1: プレイヤー１の勝ち
    2: プレイヤー２の勝ち のいずれかを返す"""
    return random.randint(0, 2)


def on_my_game_over(result):
    """対局終了時

    Parameters
    ----------
    result : int
        0: あいこ
        1: プレイヤー１の勝ち
        2: プレイヤー２の勝ち
    """

    if result == 0:
        print("aiko")
    elif result == 1:
        print("A win")
    elif result == 2:
        print("B win")
    else:
        print("Error")

    # 集計
    total_games[result] += 1


if __name__ == "__main__":

    # 集計（Totalization）
    # [0] あいこの数, [1] Aの勝利数, [2] Bの勝利数
    total_games = [0,0,0]


    def on_my_tournament_is_over():
        """大会終了時"""

        # 集計の表示
        print(f"aiko: {total_games[0]}, A win: {total_games[1]}, B win: {total_games[2]}")


    # プログラムの実行
    main(
        on_tournament_executing = on_my_tournament_executing,
        on_tournament_is_over = on_my_tournament_is_over,
        on_gyanken = gyanken,
        on_game_over = on_my_game_over)
