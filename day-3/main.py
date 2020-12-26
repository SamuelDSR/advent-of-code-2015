#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path


def load_input():
    input_path = Path(__file__).parent / "input.txt"
    with input_path.open("r") as f:
        lines = f.read()
    return list(lines.strip())


def part_one(input):
    def _move(i, j, m):
        if m == '>':
            i += 1
        elif m == '<':
            i -= 1
        elif m == '^':
            j += 1
        elif m == 'v':
            j -= 1
        else:
            raise Exception("Unknown move instructions")
        return i, j

    i, j = 0, 0
    visited = set([(i, j)])
    for m in input:
        i, j = _move(i, j, m)
        visited.add((i, j))
    answer = len(visited)
    print("Answer to part one: {}".format(answer))
    return visited 


def part_two(input):
    santa_input, robot_input = input[::2], input[1::2]
    answer = len(part_one(santa_input) | part_one(robot_input))
    print("Answer to part two: {}".format(answer))
    return answer


if __name__ == '__main__':
    input = load_input()
    part_one(input)
    part_two(input)
