import rps


rock_score = 1
paper_score = 2
scissors_score = 3


class TestPart1:
    def test_calculate_score_for_drawn_round(self):
        draw_score = 3

        assert rps.score_for_round("A", "A") == rock_score + draw_score
        assert rps.score_for_round("C", "C") == scissors_score + draw_score


    def test_calculate_score_for_win(self):
        win_score = 6

        assert rps.score_for_round("A", "B") == paper_score + win_score


class TestPart2:
    def test_losing_move_char_returns_correct_char(self):
        assert rps.losing_move_char("A") == "C"
        assert rps.losing_move_char("B") == "A"
        assert rps.losing_move_char("C") == "B"

    def test_drawing_move_char_returns_correct_char(self):
        assert rps.drawing_move_char("A") == "A"

    def test_winning_move_char_returns_correct_char(self):
        assert rps.winning_move_char("A") == "B"
        assert rps.winning_move_char("B") == "C"
        assert rps.winning_move_char("C") == "A"
