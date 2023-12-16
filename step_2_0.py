#
# python step_2_0.py
#
import math

from step_1_0 import main, on_my_tournament_executing, gyanken


# A が勝った時のレーティングの移動量
def calculate_moving_rating_that_a_wins(K, ratings):

    result = {}

    # b から見た a とのレーティング差
    result["difference_b_to_a"] = ratings[1] - ratings[2]

    # b から見た a に１勝するために必要な対局数
    result["games_b_to_a"] = get_games_by_rating_difference(result["difference_b_to_a"])

    # b から見た a への勝率
    if 0 <= result["difference_b_to_a"]:
        result["Wba"] = get_win_rate_for_upper_rating(result["games_b_to_a"])
    else:
        result["Wba"] = get_win_rate_for_lower_rating(result["games_b_to_a"])

    # レーティングの移動量
    result["moving_rating"] = math.floor(K * result["Wba"])
    return result


# B が勝った時のレーティングの移動量
def calculate_moving_rating_that_b_wins(K, ratings):

    result = {}

    # a から見た b とのレーティング差
    result["difference_a_to_b"] = ratings[2] - ratings[1]

    # a から見た b に１勝するために必要な対局数
    result["games_a_to_b"] = get_games_by_rating_difference(result["difference_a_to_b"])

    # a から見た b への勝率
    if 0 <= result["difference_a_to_b"]:
        result["Wab"] = get_win_rate_for_upper_rating(result["games_a_to_b"])
    else:
        result["Wab"] = get_win_rate_for_lower_rating(result["games_a_to_b"])

    # レーティングの移動量
    result["moving_rating"] = math.floor(K * result["Wab"])
    return result


# １勝するために必要な対局数（暗記表の x ）を取得
# 実数でも算出できるが、（1.0 以上の数になるよう数式を調整している前提で）整数にして返す
def get_games_by_rating_difference(
        rating_difference): # 暗記表の y
    return math.floor(10 ** (rating_difference / 400))


# レーティング差（暗記表の y ）を取得
def get_rating_difference_by_games(
        games_number): # 暗記表の x : 実数
    #return math.floor(10 ** (games_number / 400))
    return math.floor(400 * math.log10(games_number))


# Win rate : 実数
def get_win_rate_for_upper_rating(win_games):
    return win_games / (win_games + 1)


# Win rate : 実数
def get_win_rate_for_lower_rating(win_games):
    return 1 / (win_games + 1)


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

    def on_my_game_over(result):
        """対局終了時

        Parameters
        ----------
        result : int
            0: あいこ
            1: プレイヤー１の勝ち
            2: プレイヤー２の勝ち
        """

        # あいこ
        if result == 0:
            # ２者のレーティングは動きません
            print(f"""\
+------+
| aiko |
+------+\
* ratings: A {ratings[1]}, B {ratings[2]}""")

        # A が勝った
        elif result == 1:

            # A が勝った時のレーティングの移動量
            answers = calculate_moving_rating_that_a_wins(K, ratings)

            # ２者のレーティングが動きます
            ratings[1] += answers["moving_rating"]
            ratings[2] -= answers["moving_rating"]

            print(f"""\
+-------+
| A win |
+-------+
* b から見た a とのレーティング差: {answers["difference_b_to_a"]}
* b から見た a に１勝するために必要な対局数: {answers["games_b_to_a"]}
* b から見た a への勝率(Wba): {answers["Wba"]}
* K: {K},  moving_rating: {answers['moving_rating']},  ratings: A {ratings[1]}, B {ratings[2]}\
""")

        # B が勝った
        elif result == 2:

            # B が勝った時のレーティングの移動量
            answers = calculate_moving_rating_that_b_wins(K, ratings)

            # ２者のレーティングが動きます
            ratings[2] += answers["moving_rating"]
            ratings[1] -= answers["moving_rating"]

            print(f"""\
+-------+
| B win |
+-------+
* a から見た b とのレーティング差: {answers["difference_a_to_b"]}
* a から見た b に１勝するために必要な対局数: {answers["games_a_to_b"]}
* a から見た b への勝率(Wab): {answers["Wab"]}
* K: {K},  moving_rating: {answers['moving_rating']},  ratings: A {ratings[1]}, B {ratings[2]}\
""")

        else:
            print("Error")

        total_games[result] += 1


    def on_my_tournament_is_over():
        """大会終了時"""

        print(f"""\
+--------+
| result |
+--------+
* games:    aiko: {total_games[0]:4},  A win: {total_games[1]:4},  B win: {total_games[2]:4}
* ratings:  aiko: {ratings[0]:4},  A win: {ratings[1]:4},  B win: {ratings[2]:4}\
              """)

        # ファイルへ保存
        with open('data_output/step_2_0.csv', mode='w') as f:

            # 集計
            f.write(f"""\
player,  win, rating
------, ----, ------
  aiko, {total_games[0]:4}, {ratings[0]:6}
     A, {total_games[1]:4}, {ratings[1]:6}
     B, {total_games[2]:4}, {ratings[2]:6}
""")


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
