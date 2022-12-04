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


if __name__ == "__main__":
    print(part1(open("input")))
