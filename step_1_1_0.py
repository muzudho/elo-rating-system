#
# python step_1_1_0.py
#
import random

games = [0,0,0]


# 0, 1, 2 のいずれかを返す
def on_gyanken_1():
    return random.randint(0, 2)


def main(
        on_gyanken,
        on_result,
        on_end):

    print("Please input round number(1-100):")
    round = int(input())


    for i in range(0, round):
        result_1 = on_gyanken()

        games[result_1] += 1

        on_result(result_1)

    on_end()


if __name__ == "__main__":

    def on_result_1(result):
        if result == 0:
            print("aiko")
        elif result == 1:
            print("A win")
        elif result == 2:
            print("B win")
        else:
            print("Error")


    def on_end_1():
        print(f"aiko: {games[0]}, A win: {games[1]}, B win: {games[2]}")


    main(on_gyanken=on_gyanken_1,
         on_result=on_result_1,
         on_end=on_end_1)
