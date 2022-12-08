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
        assert trees.apply_til_start(trees.visible_from_outside, 1, [1, 2, 2])

    def test_tree_is_visible_when_taller_than_trees_to_its_right(self):
        assert trees.apply_til_end(trees.visible_from_outside, 1, [2, 2, 1])

    def test_visible_internal_trees_finds_the_right_trees(self):
        grid = trees.load_grid(io.StringIO(test_data))

        assert len(list(trees.visible_trees(grid))) == 21


def test_part1_solution():
    assert trees.part1(io.StringIO(test_data)) == 21


class TestScenicScore:
    def test_score_to_start_stops_at_edge_or_tree_at_least_as_tall(self):
        row = [2, 1, 2, 3, 3]

        assert trees.apply_til_start(trees.viewing_distance, 0, row) == 0
        assert trees.apply_til_start(trees.viewing_distance, 1, row) == 1
        assert trees.apply_til_start(trees.viewing_distance, 2, row) == 2
        assert trees.apply_til_start(trees.viewing_distance, 3, row) == 3
        assert trees.apply_til_start(trees.viewing_distance, 4, row) == 1

    def test_score_to_start_counts_trees_visible_to_end_of_sequence(self):
        row = [3, 3, 2, 1, 2]

        assert trees.apply_til_end(trees.viewing_distance, 0, row) == 1
        assert trees.apply_til_end(trees.viewing_distance, 1, row) == 3
        assert trees.apply_til_end(trees.viewing_distance, 2, row) == 2
        assert trees.apply_til_end(trees.viewing_distance, 3, row) == 1
        assert trees.apply_til_end(trees.viewing_distance, 4, row) == 0

    def test_scenic_score_calculated_correctly(self):
        grid = trees.load_grid(io.StringIO(test_data))
        row = grid[3]
        col = [r[2] for r in grid]

        assert trees.scenic_score(2, 3, row, col) == 8


def test_part2_solution():
    assert trees.part2(io.StringIO(test_data)) == 8
