import calories


def test_sum_up_calories_with_no_elves():
    totals = calories.sum_calories("")

    assert totals == []


def test_sum_up_calories_for_each_elf():
    totals = calories.sum_calories("1\n2\n\n3\n\n1\n2\n2\n")

    assert totals == [3, 3, 5]


def test_find_top_calories_from_several_elves():
    assert [3, 2] == calories.greatest_calories("2\n\n1\n2\n\n1\n", num=2)
