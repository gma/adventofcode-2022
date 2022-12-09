import collections
import sys


def display(items, xmin=-10, xmax=10, ymin=-10, ymax=10, pausing=False):
    """Display item labels in grid of dots

    Each item is expected to have the attributes label, x and y.

    """
    grid = collections.defaultdict(lambda: ".")
    for item in reversed(items):
        grid[(item.x, item.y)] = item.label

    for y in range(ymax - 1, ymin - 1, -1):
        for x in range(xmin, xmax):
            sys.stdout.write(str(grid[(x, y)]))
        print()
    print()

    if pausing:
        input()
