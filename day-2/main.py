#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path


def load_input():
    input_path = Path(__file__).parent / "input.txt"
    with input_path.open("r") as f:
        input_lines = f.readlines()
    return [[int(n) for n in ln.split("x")] for ln in input_lines]


def part_one(input):
    def _area(dims):
        ds = sorted(dims)
        return 3 * ds[0] * ds[1] + 2 * ds[0] * ds[2] + 2 * ds[1] * ds[2]

    answer = sum(_area(ds) for ds in input)
    print("Answer to part one: {}".format(answer))
    return answer


def part_two(input):
    def _area(dims):
        ds = sorted(dims)
        return ds[0] * ds[1] * ds[2] + 2 * (ds[0] + ds[1])

    answer = sum(_area(ds) for ds in input)
    print("Answer to part two: {}".format(answer))
    return answer


if __name__ == '__main__':
    input = load_input()
    part_one(input)
    part_two(input)
