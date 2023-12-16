#
# python step_1_1_0.py
#
from step_1_0 import gyanken


def main(
        on_tournament_executing,
        on_gyanken,
        on_game_over,
        on_tournament_is_over):
    """プログラムのフレームワーク
    
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

    print("Please input round number(1-100):")
    round = int(input())

    # 大会の実行
    on_tournament_executing(
        round=round,
        on_gyanken=on_gyanken,
        on_game_over=on_game_over,
        on_tournament_is_over=on_tournament_is_over)


def on_my_tournament_executing(
        round,
        on_gyanken,
        on_game_over,
        on_tournament_is_over):
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
        result_1 = on_gyanken()

        # 結果
        on_game_over(result_1)

    # 大会終了時
    on_tournament_is_over()


if __name__ == "__main__":

    # 集計。あいこの数, Aの勝利数, Bの勝利数
    total_games = [0,0,0]

    def on_my_game_over(result):
        if result == 0:
            print("aiko")
        elif result == 1:
            print("A win")
        elif result == 2:
            print("B win")
        else:
            print("Error")

        total_games[result] += 1


    def on_my_tournament_is_over():
        """対局終了時

        Parameters
        ----------
        result : int
            0: あいこ
            1: プレイヤー１の勝ち
            2: プレイヤー２の勝ち
        """
        print(f"aiko: {total_games[0]}, A win: {total_games[1]}, B win: {total_games[2]}")


    # プログラムの実行
    main(
        on_tournament_executing = on_my_tournament_executing,
        on_gyanken=gyanken,
        on_game_over=on_my_game_over,
        on_tournament_is_over=on_my_tournament_is_over)
