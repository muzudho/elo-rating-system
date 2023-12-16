#
# cd src_epoch_1_0
# python step_1_0.py
#
import random


def main():
    """プログラムのフレームワーク
    
    集計は、このプログラムのフレームワークの外に出す

    Parameters
    ----------
    player_database : object
        プレイヤー・データベース
    on_tournament_is_start: func
        大会開始時
    on_tournament_executing : func
        大会のフレームワーク
    on_tournament_is_over: func
        大会終了時
    """

    # 大会開始時

    # ラウンド数を入力
    print("Please input round number(1-100):")
    round = int(input())

    # 大会の実行
    for i in range(0, round):

        # 対局開始

        # 対局実行
        #
        # Returns
        # -------
        # 0: あいこ
        # 1: プレイヤー１の勝ち
        # 2: プレイヤー２の勝ち のいずれかを返す
        result = random.randint(0, 2)

        # 結果
        if result == 0:
            print("aiko")
        elif result == 1:
            print("A win")
        elif result == 2:
            print("B win")
        else:
            print("Error")

        # 集計
        total_games[result] += 1

    # 大会終了時
    #   データベースへの反映は、今回は行いません
    #   集計の表示
    print(f"aiko: {total_games[0]}, A win: {total_games[1]}, B win: {total_games[2]}")


if __name__ == "__main__":

    # 集計（Totalization）
    # [0] あいこの数, [1] Aの勝利数, [2] Bの勝利数
    total_games = [0,0,0]

    # プログラムの実行
    main()
