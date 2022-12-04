import io

import cleanup


class TestPart1:
    def test_sections_as_tuple_converts_string_to_range(self):
        assert cleanup.sections_as_tuple("1-2") == (1, 2)

    def test_contained_by_detects_fully_overlapping_ranges(self):
        large = (1, 4)
        small = (2, 4)

        assert cleanup.contained_by(small, container=large)
        assert not cleanup.contained_by(large, container=small)

    def test_part1_solution(self):
        data = """
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
        """.strip()

        assert cleanup.part1(io.StringIO(data)) == 2
