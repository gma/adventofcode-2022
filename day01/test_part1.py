import part1


def test_sum_up_calories_with_no_elves():
    totals = part1.sum_calories("")

    assert totals == []


def test_sum_up_calories_for_each_elf():
    totals = part1.sum_calories("1\n2\n\n3\n\n1\n2\n2\n")

    assert totals == [3, 3, 5]
