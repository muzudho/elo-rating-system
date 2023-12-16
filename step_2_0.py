#
# python step_2_0.py
#
import math
import random

from step_1_0 import main, execute_tournament, gyanken


def calculate_moving_rating_that_a_wins(K, ratings):
    """A が勝った時のレーティングの移動量"""

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


def calculate_moving_rating_that_b_wins(K, ratings):
    """B が勝った時のレーティングの移動量"""

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


def get_games_by_rating_difference(
        rating_difference):
    """１勝するために必要な対局数（暗記表の x ）を取得
    実数でも算出できるが、（1.0 以上の数になるよう数式を調整している前提で）整数にして返す

    Parameters
    ----------
    rating_difference : int
        暗記表の y
    """
    return math.floor(10 ** (rating_difference / 400))


def get_rating_difference_by_games(
        games_number):
    """レーティング差（暗記表の y ）を取得

    Parameters
    ----------
    games_number : float
        暗記表の x : 実数
    """
    return math.floor(400 * math.log10(games_number))


def get_win_rate_for_upper_rating(win_games):
    """Win rate : 実数"""
    return win_games / (win_games + 1)


def get_win_rate_for_lower_rating(win_games):
    """Win rate : 実数"""
    return 1 / (win_games + 1)


def print_drawn(ratings):
    """あいこの表示"""
    print(f"""\
+------+
| aiko |
+------+
* ratings: A {ratings[1]}, B {ratings[2]}""")


def print_a_win(ratings, K, answers):
    """A が勝ったときの表示"""
    print(f"""\
+-------+
| A win |
+-------+
* b から見た a とのレーティング差: {answers["difference_b_to_a"]}
* b から見た a に１勝するために必要な対局数: {answers["games_b_to_a"]}
* b から見た a への勝率(Wba): {answers["Wba"]}
* K: {K},  moving_rating: {answers['moving_rating']},  ratings: A {ratings[1]}, B {ratings[2]}\
""")


def print_b_win(ratings, K, answers):
    """B が勝ったときの表示"""
    print(f"""\
+-------+
| B win |
+-------+
* a から見た b とのレーティング差: {answers["difference_a_to_b"]}
* a から見た b に１勝するために必要な対局数: {answers["games_a_to_b"]}
* a から見た b への勝率(Wab): {answers["Wab"]}
* K: {K},  moving_rating: {answers['moving_rating']},  ratings: A {ratings[1]}, B {ratings[2]}\
""")


def print_tournament_result(total_games, ratings):
    """大会終了時の表示"""
    print(f"""\
+-------------------+
| tournament result |
+-------------------+
* games:    aiko: {total_games[0]:4},  A win: {total_games[1]:4},  B win: {total_games[2]:4}
* ratings:  aiko: {ratings[0]:4},  A win: {ratings[1]:4},  B win: {ratings[2]:4}\
""")


def save_game_summary(path, total_games, ratings):
    """大会記録の集計をファイルへ保存"""
    with open(path, mode='w') as f:

        # 集計
        f.write(f"""\
player,  win, rating
------, ----, ------
  aiko, {total_games[0]:4}, {ratings[0]:6}
     A, {total_games[1]:4}, {ratings[1]:6}
     B, {total_games[2]:4}, {ratings[2]:6}
""")


if __name__ == "__main__":

    # プレイヤーのデータベース
    # 操作のしやすさから、辞書ではなくリストを使う
    player_database = [
        {
            # Id
            "id" : "player_1",
            # 表示名
            "display_name" : "Alice",
            # レーティング
            "rating" : 2000,
        },
        {
            # Id
            "id" : "player_2",
            "display_name" : "Bob",
            "rating" : 2000,
        },
    ]

    # データベースから２人のプレイヤーを選び、その２人分の集計とする
    #
    # 集計（Totalization）
    # [0] あいこの数, [1] Aの勝利数, [2] Bの勝利数
    total_games = [0,0,0]

    # データベースから２人のプレイヤーを選び、そのレーティングをセットしたい。今回は行わない
    #
    # この対局でのレーティングについて
    # [0] : 未使用
    # [1] : プレイヤー１のレーティング
    # [2] : プレイヤー２のレーティング
    # 初期値：　R0 = 2000
    ratings = [0, 2000, 2000]

    # Constant K
    K = 32


    def on_my_tournament_is_start():
        """大会開始時"""
        # 開始
        # プレイヤーのデータベースから、プレイヤーを選ぶ
        two_player_records = random.sample(player_database, 2)
        # ２プレイヤーのレーティングを表示したい

        print(f"""\
+-------+
| start |
+-------+
* ratings: {two_player_records[0]['display_name']} {two_player_records[0]['rating']}, {two_player_records[1]['display_name']} {two_player_records[1]['rating']}\
""")


    def on_my_tournament_is_over():
        """大会終了時"""

        # データベースへの反映は、今回は行いません

        # 大会結果の表示
        print_tournament_result(total_games, ratings)

        # 対局記録の集計をファイルへ保存
        save_game_summary(
            path='data_output/step_2_0.csv',
            total_games=total_games,
            ratings=ratings)


    def on_my_game_start():
        """対局開始時"""


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
            print_drawn(ratings)

        # A が勝った
        elif result == 1:

            # A が勝った時のレーティングの移動量
            answers = calculate_moving_rating_that_a_wins(K, ratings)

            # ２者のレーティングが動きます
            ratings[1] += answers["moving_rating"]
            ratings[2] -= answers["moving_rating"]

            print_a_win(ratings, K, answers)

        # B が勝った
        elif result == 2:

            # B が勝った時のレーティングの移動量
            answers = calculate_moving_rating_that_b_wins(K, ratings)

            # ２者のレーティングが動きます
            ratings[2] += answers["moving_rating"]
            ratings[1] -= answers["moving_rating"]

            print_b_win(ratings, K, answers)

        else:
            print("Error")

        total_games[result] += 1


    # プログラムの実行
    main(
        player_database=player_database,
        on_tournament_is_start=on_my_tournament_is_start,
        on_tournament_executing=execute_tournament,
        on_tournament_is_over=on_my_tournament_is_over,
        on_game_start = on_my_game_start,
        on_gyanken=gyanken,
        on_game_over=on_my_game_over)
