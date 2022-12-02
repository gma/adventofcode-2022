import collections


char_shapes = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
}


shape_chars = {shape: char for char, shape in char_shapes.items()}


shape_scores = {"rock": 1, "paper": 2, "scissors": 3}


Game = collections.namedtuple("Game", "loser winner")
winning_games = (
    Game("rock", "paper"),
    Game("paper", "scissors"),
    Game("scissors", "rock"),
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


def losing_move_char(opponent_char):
    opponent_shape = char_shapes[opponent_char]
    game = list(filter(lambda g: g.winner == opponent_shape, winning_games))[0]
    return shape_chars[game.loser]


def drawing_move_char(opponent_char):
    return opponent_char


def winning_move_char(opponent_char):
    opponent_shape = char_shapes[opponent_char]
    game = list(filter(lambda g: g.loser == opponent_shape, winning_games))[0]
    return shape_chars[game.winner]


strategies = {
    "X": losing_move_char,
    "Y": drawing_move_char,
    "Z": winning_move_char,
}


strategies_as_move = {"X": "A", "Y": "B", "Z": "C"}


def part1(rounds):
    total = 0
    for game in rounds:
        opponent_char, player_char = game.split()
        total += score_for_round(opponent_char, strategies_as_move[player_char])
    print(total)


def part2(rounds):
    total = 0
    for game in rounds:
        opponent_char, strategy = game.split()
        player_char = strategies[strategy](opponent_char)
        total += score_for_round(opponent_char, player_char)
    print(total)


if __name__ == "__main__":
    rounds = open("input").readlines()
    part1(rounds)
    part2(rounds)
