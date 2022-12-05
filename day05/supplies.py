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


def remove_crates_9000(stack, count):
    for _ in range(count):
        yield stack.pop()


def remove_crates_9001(stack, count):
    return reversed(list(remove_crates_9000(stack, count)))


def move_crates(stacks, file, strategy=remove_crates_9000):
    for to_move, source, destination in read_move(file):
        for crate in strategy(stacks[source - 1], to_move):
            stacks[destination - 1].append(crate)
    return stacks


def part1(file):
    stacks = move_crates(load_stacks(file), file, strategy=remove_crates_9000)
    return "".join(stack[-1] for stack in stacks)


def part2(file):
    stacks = move_crates(load_stacks(file), file, strategy=remove_crates_9001)
    return "".join(stack[-1] for stack in stacks)


if __name__ == "__main__":
    print(part1(open("input")))
    print(part2(open("input")))
