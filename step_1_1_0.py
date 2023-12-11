#
# python step_1_1_0.py
#
import random

counts = [0,0,0]

# 0, 1, 2 のいずれかを返す
def gyanken():
    return random.randint(0, 2)

def on_result_1(result):
    counts[result] += 1

def main(on_result):
    print("Please input round number(1-100):")
    round = int(input())


    for i in range(0, round):
        result_1 = gyanken()

        on_result(result_1)

        if result_1 == 0:
            print("aiko")
        elif result_1 == 1:
            print("A win")
        elif result_1 == 2:
            print("B win")
        else:
            print("Error")

    print(f"aiko: {counts[0]}, A win: {counts[1]}, B win: {counts[2]}")


if __name__ == "__main__":
    main(on_result=on_result_1)
