import io

import cleanup


test_data = """
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
""".strip()


class TestPart1:
    def test_sections_as_tuple_converts_string_to_range(self):
        assert cleanup.sections_as_tuple("1-2") == (1, 2)

    def test_contained_by_detects_fully_overlapping_ranges(self):
        large = (1, 4)
        small = (2, 4)

        assert cleanup.contained_by(small, container=large)
        assert not cleanup.contained_by(large, container=small)

    def test_part1_solution(self):
        assert cleanup.part1(io.StringIO(test_data)) == 2


class TestPart2:
    def test_overlap_knows_if_two_ranges_overlap(self):
        # partially overlapping
        assert cleanup.overlap((1, 2), (2, 3)) == True
        assert cleanup.overlap((2, 3), (1, 2)) == True

        # not overlapping
        assert cleanup.overlap((1, 2), (3, 4)) == False
        assert cleanup.overlap((3, 4), (1, 2)) == False

        # fully contained
        assert cleanup.overlap((1, 6), (2, 3)) == True

        # ranges of length 1
        assert cleanup.overlap((1, 1), (1, 2)) == True
        assert cleanup.overlap((1, 2), (2, 2)) == True

    def test_part2_solution(self):
        assert cleanup.part2(io.StringIO(test_data)) == 4
