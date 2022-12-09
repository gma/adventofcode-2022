import io

import rope


class TestKnot:
    def test_can_be_moved_in_each_direction(self):
        knot = rope.Knot("H", 0, 0)

        knot.go("L")
        assert knot.coords == (-1, 0)

        knot.go("U")
        assert knot.coords == (-1, 1)

    def test_follower_doesnt_move_while_knot_is_one_step_away(self):
        head = rope.Knot("H", 0, 0)
        tail = rope.Knot("H", 0, 0)
        tail.follow(head)

        # head makes a circle around tail
        head.go("L")
        head.go("U")
        head.go("R")
        head.go("R")
        head.go("D")
        head.go("D")
        head.go("L")
        head.go("L")
        head.go("U")

        assert len(set(tail.track)) == 1

    def test_follower_moves_up_when_knot_moves_more_than_one_step_away(self):
        head = rope.Knot("H", 0, 0)
        tail = rope.Knot("T", 0, 0)
        tail.follow(head)

        head.go("U")
        head.go("U")

        assert tail.coords == (0, 1)

    def test_follower_moves_right_when_knot_moves_more_than_one_step_away(self):
        head = rope.Knot("H", 0, 0)
        tail = rope.Knot("T", 0, 0)
        tail.follow(head)

        head.go("R")
        head.go("R")

        assert tail.coords == (1, 0)

    def test_follower_as_diagonally_adjacent_knot_moves_away_vertically(self):
        head = rope.Knot("H", 1, 1)
        tail = rope.Knot("T", 0, 0)
        tail.follow(head)

        head.go("U")

        assert tail.coords == (1, 1)

    def test_follower_as_diagonally_adjacent_knot_moves_away_horizontally(self):
        head = rope.Knot("H", 1, 1)
        tail = rope.Knot("T", 0, 0)
        tail.follow(head)

        head.go("R")

        assert tail.coords == (1, 1)

    def test_follower_as_directly_adjacent_knot_moves_away_diagonally(self):
        head = rope.Knot("H", -2, 2)
        one = rope.Knot("1", 0, 1)
        one.follow(head)
        tail = rope.Knot("T", 0, 0)
        tail.follow(one)

        head.go("L")

        assert tail.coords == (-1, 1)

    def test_follower_tracks_its_route(self):
        head = rope.Knot("H", 0, 0)
        tail = rope.Knot("T", 0, 0)
        tail.follow(head)

        head.go("R")
        head.go("R")

        assert (1, 0) in set(tail.track)


def test_part1_solution():
    test_data = """\
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""

    assert rope.part1(io.StringIO(test_data)) == 13


def test_part2_solution():
    test_data = """\
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
"""

    assert rope.part2(io.StringIO(test_data)) == 36
