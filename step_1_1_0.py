#
# python step_1_1_0.py
#
import random

# 集計。あいこの数, Aの勝利数, Bの勝利数
total_games = [0,0,0]


# 0, 1, 2 のいずれかを返す
def on_gyanken_1():
    return random.randint(0, 2)


def main(
        on_gyanken,
        on_tournament_is_over,
        on_end):

    print("Please input round number(1-100):")
    round = int(input())


    for i in range(0, round):
        result_1 = on_gyanken()

        total_games[result_1] += 1

        on_tournament_is_over(result_1)

    on_end()


if __name__ == "__main__":

    def on_my_tournament_is_over(result):
        if result == 0:
            print("aiko")
        elif result == 1:
            print("A win")
        elif result == 2:
            print("B win")
        else:
            print("Error")


    def on_my_end():
        print(f"aiko: {total_games[0]}, A win: {total_games[1]}, B win: {total_games[2]}")


    main(on_gyanken=on_gyanken_1,
         on_tournament_is_over=on_my_tournament_is_over,
         on_end=on_my_end)
