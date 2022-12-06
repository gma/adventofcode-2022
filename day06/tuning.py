def marker_position(data):
    marker_width = 4
    for i in range(marker_width - 1, len(data) + 1):
        potential_marker = data[max(0, i - marker_width) : i]
        if len(set(potential_marker)) == marker_width:
            return i
    return None


if __name__ == "__main__":
    print(marker_position(open("input").read()))
