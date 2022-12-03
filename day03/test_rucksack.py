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
