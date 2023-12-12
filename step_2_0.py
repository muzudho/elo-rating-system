#
# python step_2_0.py
#
import math

from step_1_1_0 import on_gyanken_1, games, main

# R0 = 2000
ratings = [0, 2000, 2000]

# Constant K
K = 32


# １勝するために必要な対局数（暗記表の x ）を取得
def get_games_by_rating_difference(
        rating_difference): # 暗記表の y
    
    # ゼロなら
    if rating_difference==0:
        return 1
    
    # 負数なら
    elif rating_difference <0:
        # 負数を指定できないので、符号をひっくり返して、あとで戻す
        return -400 * math.log10(-rating_difference)

    # 正の数なら
    else:
        return 400 * math.log10(rating_difference)


# レーティング差（暗記表の y ）を取得
def get_rating_difference_by_games(
        games): # 暗記表の x : 実数
    return math.floor(10 ** (games / 400))


# Win rate : 実数
def get_win_rate_for_upper_rating(win_games):
    return win_games / (win_games + 1)


# Win rate : 実数
def get_win_rate_for_lower_rating(win_games):
    return 1 / (win_games + 1)


if __name__ == "__main__":

    def on_result_1(result):


        # a から見た b とのレーティング差
        difference_a_to_b = ratings[2] - ratings[1]
        print(f"a から見た b とのレーティング差: {difference_a_to_b}")

        # b から見た a とのレーティング差
        difference_b_to_a = ratings[1] - ratings[2]
        print(f"b から見た a とのレーティング差: {difference_b_to_a}")

        # a から見た b に１勝するために必要な対局数
        games_a_to_b = get_games_by_rating_difference(difference_a_to_b)
        print(f"a から見た b に１勝するために必要な対局数: {games_a_to_b}")

        # b から見た a に１勝するために必要な対局数
        games_b_to_a = get_games_by_rating_difference(difference_b_to_a)
        print(f"b から見た a に１勝するために必要な対局数: {games_b_to_a}")

        # a から見た b への勝率
        if 0 <= difference_a_to_b:
            Wab = get_win_rate_for_upper_rating(games_a_to_b)
        else:
            Wab = get_win_rate_for_lower_rating(games_a_to_b)

        # b から見た a への勝率
        if 0 <= difference_b_to_a:
            Wba = get_win_rate_for_upper_rating(games_b_to_a)
        else:
            Wba = get_win_rate_for_lower_rating(games_b_to_a)

        print(f"Wab: {Wab}, Wba: {Wba}")

        # レーティングは動きません
        if result == 0:
            print(f"aiko  >  ratings A {ratings[1]}, B {ratings[2]}")

        # A が勝った
        elif result == 1:
            offset = math.floor(K * Wba)
            ratings[1] += offset
            ratings[2] -= offset
            print(f"A win  >  offset {offset},  ratings A {ratings[1]}, B {ratings[2]}")

        # B が勝った
        elif result == 2:
            offset = math.floor(K * Wab)
            ratings[2] += offset
            ratings[1] -= offset
            print(f"B win  >  offset {offset}, ratings A {ratings[1]}, B {ratings[2]}")

        else:
            print("Error")


    def on_end_1():
        print(f"games:   aiko: {games[0]}, A win: {games[1]}, B win: {games[2]}")
        print(f"ratings: aiko: {ratings[0]}, A win: {ratings[1]}, B win: {ratings[2]}")


    main(on_gyanken=on_gyanken_1,
         on_result=on_result_1,
         on_end=on_end_1)
