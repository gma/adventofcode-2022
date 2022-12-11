import sys


class CPU:
    def __init__(self):
        self.register = 1

    def execute(self, instructions):
        for instruction in instructions:
            for _ in self.execute_op(instruction):
                yield self.register

    def execute_op(self, instruction):
        operation = instruction.split()
        method, args = getattr(self, operation[0]), operation[1:]
        for _ in method(*args):
            yield

    def noop(self):
        yield

    def addx(self, *args):
        yield
        yield
        self.register += int(args[0])


def signal_strength(cycle, register):
    return cycle * register


def part1(instructions):
    cycles = (20, 60, 100, 140, 180, 220)
    cpu = CPU()
    total = 0
    for i, register in enumerate(cpu.execute(instructions)):
        cycle = i + 1
        if cycle in cycles:
            total += signal_strength(cycle, register)
    return total


def part2(instructions):
    cpu = CPU()
    columns = 40
    for pixel, register in enumerate(cpu.execute(instructions)):
        sprite = range(register - 1, register + 2)
        sys.stdout.write("#" if pixel % columns in sprite else ".")
        if (pixel + 1) % columns == 0:
            sys.stdout.write("\n")


if __name__ == "__main__":
    with open("input") as file:
        instructions = file.readlines()
    print(part1(instructions))
    part2(open("input"))
