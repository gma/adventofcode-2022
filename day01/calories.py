def totals(data):
    totals = []
    lines = data.strip()
    if lines:
        for part in lines.split("\n\n"):
            calories = sum(int(line) for line in part.splitlines())
            totals.append(calories)
    return totals


def largest_totals(data, *, num):
    calories = totals(data)
    calories.sort()
    return list(reversed(calories))[:num]


if __name__ == "__main__":
    print(max(totals(open('input').read())))
    print(sum(largest_totals(open('input').read(), num=3)))
