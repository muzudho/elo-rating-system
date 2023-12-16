#
# python step_2_1_0.py
#
from step_1_0 import main, on_my_tournament_executing, gyanken
from step_2_0 import calculate_moving_rating_that_a_wins,\
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

    # 集計（Totalization）
    # [0] あいこの数, [1] Aの勝利数, [2] Bの勝利数
    total_games = [0,0,0]

    # この対局でのレーティングについて
    # [0] : 未使用
    # [1] : プレイヤー１のレーティング
    # [2] : プレイヤー２のレーティング
    # 初期値：　R0 = 2000
    ratings = [0, 2000, 2000]

    # Constant K
    K = 32

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
            result_2 = calculate_moving_rating_that_a_wins(K, ratings)

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
            result_2 = calculate_moving_rating_that_b_wins(K, ratings)

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

        total_games[result] += 1


    def on_my_tournament_is_over():
        print(f"""\
+--------+
| result |
+--------+
* games:    aiko: {total_games[0]:4},  A win: {total_games[1]:4},  B win: {total_games[2]:4}
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


    # 開始
    print(f"""\
+-------+
| start |
+-------+\
* ratings: A {ratings[1]}, B {ratings[2]}""")

    # プログラムの実行
    main(
        on_tournament_executing=on_my_tournament_executing,
        on_gyanken=gyanken,
        on_game_over=on_my_game_over,
        on_tournament_is_over=on_my_tournament_is_over)
