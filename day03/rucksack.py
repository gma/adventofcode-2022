import itertools
import string


def common_item(*bags):
    common = set(bags[0])
    for bag in bags[1:]:
        common = common.intersection(set(bag))
    return common.pop()


def item_priority(item):
    return string.ascii_letters.index(item) + 1


def compartment_contents(items):
    items_per_compartment = len(items) // 2
    compartment1 = items[0:items_per_compartment]
    compartment2 = items[items_per_compartment:]
    return (compartment1, compartment2)


def groups(file):
    for group in itertools.zip_longest(file, file, file):
        yield tuple(line.strip() for line in group)


if __name__ == "__main__":
    print(
        sum(
            item_priority(common_item(*compartment_contents(bag)))
            for bag in open("input")
        )
    )

    print(
        sum(
            item_priority(common_item(*group))
            for group in groups(open("input"))
        )
    )
