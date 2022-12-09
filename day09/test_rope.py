import io

import rope


class TestRopeEnd:
    def test_can_be_moved_in_each_direction(self):
        end = rope.End(0, 0)

        end.go("L")
        assert end.x == -1 and end.y == 0

        end.go("U")
        assert end.x == -1 and end.y == 1

    def test_follower_doesnt_move_while_end_is_one_step_away(self):
        head = rope.End(0, 0)
        tail = rope.End(0, 0)
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

    def test_follower_moves_up_when_end_moves_more_than_one_step_away(self):
        head = rope.End(0, 0)
        tail = rope.End(0, 0)
        tail.follow(head)

        head.go("U")
        head.go("U")

        assert tail.x == 0 and tail.y == 1

    def test_follower_moves_right_when_end_moves_more_than_one_step_away(self):
        head = rope.End(0, 0)
        tail = rope.End(0, 0)
        tail.follow(head)

        head.go("R")
        head.go("R")

        assert tail.x == 1 and tail.y == 0

    def test_follower_as_diagonally_adjacent_end_moves_away_vertically(self):
        head = rope.End(1, 1)
        tail = rope.End(0, 0)
        tail.follow(head)

        head.go("U")

        assert tail.x == 1 and tail.y == 1

    def test_follower_as_diagonally_adjacent_end_moves_away_horizontally(self):
        head = rope.End(1, 1)
        tail = rope.End(0, 0)
        tail.follow(head)

        head.go("R")

        assert tail.x == 1 and tail.y == 1

    def test_follower_tracks_its_route(self):
        head = rope.End(0, 0)
        tail = rope.End(0, 0)
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
