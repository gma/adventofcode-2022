def read_stack_lines(file):
    lines = []
    for line in file:
        if line == "\n":
            break
        lines.append(line.rstrip("\n"))
    lines.reverse()
    return lines


def parse_crates(line):
    width = 4
    crates = tuple(line[i : i + width] for i in range(0, len(line), width))
    return tuple(None if crate.isspace() else crate[1] for crate in crates)


def load_stacks(file):
    lines = read_stack_lines(file)
    labels = lines[0].split()
    stacks = [[] for _ in range(len(labels))]

    for line in lines[1:]:
        for i, crate in enumerate(parse_crates(line)):
            if crate is not None:
                stacks[i].append(crate)
    return stacks


def read_move(file):
    for line in file:
        yield [int(n) for n in line.split()[1::2]]


def move_crates(stacks, file):
    for to_move, source, destination in read_move(file):
        for _ in range(to_move):
            crate = stacks[source - 1].pop()
            stacks[destination - 1].append(crate)
    return stacks
