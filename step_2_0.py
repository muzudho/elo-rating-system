#
# python step_1_1_0.py
#
import math

from step_1_1_0 import on_gyanken_1, games, main

# R0 = 2000
ratings = [0, 2000, 2000]

# Constant K
K = 32


# Rating calculate
def get_x_by_y(y):
    if y==0:
        return 1
    else:
        return 400 * math.log10(y)


# Rating calculate
def get_y_by_x(x):
    return x ** (x / 400)


# Win rate
def get_win_rate_for_upper_rating(win_games):
    return win_games / (win_games + 1)


# Win rate
def get_win_rate_for_lower_rating(win_games):
    return 1 / (win_games + 1)


if __name__ == "__main__":

    def on_result_1(result):


        # レーティング差
        ab = ratings[1] - ratings[2]
        ba = ratings[2] - ratings[1]
        y = abs(ba)
        print(f"y: {y}")
        x = get_x_by_y(y)


        # 勝率
        win_rate_for_lower_rating = 1 / (x+1)
        #win_rate_for_upper_rating = x / (x+1)


        if result == 0:
            # レーティングは動きません
            print(f"aiko  >  ratings A {ratings[1]}, B {ratings[2]}")

        elif result == 1:
            offset = K * win_rate_for_lower_rating
            ratings[1] += offset
            ratings[2] -= offset
            print(f"A win  >  ratings A {ratings[1]}, B {ratings[2]}")

        elif result == 2:
            offset = K * win_rate_for_lower_rating
            ratings[2] += offset
            ratings[1] -= offset
            print(f"B win  >  ratings A {ratings[1]}, B {ratings[2]}")

        else:
            print("Error")


    def on_end_1():
        print(f"games:   aiko: {games[0]}, A win: {games[1]}, B win: {games[2]}")
        print(f"ratings: aiko: {ratings[0]}, A win: {ratings[1]}, B win: {ratings[2]}")


    main(on_gyanken=on_gyanken_1,
         on_result=on_result_1,
         on_end=on_end_1)
