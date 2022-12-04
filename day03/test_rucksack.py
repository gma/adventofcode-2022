import io

import rucksack


class TestPart1:
    def test_common_item_identifies_duplicate_character(self):
        assert rucksack.common_item("abc", "cde") == "c"

    def test_item_priority_of_letters_in_alphabet(self):
        assert rucksack.item_priority("a") == 1
        assert rucksack.item_priority("z") == 26
        assert rucksack.item_priority("A") == 27
        assert rucksack.item_priority("Z") == 52

    def test_compartment_contents_returns_contents_of_both_compartments(self):
        assert rucksack.compartment_contents("abcd") == ("ab", "cd")

    def test_part1_solution(self):
        test_data = """
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
        """.strip()

        assert rucksack.part1(io.StringIO(test_data)) == 157


class TestPart2:
    def test_group_iterates_over_lines_three_lines_at_a_time(self):
        groups = rucksack.groups(io.StringIO("1\n2\n3\n4\n5\n6\n"))

        assert next(groups) == ("1", "2", "3")
        assert next(groups) == ("4", "5", "6")

    def test_common_item_supports_multiple_sets(self):
        assert rucksack.common_item("abc", "cde", "cfg") == "c"

    def test_part2_solution(self):
        test_data = """
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
        """.strip()

        assert rucksack.part2(io.StringIO(test_data)) == 70
