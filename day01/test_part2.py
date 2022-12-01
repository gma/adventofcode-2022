import part2


def test_find_top_calories_from_several_elves():
    assert [3, 2] == part2.greatest_calories("2\n\n1\n2\n\n1\n", num=2)
