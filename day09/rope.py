class Knot:
    def __init__(self, label, x=0, y=0):
        self.label = label
        self.x = x
        self.y = y
        self.track = []
        self.observers = []

    def __repr__(self):
        return f"self.__class__.__name__({self.label}, {self.x}, {self.y})"

    @property
    def coords(self):
        return (self.x, self.y)

    def go(self, direction):
        transforms = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}
        self.transform(transforms[direction])

    def transform(self, transform):
        self.x += transform[0]
        self.y += transform[1]
        for observer in self.observers:
            observer.keep_in_contact(self)

    def follow(self, knot):
        knot.observers.append(self)

    def step_towards(self, delta):
        return delta // abs(delta)

    def keep_in_contact(self, followed_knot):
        delta_v = followed_knot.y - self.y
        delta_h = followed_knot.x - self.x

        step_h = 0
        step_v = 0
        if (abs(delta_v) > 1 and abs(delta_h) >= 1) or (
            abs(delta_h) > 1 and abs(delta_v) >= 1
        ):
            step_h = self.step_towards(delta_h)
            step_v = self.step_towards(delta_v)
        elif abs(delta_v) > 1:
            step_v = self.step_towards(delta_v)
        elif abs(delta_h) > 1:
            step_h = self.step_towards(delta_h)
        self.transform((step_h, step_v))

        self.track.append((self.x, self.y))


def moves(file):
    for line in file:
        direction, steps = line.split()
        for _ in range(0, int(steps)):
            yield direction


def part1(file):
    head = Knot("H")
    tail = Knot("T")
    tail.follow(head)

    for direction in moves(file):
        head.go(direction)

    return len(set(tail.track))


def part2(file):
    knots = [Knot("H")]
    for i in range(1, 10):
        knot = Knot(i)
        knot.follow(knots[-1])
        knots.append(knot)
    head, tail = knots[0], knots[-1]

    for direction in moves(file):
        head.go(direction)

    return len(set(tail.track))


if __name__ == "__main__":
    with open("input") as f:
        lines = f.readlines()
    print(part1(lines))
    print(part2(lines))
