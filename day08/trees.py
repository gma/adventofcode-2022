def load_grid(file):
    return [[int(height) for height in line.strip()] for line in file]


def part1(file):
    plantation = load_grid(file)
    return num_edge_trees(plantation) + len(visible_internal_trees(plantation))
