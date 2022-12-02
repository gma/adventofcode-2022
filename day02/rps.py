import collections


char_shapes = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "rock",
    "Y": "paper",
    "Z": "scissors",
}


shape_scores = {"rock": 1, "paper": 2, "scissors": 3}


Win = collections.namedtuple("Win", "opponent player")
winning_games = (
    Win("rock", "paper"),
    Win("paper", "scissors"),
    Win("scissors", "rock"),
)


def score_for_round(opponent_char, player_char):
    opponent_shape = char_shapes[opponent_char]
    player_shape = char_shapes[player_char]

    score = shape_scores[player_shape]
    if opponent_shape == player_shape:
        score += 3
    elif (opponent_shape, player_shape) in winning_games:
        score += 6
    return score


if __name__ == "__main__":
    rounds = open("input").readlines()
    print(sum(score_for_round(*game.split()) for game in rounds))
