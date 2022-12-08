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


if __name__ == "__main__":
    print(part1(open("input")))
