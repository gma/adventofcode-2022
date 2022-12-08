def load_grid(file):
    return [[int(height) for height in line.strip()] for line in file]


def apply_til_start(f, i, sequence):
    return f(sequence[i], reversed(sequence[:i]))


def apply_til_end(f, i, sequence):
    return f(sequence[i], sequence[i + 1 :])


def trees_in_plantation(grid):
    for y, row in enumerate(grid):
        for x in range(len(row)):
            col = [r[x] for r in grid]
            yield x, y, row, col


def visible_from_outside(tree_height, trees):
    return all(tree_height > height for height in trees)


def visible_trees(grid):
    for x, y, row, col in trees_in_plantation(grid):
        if (
            apply_til_start(visible_from_outside, x, row)
            or apply_til_end(visible_from_outside, x, row)
            or apply_til_start(visible_from_outside, y, col)
            or apply_til_end(visible_from_outside, y, col)
        ):
            yield (x, y)


def part1(file):
    return len(list(visible_trees(load_grid(file))))


def viewing_distance(tree_height, trees):
    score = 0
    for height in trees:
        score += 1
        if height >= tree_height:
            break
    return score


def scenic_score(x, y, row, col):
    return (
        apply_til_start(viewing_distance, x, row)
        * apply_til_end(viewing_distance, x, row)
        * apply_til_start(viewing_distance, y, col)
        * apply_til_end(viewing_distance, y, col)
    )


def scenic_scores(grid):
    for x, y, row, col in trees_in_plantation(grid):
        yield scenic_score(x, y, row, col)


def part2(file):
    return max(scenic_scores(load_grid(file)))


if __name__ == "__main__":
    print(part1(open("input")))
    print(part2(open("input")))
