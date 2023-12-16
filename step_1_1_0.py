#
# python step_1_1_0.py
#
from step_1_0 import main, execute_tournament, play_game


if __name__ == "__main__":

    # プレイヤーのデータベース（まだない）
    player_database = {}

    # 集計（Totalization）
    # [0] あいこの数, [1] Aの勝利数, [2] Bの勝利数
    total_games = [0,0,0]


    def on_my_tournament_is_start():
        """大会開始時"""
        pass


    def on_my_tournament_is_over():
        """大会終了時"""

        # データベースへの反映は、今回は行いません

        # 集計の表示
        print(f"aiko: {total_games[0]}, A win: {total_games[1]}, B win: {total_games[2]}")


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

        if result == 0:
            print("aiko")
        elif result == 1:
            print("A win")
        elif result == 2:
            print("B win")
        else:
            print("Error")

        total_games[result] += 1


    # プログラムの実行
    main(
        player_database = player_database,
        on_tournament_is_start = on_my_tournament_is_start,
        on_tournament_executing = execute_tournament,
        on_tournament_is_over=on_my_tournament_is_over,
        on_game_start = on_my_game_start,
        on_game_playing=play_game,
        on_game_over=on_my_game_over)
