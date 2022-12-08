import io

import pytest

import trees


test_data = """\
30373
25512
65332
33549
35390
"""


def test_load_grid_returns_sequence_of_sequences():
    assert trees.load_grid(io.StringIO("12\n34\n")) == [[1, 2], [3, 4]]


class TestVisibility:
    def test_tree_is_visible_when_taller_than_trees_to_its_left(self):
        assert trees.visible_from_start(1, sequence=[1, 2, 2])

    def test_tree_is_visible_when_taller_than_trees_to_its_right(self):
        assert trees.visible_from_end(1, sequence=[2, 2, 1])

    def test_visible_internal_trees_finds_the_right_trees(self):
        grid = trees.load_grid(io.StringIO(test_data))

        assert len(trees.visible_trees(grid)) == 21


def test_part1_solution():
    assert trees.part1(io.StringIO(test_data)) == 21
