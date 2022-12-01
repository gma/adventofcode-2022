import calories


def test_sum_up_calories_with_no_elves():
    assert [] == calories.totals("")


def test_sum_up_calories_for_each_elf():
    assert [3, 3, 5] == calories.totals("1\n2\n\n3\n\n1\n2\n2\n")


def test_find_highest_calory_counts_of_multiple_elves():
    assert [3, 2] == calories.largest_totals("2\n\n1\n2\n\n1\n", num=2)
