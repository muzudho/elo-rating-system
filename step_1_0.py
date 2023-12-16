#
# python step_1_0.py
#
import random


# 0: あいこ, 1: プレイヤー１の勝ち, 2: プレイヤー２の勝ち のいずれかを返す
def gyanken():
    return random.randint(0, 2)


def main(
        on_tournament_executed):
    """プログラムの全体"""

    print("Please input round number(1-100):")
    round = int(input())

    # 大会の実行
    on_tournament_executed(round)


if __name__ == "__main__":

    def on_my_tournament_executed(round):
        """大会を実行する

        Parameters
        ----------
        round : int
            対局数
        """

        counts = [0,0,0]

        for i in range(0, round):
            result = gyanken()

            counts[result] += 1

            if result == 0:
                print("aiko")
            elif result == 1:
                print("A win")
            elif result == 2:
                print("B win")
            else:
                print("Error")

        print(f"aiko: {counts[0]}, A win: {counts[1]}, B win: {counts[2]}")


    # プログラムの実行
    main(
        on_tournament_executed = on_my_tournament_executed)
