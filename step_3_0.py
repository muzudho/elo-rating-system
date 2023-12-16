#
# python step_3_0.py
#
# プレイヤーのデータベースを連想配列で作る
#
import random
from step_1_0 import main, execute_tournament, gyanken
from step_2_0 import calculate_moving_rating_that_a_wins,\
        calculate_moving_rating_that_b_wins, print_drawn, print_a_win, print_b_win
from step_2_1_0 import GameRecord, save_game_records


def execute_tournament(
        player_database,
        round,
        on_tournament_is_over,
        on_gyanken,
        on_game_over):
    """大会実行のフレームワーク

    集計は、大会の実行の外に出す

    Parameters
    ----------
    player_database : object
        プレイヤー・データベース
    round : int
        対局数
    on_tournament_is_over : func
        大会終了時
    on_game_over : func
        対局終了時
    on_gyanken : func
        対局実行
    """

    for i in range(0, round):

        # TODO プレイヤーのデータベースから、プレイヤーのIdを２つ選びたい
        two_player_records = random.sample(player_database, 2)

        sente_id = two_player_records[0]["id"]
        gote_id = two_player_records[1]["id"]

        # 対局実行
        result = on_gyanken(
            sente_id=sente_id,
            gote_id=gote_id,
            player_database=player_database)

        # 結果
        on_game_over(result)

    # 大会終了時
    on_tournament_is_over()


def print_tournament_result(total_games, ratings, player_database):
    """大会終了時の表示"""

    # プレイヤーをレーティング順に並べて表示したい
    # 各プレイヤーを配列へ入れる
    player_ranking = []

    for player_record in player_database:
        player_ranking.append(player_record)

    # レーティング順にソートする
    # https://www.geeksforgeeks.org/ways-sort-list-dictionaries-values-python-using-lambda-function/
    player_ranking = sorted(player_ranking, key=lambda item: item['rating'])

    print(f"""\
+-------------------+
| tournament result |
+-------------------+\
""")
    print_players_record(player_ranking)


def print_players_record(player_record_list):
    """プレイヤーの記録を表示"""
    for player_record in player_record_list:
        print(f"""\
* name: {player_record['display_name']:16}, rating: {player_record['rating']:4}\
""")


if __name__ == "__main__":

    # プレイヤーのデータベース
    # 操作のしやすさから、辞書ではなくリストを使う
    player_database = [
        {
            # Id
            "id" : "player_1",
            # 表示名
            "display_name" : "Alice",
            # レーティング
            "rating" : 2000,
        },
        {
            # Id
            "id" : "player_2",
            "display_name" : "Bob",
            "rating" : 2000,
        },
        {
            # Id
            "id" : "player_3",
            "display_name" : "Charley",
            "rating" : 2000,
        },
    ]

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

    # 対局の記録
    game_records = []


    def on_my_tournament_is_over():

        # TODO データベースへの反映を、今回は行いたい

        # 大会結果の表示
        print_tournament_result(total_games, ratings, player_database)

        # 対局記録をファイルへ保存
        save_game_records(
            path='data_output/step_3_0.csv',
            game_records=game_records)


    def on_my_game_start():
        """対局開始時"""
        pass


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

            # 対局の記録
            game_records.append(GameRecord(
                player_name_1="A",
                player_name_2="B",
                win_player=0,
                player_1_rating_before_game=ratings[1],
                player_2_rating_before_game=ratings[2],
                moving_rating_after_game=0))

            print_drawn(ratings)

        # A が勝った
        elif result == 1:
            # レーティングの変動
            answers = calculate_moving_rating_that_a_wins(K, ratings)

            # 対局の記録
            game_records.append(GameRecord(
                player_name_1="A",
                player_name_2="B",
                win_player=1,
                player_1_rating_before_game=ratings[1],
                player_2_rating_before_game=ratings[2],
                moving_rating_after_game=answers["moving_rating"]))

            ratings[1] += answers["moving_rating"]
            ratings[2] -= answers["moving_rating"]

            print_a_win(ratings, K, answers)

        # B が勝った
        elif result == 2:
            # レーティングの変動
            answers = calculate_moving_rating_that_b_wins(K, ratings)

            # 対局の記録
            game_records.append(GameRecord(
                player_name_1="A",
                player_name_2="B",
                win_player=2,
                player_1_rating_before_game=ratings[1],
                player_2_rating_before_game=ratings[2],
                moving_rating_after_game=answers["moving_rating"]))

            ratings[2] += answers["moving_rating"]
            ratings[1] -= answers["moving_rating"]

            print_b_win(ratings, K, answers)

        else:
            print("Error")

        total_games[result] += 1


    # 開始
    print(f"""\
+-------+
| start |
+-------+\
* ratings: A {ratings[1]}, B {ratings[2]}""")

    # プログラムの実行
    main(
        player_database=player_database,
        on_tournament_executing=execute_tournament,
        on_tournament_is_over=on_my_tournament_is_over,
        on_game_start = on_my_game_start,
        on_gyanken=gyanken,
        on_game_over=on_my_game_over)
