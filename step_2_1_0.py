#
# python step_2_1_0.py
#
import math

from step_1_1_0 import on_gyanken_1, games, main
from step_2_0 import ratings, K, get_games_by_rating_difference, get_rating_difference_by_games,\
      get_win_rate_for_upper_rating, get_win_rate_for_lower_rating,calculate_moving_rating_that_a_wins,\
        calculate_moving_rating_that_b_wins


# 対局の記録
game_records = []


class GameRecord():
    """ゲームの記録"""

    def __init__(
            self,
            player_name_1,
            player_name_2,
            win_player,
            player_1_rating_before_game,
            player_2_rating_before_game,
            moving_rating_after_game):
        self._player_name_1 = player_name_1
        self._player_name_2 = player_name_2
        self._win_player = win_player
        self._player_1_rating_before_game = player_1_rating_before_game
        self._player_2_rating_before_game = player_2_rating_before_game
        self._moving_rating_after_game = moving_rating_after_game

    @property
    def player_name_1(self):
        return self._player_name_1

    @property
    def player_name_2(self):
        return self._player_name_2

    @property
    def win_player(self):
        """0:引分け, 1:プレイヤー１の勝ち, 2:プレイヤー２の勝ち"""
        return self._win_player

    @property
    def player_1_rating_before_game(self):
        return self._player_1_rating_before_game

    @property
    def player_2_rating_before_game(self):
        return self._player_2_rating_before_game

    @property
    def moving_rating_after_game(self):
        return self._moving_rating_after_game


if __name__ == "__main__":

    def on_result_1(result):

        # あいこ
        if result == 0:
            # レーティングは動きません
            game_records.append(GameRecord(
                player_name_1="A",
                player_name_2="B",
                win_player=0,
                player_1_rating_before_game=ratings[1],
                player_2_rating_before_game=ratings[2],
                moving_rating_after_game=0))

            print(f"""\
+------+
| aiko |
+------+
* ratings: A {ratings[1]}, B {ratings[2]}\
                  """)

        # A が勝った
        elif result == 1:
            # レーティングの変動
            result_2 = calculate_moving_rating_that_a_wins()

            game_records.append(GameRecord(
                player_name_1="A",
                player_name_2="B",
                win_player=1,
                player_1_rating_before_game=ratings[1],
                player_2_rating_before_game=ratings[2],
                moving_rating_after_game=result_2["moving_rating"]))

            ratings[1] += result_2["moving_rating"]
            ratings[2] -= result_2["moving_rating"]
            print(f"""\
+-------+
| A win |
+-------+
* K: {K},  ratings: A {ratings[1]}, B {ratings[2]}\
                  """)

        # B が勝った
        elif result == 2:
            # レーティングの変動
            result_2 = calculate_moving_rating_that_b_wins()

            game_records.append(GameRecord(
                player_name_1="A",
                player_name_2="B",
                win_player=2,
                player_1_rating_before_game=ratings[1],
                player_2_rating_before_game=ratings[2],
                moving_rating_after_game=result_2["moving_rating"]))

            ratings[2] += result_2["moving_rating"]
            ratings[1] -= result_2["moving_rating"]
            print(f"""\
+-------+
| B win |
+-------+
* K: {K},  ratings: A {ratings[1]}, B {ratings[2]}\
                  """)

        else:
            print("Error")


    def on_end_1():
        print(f"""\
+--------+
| result |
+--------+
* games:    aiko: {games[0]:4},  A win: {games[1]:4},  B win: {games[2]:4}
* ratings:  aiko: {ratings[0]:4},  A win: {ratings[1]:4},  B win: {ratings[2]:4}\
              """)

        # ファイルへ保存
        with open('data_output/step_2_1_0.csv', mode='w') as f:

            f.write(f"""\
player_1_name, player_1_rating_before_game, player_2_name, player_2_rating_before_game, win_player, moving_rating
""")

            for game_record in game_records:
                f.write(f"""\
{game_record.player_name_1}, {game_record.player_1_rating_before_game}, {game_record.player_name_2}, {game_record.player_2_rating_before_game}, {game_record.win_player}, {game_record.moving_rating_after_game}
""")


    print("""\
+-------+
| start |
+-------+\
          """)
    
    # レーティングは動きません
    print(f"* ratings: A {ratings[1]}, B {ratings[2]}")


    main(on_gyanken=on_gyanken_1,
         on_result=on_result_1,
         on_end=on_end_1)
