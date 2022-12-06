import tuning


class TestPacketMarker:
    def test_find_packet_returns_4_when_packet_starts_immediately(self):
        assert tuning.find_packet("abcd") == 4

    def test_find_packet_with_part1_sample_data(self):
        assert tuning.find_packet("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5
        assert tuning.find_packet("nppdvjthqldpwncqszvftbrmjlhg") == 6
        assert tuning.find_packet("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10
        assert tuning.find_packet("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11


class TestMessageMarker:
    def test_find_message_with_part2_sample_data(self):
        assert tuning.find_message("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 19
        assert tuning.find_message("bvwbjplbgvbhsrlpgdmjqwftvncz") == 23
        assert tuning.find_message("nppdvjthqldpwncqszvftbrmjlhg") == 23
        assert tuning.find_message("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 29
        assert tuning.find_message("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 26
