moves = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "rock",
    "Y": "paper",
    "Z": "scissors",
}


shape_scores = {"rock": 1, "paper": 2, "scissors": 3}


def score_for_round(opponent, player):
    score = shape_scores[moves[player]]
    if moves[opponent] == moves[player]:
        score += 3
    return score
