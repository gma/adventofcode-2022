def sum_calories(data):
    totals = []
    lines = data.strip()
    if lines:
        for part in lines.split("\n\n"):
            calories = sum(int(line) for line in part.splitlines())
            totals.append(calories)
    return totals


if __name__ == "__main__":
    print(max(sum_calories(open('input').read())))
