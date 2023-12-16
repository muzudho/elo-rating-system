#
# python step_1_1_0.py
#
from step_1_0 import gyanken


# 集計。あいこの数, Aの勝利数, Bの勝利数
total_games = [0,0,0]


def main(
        on_gyanken,
        on_game_over,
        on_tournament_is_over):

    print("Please input round number(1-100):")
    round = int(input())


    for i in range(0, round):
        result_1 = on_gyanken()

        total_games[result_1] += 1

        on_game_over(result_1)

    on_tournament_is_over()


if __name__ == "__main__":

    def on_my_game_over(result):
        if result == 0:
            print("aiko")
        elif result == 1:
            print("A win")
        elif result == 2:
            print("B win")
        else:
            print("Error")


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
        on_gyanken=gyanken,
        on_game_over=on_my_game_over,
        on_tournament_is_over=on_my_tournament_is_over)
