class Knot:
    def __init__(self, label, x=0, y=0):
        self.label = label
        self.x = x
        self.y = y
        self.track = []
        self.observers = []

    def __repr__(self):
        return f"self.__class__.__name__({self.label}, {self.x}, {self.y})"

    def go(self, direction):
        transforms = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}
        self.transform_position(transforms[direction])

    def transform_position(self, transform):
        self.x += transform[0]
        self.y += transform[1]
        for observer in self.observers:
            observer.keep_in_contact(self)

    def follow(self, knot):
        knot.observers.append(self)

    def transform_vertically(self, delta):
        self.transform_position((0, delta // abs(delta)))

    def transform_horizontally(self, delta):
        self.transform_position((delta // abs(delta), 0))

    def keep_in_contact(self, followed_knot):
        vertical_delta = followed_knot.y - self.y
        horizontal_delta = followed_knot.x - self.x

        if abs(vertical_delta) > 1 and abs(horizontal_delta) == 1:
            self.transform_vertically(vertical_delta)
            self.transform_horizontally(horizontal_delta)
        elif abs(horizontal_delta) > 1 and abs(vertical_delta) == 1:
            self.transform_vertically(vertical_delta)
            self.transform_horizontally(horizontal_delta)
        elif abs(vertical_delta) > 1:
            self.transform_vertically(vertical_delta)
        elif abs(horizontal_delta) > 1:
            self.transform_horizontally(horizontal_delta)

        self.track.append((self.x, self.y))


def part1(file):
    head = Knot("H")
    tail = Knot("T")
    tail.follow(head)

    for line in file:
        direction, steps = line.split()
        for _ in range(0, int(steps)):
            head.go(direction)

    return len(set(tail.track))


if __name__ == "__main__":
    print(part1(open("input")))
