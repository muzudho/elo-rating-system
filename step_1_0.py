#
# python step_1_0.py
#
import random


def gyanken():
    """ジャンケンをする。

    Returns
    -------
    0: あいこ
    1: プレイヤー１の勝ち
    2: プレイヤー２の勝ち のいずれかを返す"""
    return random.randint(0, 2)


def main(
        on_tournament_executed,
        on_tournament_is_over,
        on_game_over,
        on_gyanken):
    """プログラムのフレームワーク"""

    # ラウンド数を入力
    print("Please input round number(1-100):")
    round = int(input())

    # TODO 大会と集計は分けたい
    # 大会の実行
    on_tournament_executed(
        round,
        on_tournament_is_over,
        on_game_over,
        on_gyanken)


if __name__ == "__main__":

    # 集計
    counts = [0,0,0]


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

        counts[result] += 1


    def on_my_tournament_is_over():
        """大会終了時"""
        print(f"aiko: {counts[0]}, A win: {counts[1]}, B win: {counts[2]}")


    def on_my_tournament_executed(
            round,
            on_tournament_is_over,
            on_game_over,
            on_gyanken):
        """大会を実行する

        Parameters
        ----------
        round : int
            対局数
        """

        for i in range(0, round):
            result = on_gyanken()

            # 集計は、大会の実行の外に出す
            on_game_over(result)


        # 大会終了時
        on_tournament_is_over()


    # プログラムの実行
    main(
        on_tournament_executed = on_my_tournament_executed,
        on_tournament_is_over = on_my_tournament_is_over,
        on_game_over = on_my_game_over,
        on_gyanken = gyanken)
