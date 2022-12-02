moves = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "rock",
    "Y": "paper",
    "Z": "scissors",
}


shape_scores = {"rock": 1, "paper": 2, "scissors": 3}


winning_games = (
    ("rock", "paper"),
    ("paper", "scissors"),
    ("scissors", "rock"),
)


def score_for_round(opponent, player):
    score = shape_scores[moves[player]]
    if moves[opponent] == moves[player]:
        score += 3
    elif (moves[opponent], moves[player]) in winning_games:
        score += 6
    return score
