import collections


File = collections.namedtuple("File", "name size")


class Tree:
    @classmethod
    def from_log(cls, file):
        root = cls(None, None)
        cwd = root
        for line in file:
            if line.startswith("$ cd"):
                name = line.split()[2]
                cwd = cwd.parent if name == ".." else cwd.add_subdir(name)
            elif line.startswith("$ ls"):
                pass
            else:
                size, name = line.split(maxsplit=2)
                cwd.add_file(name, size)
        return root

    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.contents = {}

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name!r}, {self.parent!r})"

    def __contains__(self, name):
        return name in self.contents

    def __getitem__(self, name):
        return self.contents[name]

    def add_subdir(self, name):
        directory = self.__class__(name, self)
        self.contents[name] = directory
        return directory

    def add_file(self, name, size):
        try:
            size = int(size)
        except ValueError:
            pass
        else:
            self.contents[name] = File(name, size)

    @property
    def size(self):
        return sum(f.size for f in self.contents.values())

    @property
    def directories(self):
        dirs = [self] if self.parent is not None else []
        for file_or_directory in self.contents.values():
            if hasattr(file_or_directory, "directories"):
                dirs.extend(file_or_directory.directories)
        return dirs


def part1(file):
    tree = Tree.from_log(file)
    return sum(d.size for d in tree.directories if d.size <= 100000)


def part2(file):
    tree = Tree.from_log(file)
    space_used = tree["/"].size
    space_required = 30_000_000 - (70_000_000 - space_used)

    candidates = [d for d in tree.directories if d.size >= space_required]
    candidates.sort(key=lambda d: d.size)
    return candidates[0].size


if __name__ == "__main__":
    print(part1(open("input")))
    print(part2(open("input")))
