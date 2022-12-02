import rps


def test_calculate_score_for_drawn_round():
    rock_score = 1
    scissors_score = 3
    draw_score = 3

    assert rps.score_for_round("A", "X") == rock_score + draw_score
    assert rps.score_for_round("C", "Z") == scissors_score + draw_score
