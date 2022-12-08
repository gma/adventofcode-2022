def load_grid(file):
    return [[int(height) for height in line.strip()] for line in file]


def visible_from_start(i, sequence):
    return all(sequence[i] > height for height in sequence[:i])


def visible_from_end(i, sequence):
    return all(sequence[i] > height for height in sequence[i + 1 :])


def visible_trees(grid):
    visible = []
    for y, row in enumerate(grid):
        for x in range(len(row)):
            col = [r[x] for r in grid]
            if (
                visible_from_start(x, row)
                or visible_from_end(x, row)
                or visible_from_start(y, col)
                or visible_from_end(y, col)
            ):
                visible.append((x, y))
    return visible


def part1(file):
    return len(visible_trees(load_grid(file)))


def score_to_start(i, sequence):
    score = 0
    for height in reversed(sequence[:i]):
        score += 1
        if height >= sequence[i]:
            break
    return score


def score_to_end(i, sequence):
    score = 0
    for height in sequence[i + 1 :]:
        score += 1
        if height >= sequence[i]:
            break
    return score


def scenic_score(x, y, grid):
    col = [row[x] for row in grid]
    return (
        score_to_start(x, grid[y])
        * score_to_end(x, grid[y])
        * score_to_start(y, col)
        * score_to_end(y, col)
    )


def scenic_scores(grid):
    scores = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            scores.append(scenic_score(x, y, grid))
    return scores


def part2(file):
    return max(scenic_scores(load_grid(file)))


if __name__ == "__main__":
    print(part1(open("input")))
    print(part2(open("input")))
