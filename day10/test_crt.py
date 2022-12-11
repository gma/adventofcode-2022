from _pytest.assertion import install_importhook
import crt


class TestCPU:
    def test_reports_value_of_register_at_given_cycle_count(self):
        cpu = crt.CPU()

        with open("test_input") as instructions:
            registers = list(cpu.execute(instructions))

        cycles = (20, 60, 100, 140, 180, 220)
        values = (21, 19, 18, 21, 16, 18)

        for cycle, expected in zip(cycles, values):
            assert registers[cycle - 1] == expected


def test_part1_solution():
    with open("test_input") as instructions:
        assert crt.part1(instructions) == 13140
