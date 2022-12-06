import tuning


class TestFirstMarker:
    def test_marker_position_returns_4_when_all_leading_characters_differ(self):
        assert tuning.marker_position("abcd") == 4

    def test_marker_position_with_part1_sample_data(self):
        assert tuning.marker_position("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5
        assert tuning.marker_position("nppdvjthqldpwncqszvftbrmjlhg") == 6
        assert tuning.marker_position("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10
        assert tuning.marker_position("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11
