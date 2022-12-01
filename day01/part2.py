import part1


def greatest_calories(data, *, num):
    totals = part1.sum_calories(data)
    totals.sort()
    return list(reversed(totals))[:num]


if __name__ == "__main__":
    print(sum(greatest_calories(open('input').read(), num=3)))
