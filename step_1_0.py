import random
#
# python step_1_0.py
#

# 0, 1, 2 のいずれかを返す
def gyanken():
    return random.randint(0, 2)

if __name__ == "__main__":

    print("Please input round number(1-100):")
    round = int(input())

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
