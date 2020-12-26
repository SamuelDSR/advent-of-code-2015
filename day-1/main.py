#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from collections import Counter


def load_input():
    input_path = Path(__file__).parent / "input.txt"
    with input_path.open("r") as f:
        input = f.read()
    return list(input.strip())


def part_one(input):
    counter = Counter(input)
    answer = counter["("] - counter[")"]
    print("Answer to part one: {}".format(answer))
    return answer


def part_two(input):
    floor = 0
    for i, c in enumerate(input):
        if c == "(":
            floor += 1
        else:
            floor -= 1
        if floor == -1:
            break
    answer = i + 1
    print("Answer to part two: {}".format(answer))
    return answer


if __name__ == '__main__':
    input = load_input()
    part_one(input)
    assert part_two(list("(((())())))()")) == 11
    assert part_two(list("()())")) == 5
    part_two(input)
