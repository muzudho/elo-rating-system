#
# python step_4_0.py
#
# じゃんけんの代わりに、数字を使った対局に変更
#
import random

from step_1_0 import main
from step_2_0 import calculate_moving_rating_that_a_wins,\
        calculate_moving_rating_that_b_wins, print_drawn, print_a_win, print_b_win
from step_2_1_0 import GameRecord, save_game_records
from step_3_0 import print_tournament_result, execute_tournament


def play_game(sente_id, gote_id, player_database):
    """対局をする。

    Parameters
    ----------
    sente_id : str
        先手のプレイヤーId
    gote_id : str
        後手のプレイヤーId
    player_database : object
        プレイヤー・データベース
    
    Returns
    -------
    0: あいこ
    1: プレイヤー１の勝ち
    2: プレイヤー２の勝ち のいずれかを返す
    """

    sente_player_record = list(filter(lambda item : item["id"] == sente_id, player_database))[0]
    gote_player_record = list(filter(lambda item : item["id"] == gote_id, player_database))[0]
    
    sente_bp = random.randint(0, sente_player_record['battle_point'])
    gote_bp = random.randint(0, gote_player_record['battle_point'])

    # 先手の勝ち
    if gote_bp + 100 < sente_bp:
        return 1
    
    # 後手の勝ち
    elif sente_bp + 100 < gote_bp:
        return 2

    # 引分け
    else:
        return 0


if __name__ == "__main__":

    # プレイヤーのデータベース
    # 操作のしやすさから、辞書ではなくリストを使う
    # ここでのイロ・レーティングの初期値（R0）：　2000
    player_database = [
        {
            # Id
            "id" : "player_1",
            # 表示名
            "display_name" : "Alice",
            # レーティング
            "rating" : 2000,
            # 戦闘力
            "battle_point": 10000,
        },
        {
            # Id
            "id" : "player_2",
            "display_name" : "Bob",
            "rating" : 2000,
            # 戦闘力
            "battle_point": 5000,
        },
        {
            # Id
            "id" : "player_3",
            "display_name" : "Charley",
            "rating" : 2000,
            # 戦闘力
            "battle_point": 2500,
        },
        {
            # Id
            "id" : "player_4",
            "display_name" : "Dingo",
            "rating" : 2000,
            # 戦闘力
            "battle_point": 1250,
        },
        {
            # Id
            "id" : "player_5",
            "display_name" : "Eric",
            "rating" : 2000,
            # 戦闘力
            "battle_point": 625,
        },
        {
            # Id
            "id" : "player_6",
            "display_name" : "Francisca",
            "rating" : 2000,
            # 戦闘力
            "battle_point": 312,
        },
    ]
    
    # 集計（Totalization）
    # [0] あいこの数, [1] Aの勝利数, [2] Bの勝利数
    total_games = [0,0,0]

    # Constant K
    K = 32

    # 対局の記録
    game_records = []


    def on_my_tournament_is_start():
        """大会開始時"""
        # 開始
        # プレイヤーのデータベースから、プレイヤーを選ぶ
        two_player_records = random.sample(player_database, 2)
        # ２プレイヤーのレーティングを表示したい

        print(f"""\
+-------+
| start |
+-------+
* ratings: {two_player_records[0]['display_name']} {two_player_records[0]['rating']}, {two_player_records[1]['display_name']} {two_player_records[1]['rating']}\
""")


    def on_my_tournament_is_over():

        # TODO データベースへの反映を、今回は行いたい

        # 大会結果の表示
        print_tournament_result(
            total_games=total_games,
            ratings=[0,0,0], # Obsoleted
            player_database=player_database)

        # 対局記録をファイルへ保存
        save_game_records(
            path='data_output/step_3_0.csv',
            game_records=game_records)


    def on_my_game_start(
            sente_id,
            gote_id):
        """対局開始時
        
        Parameters
        ----------
        sente_id : str
            先手プレイヤーのId
        gote_id : str
            後手プレイヤーのId
        """
        pass


    def on_my_game_over(
            sente_id,
            gote_id,
            result):
        """対局終了時

        Parameters
        ----------
        sente_id : str
            先手プレイヤーのId
        gote_id : str
            後手プレイヤーのId
        result : int
            0: あいこ
            1: プレイヤー１の勝ち
            2: プレイヤー２の勝ち
        """

        sente_player_record = list(filter(lambda item : item["id"] == sente_id, player_database))[0]
        gote_player_record = list(filter(lambda item : item["id"] == gote_id, player_database))[0]

        # あいこ
        if result == 0:
            # レーティングは動きません

            # 対局の記録
            game_records.append(GameRecord(
                player_name_1="A",
                player_name_2="B",
                win_player=0,
                player_1_rating_before_game = sente_player_record['rating'],
                player_2_rating_before_game = gote_player_record['rating'],
                moving_rating_after_game=0))

            # 表示
            print_drawn(
                ratings=[0, sente_player_record['rating'], gote_player_record['rating']])

        # A が勝った
        elif result == 1:
            # レーティングの変動
            answers = calculate_moving_rating_that_a_wins(
                K=K,
                ratings=[0, sente_player_record['rating'], gote_player_record['rating']])

            # 対局の記録
            game_records.append(GameRecord(
                player_name_1="A",
                player_name_2="B",
                win_player=1,
                player_1_rating_before_game = sente_player_record['rating'],
                player_2_rating_before_game = gote_player_record['rating'],
                moving_rating_after_game=answers["moving_rating"]))

            # TODO アルゴリズム高速化できんか？
            # データベースに反映
            update_count = 0
            for record in player_database:
                if record['id'] == sente_player_record['id']:
                    record['rating'] = sente_player_record["rating"]
                    update_count += 1
                    if 2 <= update_count:
                        break

                elif record['id'] == gote_player_record['id']:
                    record['rating'] = gote_player_record["rating"]
                    update_count += 1
                    if 2 <= update_count:
                        break

            sente_player_record["rating"] += answers["moving_rating"]
            gote_player_record["rating"] -= answers["moving_rating"]

            # 表示
            print_a_win(
                ratings=[0, sente_player_record['rating'], gote_player_record['rating']],
                K=K,
                answers=answers,
                sente_player_record = sente_player_record,
                gote_player_record = gote_player_record)

        # B が勝った
        elif result == 2:
            # レーティングの変動
            answers = calculate_moving_rating_that_b_wins(
                K=K,
                ratings=[0, sente_player_record['rating'], gote_player_record['rating']])

            # 対局の記録
            game_records.append(GameRecord(
                player_name_1="A",
                player_name_2="B",
                win_player=2,
                player_1_rating_before_game = sente_player_record['rating'],
                player_2_rating_before_game = gote_player_record['rating'],
                moving_rating_after_game=answers["moving_rating"]))

            # TODO アルゴリズム高速化できんか？
            # データベースに反映
            update_count = 0
            for record in player_database:
                if record['id'] == sente_player_record['id']:
                    record['rating'] = sente_player_record["rating"]
                    update_count += 1
                    if 2 <= update_count:
                        break

                elif record['id'] == gote_player_record['id']:
                    record['rating'] = gote_player_record["rating"]
                    update_count += 1
                    if 2 <= update_count:
                        break

            gote_player_record["rating"] += answers["moving_rating"]
            sente_player_record["rating"] -= answers["moving_rating"]

            # 表示
            print_b_win(
                ratings=[0, sente_player_record['rating'], gote_player_record['rating']],
                K=K,
                answers=answers,
                sente_player_record = sente_player_record,
                gote_player_record = gote_player_record)

        else:
            print("Error")

        total_games[result] += 1

    # プログラムの実行
    main(
        player_database=player_database,
        on_tournament_is_start = on_my_tournament_is_start,
        on_tournament_executing=execute_tournament,
        on_tournament_is_over=on_my_tournament_is_over,
        on_game_start = on_my_game_start,
        on_game_playing=play_game,
        on_game_over=on_my_game_over)
