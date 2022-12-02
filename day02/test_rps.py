import rps


rock_score = 1
paper_score = 2
scissors_score = 3


def test_calculate_score_for_drawn_round():
    draw_score = 3

    assert rps.score_for_round("A", "X") == rock_score + draw_score
    assert rps.score_for_round("C", "Z") == scissors_score + draw_score


def test_calculate_score_for_win():
    win_score = 6

    assert rps.score_for_round("A", "Y") == paper_score + win_score
