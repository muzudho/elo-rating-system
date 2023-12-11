#
# python step_1_1_0.py
#
import random

counts = [0,0,0]


def main(
        on_result,
        on_end):
    print("Please input round number(1-100):")
    round = int(input())


    for i in range(0, round):
        result_1 = gyanken()

        counts[result_1] += 1

        on_result(result_1)

    on_end()


if __name__ == "__main__":

    # 0, 1, 2 のいずれかを返す
    def gyanken():
        return random.randint(0, 2)


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
        print(f"aiko: {counts[0]}, A win: {counts[1]}, B win: {counts[2]}")


    main(on_result=on_result_1,
         on_end=on_end_1)
