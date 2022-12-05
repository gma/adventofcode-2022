import io

import pytest

import supplies


test_data = """\
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""


class TestLoadStacks:
    def test_read_stack_lines_returns_lines_defining_stack(self):
        file = io.StringIO(test_data)
        lines = supplies.read_stack_lines(file)

        assert lines[0] == " 1   2   3 "
        assert lines[-1] == "    [D]    "
        assert len(lines) == 4

    def test_parse_crates_returns_crates_for_single_stack(self):
        assert supplies.parse_crates("[A]") == ("A",)

    def test_parse_crates_returns_multiple_crates(self):
        assert supplies.parse_crates("[A] [B]") == ("A", "B")

    def test_parse_crates_handles_lines_with_missing_crates(self):
        letters = supplies.parse_crates("[A]     [B]    ")

        assert letters == ("A", None, "B", None)

    def test_load_crates_builds_stacks_from_multiple_columns(self):
        file = io.StringIO(test_data)
        stack1, stack2, stack3 = supplies.load_stacks(file)

        assert stack1 == ["Z", "N"]
        assert stack2 == ["M", "C", "D"]
        assert stack3 == ["P"]
