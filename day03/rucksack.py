import string


def common_item(items1, items2):
    common_to_both = set(items1).intersection(set(items2))
    return common_to_both.pop()


def item_priority(item):
    return string.ascii_letters.index(item) + 1


def compartment_contents(items):
    items_per_compartment = len(items) // 2
    compartment1 = items[0:items_per_compartment]
    compartment2 = items[items_per_compartment:]
    return (compartment1, compartment2)


if __name__ == "__main__":
    print(
        sum(
            item_priority(common_item(*compartment_contents(bag)))
            for bag in open("input").readlines()
        )
    )
