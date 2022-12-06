import collections


marker_width = 4


def is_marker(marker):
    return len(set(marker)) == marker_width


def marker_position(data):
    potential_marker = collections.deque([], marker_width)
    for i, char in enumerate(data):
        potential_marker.append(char)
        if is_marker(potential_marker):
            return i + 1


if __name__ == "__main__":
    print(marker_position(open("input").read()))
