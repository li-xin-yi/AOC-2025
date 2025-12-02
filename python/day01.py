"""Advent of Code 2025 - Day 01"""

from utils import read_input


def part1(input_data: list[str]) -> int:
    """Solve part 1 of the puzzle."""
    return len(input_data)


def part2(input_data: list[str]) -> int:
    """Solve part 2 of the puzzle."""
    return len(input_data)


def main():
    # Test if implementation meets criteria from the description
    assert part1(["test_input"]) == 1

    # Or read a large test input from the `python/Day01_test.txt` file:
    test_input = read_input("Day01_test")
    assert part1(test_input) == 1

    # Read the input from the `python/Day01.txt` file.
    input_data = read_input("Day01")
    print(part1(input_data))
    print(part2(input_data))


if __name__ == "__main__":
    main()
