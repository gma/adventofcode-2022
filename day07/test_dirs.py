import io

import pytest

import dirs


class TestTree:
    def test_from_log_adds_dirs_in_cd_command_to_current_directory(self):
        log = """\
$ cd /
$ ls
dir dir1
123 file1
$ cd dir1
"""
        tree = dirs.Tree.from_log(io.StringIO(log))

        assert "dir1" in tree["/"]

    def test_from_log_adjusts_current_directory_when_cd_to_parent(self):
        log = """\
$ cd /
$ cd dir1
$ cd ..
$ cd dir2
"""
        tree = dirs.Tree.from_log(io.StringIO(log))

        assert "dir2" in tree["/"]

    def test_from_log_uses_ls_output_to_track_files_in_current_directory(self):
        log = """\
$ cd /
$ ls
123 file1
"""
        tree = dirs.Tree.from_log(io.StringIO(log))

        assert "file1" in tree["/"]
        assert tree["/"]["file1"].size == 123

    def test_from_log_tallies_size_of_files_directly_inside_directory(self):
        log = """\
$ cd /
$ ls
123 file1
456 file2
"""
        tree = dirs.Tree.from_log(io.StringIO(log))

        assert tree["/"].size == 123 + 456

    def test_tree_allows_us_to_iterate_over_descendent_directories(self):
        log = """\
$ cd /
$ cd dir1
$ ls
123 file1
$ cd dir2
$ cd ..
$ cd ..
$ cd dir3
"""
        tree = dirs.Tree.from_log(io.StringIO(log))

        expected = ["/", "dir1", "dir2", "dir3"]
        assert [d.name for d in tree.directories] == expected


test_data = """\
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""


def test_part1_solution():
    size_of_e = 584
    size_of_a = size_of_e + 29116 + 2557 + 62596
    expected = size_of_e + size_of_a

    assert dirs.part1(io.StringIO(test_data)) == expected
