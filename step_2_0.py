#
# python step_1_1_0.py
#
import random

from step_1_1_0 import on_gyanken_1, games, main

# R0 = 2000
ratings = [0, 2000, 2000]

# Constant K
K = 32

if __name__ == "__main__":

    def on_result_1(result):


        # レーティング差
        ab = ratings[1] - ratings[2]
        ba = ratings[2] - ratings[1]
        y = abs(ba)


        # 勝率
        wab = ab
        wba = ba


        if result == 0:
            # レーティングは動きません
            print(f"aiko  >  ratings A {ratings[1]}, B {ratings[2]}")

        elif result == 1:
            offset = K * wba
            ratings[1] += offset
            ratings[2] -= offset
            print(f"A win  >  ratings A {ratings[1]}, B {ratings[2]}")

        elif result == 2:
            offset = K * wab
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
