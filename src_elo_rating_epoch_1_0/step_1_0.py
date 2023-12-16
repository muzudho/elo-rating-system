#
# cd src_elo_rating_epoch_1_0
#
# このファイルはライブラリなので、実行しても何もしません
#
import math

def calculate_moving_rating_that_a_wins(K, ratings):
    """A が勝った時のレーティングの移動量

    Parameters
    ----------
    K : int
        定数Ｋ。一般的に 32 とか 16 とかの整数
    ratings : list
        レーティング。 [0]未使用, [1]先手プレイヤーのレーティング, [2]後手プレイヤーのレーティング
    """

    result = {}

    # b から見た a とのレーティング差
    result["difference_b_to_a"] = ratings[1] - ratings[2]
    result["difference_b_to_a_formula"] = f"{ratings[1]}<a> - {ratings[2]}<b>"

    # b から見た a に１勝するために必要な対局数
    result["games_b_to_a"] = get_games_by_rating_difference(result["difference_b_to_a"])
    result["games_b_to_a_formula"] = get_formula_games_by_rating_difference(result["difference_b_to_a"])

    # b から見た a への勝率
    # b がレーティング上位者なら
    if ratings[1] < ratings[2]:
        result["Wba"] = get_win_rate_for_upper_rating(result["games_b_to_a"])
        result["Wba_formula"] = get_formula_win_rate_for_upper_rating(result["games_b_to_a"])
    # b がレーティング同等または下位者なら
    else:
        result["Wba"] = get_win_rate_for_lower_rating(result["games_b_to_a"])
        result["Wba_formula"] = get_formula_win_rate_for_lower_rating(result["games_b_to_a"])

    # レーティングの移動量
    result["moving_rating"] = math.floor(K * result["Wba"])
    result["moving_rating_formula"] = f"math.floor({K} * {result['Wba']})"
    return result

def calculate_moving_rating_that_b_wins(K, ratings):
    """B が勝った時のレーティングの移動量

    Parameters
    ----------
    K : int
        定数Ｋ。一般的に 32 とか 16 とかの整数
    ratings : list
        レーティング。 [0]未使用, [1]先手プレイヤーのレーティング, [2]後手プレイヤーのレーティング
    """

    result = {}

    # a から見た b とのレーティング差
    result["difference_a_to_b"] = ratings[2] - ratings[1]
    result["difference_a_to_b_formula"] = f"{ratings[2]}<b> - {ratings[1]}<a>"

    # a から見た b に１勝するために必要な対局数
    result["games_a_to_b"] = get_games_by_rating_difference(result["difference_a_to_b"])
    result["games_a_to_b_formula"] = get_formula_games_by_rating_difference(result["difference_a_to_b"])

    # a から見た b への勝率
    # a がレーティング上位者なら
    if ratings[2] < ratings[1]:
        result["Wab"] = get_win_rate_for_upper_rating(result["games_a_to_b"])
        result["Wab_formula"] = get_formula_win_rate_for_upper_rating(result["games_a_to_b"])
    # a がレーティング同等または下位者なら
    else:
        result["Wab"] = get_win_rate_for_lower_rating(result["games_a_to_b"])
        result["Wab_formula"] = get_formula_win_rate_for_lower_rating(result["games_a_to_b"])

    # レーティングの移動量
    result["moving_rating"] = math.floor(K * result["Wab"])
    result["moving_rating_formula"] = f"math.floor({K} * {result['Wab']})"
    return result


def get_games_by_rating_difference(
        rating_difference):
    """１勝するために必要な対局数（暗記表の x ）を取得
    実数でも算出できるが、（1.0 以上の数になるよう数式を調整している前提で）整数にして返す

    Parameters
    ----------
    rating_difference : int
        暗記表の y
    """
    return math.floor(10 ** (abs(rating_difference) / 400))


def get_formula_games_by_rating_difference(
        rating_difference):
    """１勝するために必要な対局数（暗記表の x ）を取得
    実数でも算出できるが、（1.0 以上の数になるよう数式を調整している前提で）整数にして返す

    Parameters
    ----------
    rating_difference : int
        暗記表の y
    """
    return f"math.floor(10 ** (abs({rating_difference}) / 400))"


def get_rating_difference_by_games(
        games_number):
    """レーティング差（暗記表の y ）を取得

    Parameters
    ----------
    games_number : float
        暗記表の x : 実数
    """
    return math.floor(400 * math.log10(games_number))


def get_formula_rating_difference_by_games(
        games_number):
    """レーティング差（暗記表の y ）を取得

    Parameters
    ----------
    games_number : float
        暗記表の x : 実数
    """
    return f"math.floor(400 * math.log10({games_number}))"


def get_win_rate_for_upper_rating(win_games):
    """Win rate : 実数"""
    return win_games / (win_games + 1)


def get_formula_win_rate_for_upper_rating(win_games):
    """Win rate : 実数"""
    return f"{win_games} / ({win_games} + 1)"


def get_win_rate_for_lower_rating(win_games):
    """Win rate : 実数"""
    return 1 / (win_games + 1)


def get_formula_win_rate_for_lower_rating(win_games):
    """Win rate : 実数"""
    return f"1 / ({win_games} + 1)"
