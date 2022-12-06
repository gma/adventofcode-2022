import collections


def is_marker(marker):
    return len(set(marker)) == marker.maxlen


def find_marker(data, *, width):
    potential_marker = collections.deque(maxlen=width)
    for i, char in enumerate(data):
        potential_marker.append(char)
        if is_marker(potential_marker):
            return i + 1


def find_packet(data):
    return find_marker(data, width=4)


def find_message(data):
    return find_marker(data, width=14)


if __name__ == "__main__":
    print(find_packet(open("input").read()))
    print(find_message(open("input").read()))
