def sum_calories(data):
    totals = []
    lines = data.strip()
    if lines:
        for part in lines.split("\n\n"):
            calories = sum(int(line) for line in part.splitlines())
            totals.append(calories)
    return totals


def greatest_calories(data, *, num):
    totals = sum_calories(data)
    totals.sort()
    return list(reversed(totals))[:num]


if __name__ == "__main__":
    print(max(sum_calories(open('input').read())))
    print(sum(greatest_calories(open('input').read(), num=3)))
