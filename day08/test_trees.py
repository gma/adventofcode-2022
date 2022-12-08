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


@pytest.mark.skip
def test_part1_solution():
    assert trees.part1(io.StringIO(test_data)) == 21
