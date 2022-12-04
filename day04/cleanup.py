def sections_as_tuple(sections):
    lower, upper = [int(i) for i in sections.split("-")]
    return (lower, upper)


def contained_by(contained, *, container):
    return container[0] <= contained[0] <= contained[1] <= container[1]


def part1(file):
    count = 0
    for line in file:
        a, b = [sections_as_tuple(sections) for sections in line.split(",")]
        if contained_by(a, container=b) or contained_by(b, container=a):
            count += 1
    return count


def overlap(a, b):
    overlapping_range = range(max(a[0], b[0]), min(a[1], b[1]) + 1)
    return bool(overlapping_range)


def part2(file):
    return [
        overlap(*[sections_as_tuple(sections) for sections in line.split(",")])
        for line in file
    ].count(True)


if __name__ == "__main__":
    print(part1(open("input")))
    print(part2(open("input")))
