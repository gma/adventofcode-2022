# Advent of Code 2022

These are my solutions to [2022's Advent of Code], which I'm working on in Python, with a spot of [TDD].

There are two problems to solve each day, from 1 December up to (and including) Christmas day.

If you'd like to play around with my solutions and run the tests, you can checkout the code and then create a virtual environment like this:

    python -m venv venv
    source venv/bin/activate         # activates the virtual environment
    pip install -r requirements.txt  # install testing tools in environment

Now you can run the tests for all my solutions with:

    pytest

To run one of the solutions, change to the relevant directory and then run the code:

    cd day01
    pytest
    python calories.py

## The exercises

- [Day 1: Calory Counting](./day01)
- [Day 2: Rock Paper Scissors](./day02)
- [Day 3: Rucksack Reorganization](./day03)
- [Day 4: Camp Cleanup](./day04)
- [Day 5: Supply Stacks](./day05)
- [Day 6: Tuning Trouble](./day06)
- [Day 7: No Space Lef On Device](./day07)
- [Day 8: Treetop Tree House](./day08)
- [Day 9: Rope Bridge](./day09)
- [Day 10: Cathode-Ray Tube](./day10)

[2022's Advent of Code]: https://adventofcode.com/2022
[TDD]: https://www.agilealliance.org/glossary/tdd/
