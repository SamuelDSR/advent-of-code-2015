#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
import re


def load_input():
    input_path = Path(__file__).parent / "input.txt"
    with input_path.open("r") as f:
        lines = f.readlines()
    pat = re.compile(
        r'(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)')
    return [pat.findall(ln)[0] for ln in lines]


def part_one(input, grid_width, grid_height):
    grids = [[False] * grid_width for i in range(grid_height)]

    def _traverse(lx, ly, rx, ry):
        x = lx
        while x <= rx:
            y = ly
            while y <= ry:
                yield x, y
                y += 1
            x += 1

    for action, lx, ly, rx, ry in input:
        lx, ly, rx, ry = int(lx), int(ly), int(rx), int(ry)
        if action == "turn on":
            for i, j in _traverse(lx, ly, rx, ry):
                grids[i][j] = True
        elif action == "turn off":
            for i, j in _traverse(lx, ly, rx, ry):
                grids[i][j] = False
        elif action == "toggle":
            for i, j in _traverse(lx, ly, rx, ry):
                grids[i][j] = not grids[i][j]
        else:
            raise Exception("Unknown action")

    turn_on = 0
    for i, j in _traverse(0, 0, grid_width - 1, grid_height - 1):
        if grids[i][j]:
            turn_on += 1
    print("Answer to part one: {}".format(turn_on))


def part_two(input, grid_width, grid_height):
    grids = [[0] * grid_width for i in range(grid_height)]

    def _traverse(lx, ly, rx, ry):
        x = lx
        while x <= rx:
            y = ly
            while y <= ry:
                yield x, y
                y += 1
            x += 1

    for action, lx, ly, rx, ry in input:
        lx, ly, rx, ry = int(lx), int(ly), int(rx), int(ry)
        if action == "turn on":
            for i, j in _traverse(lx, ly, rx, ry):
                grids[i][j] += 1
        elif action == "turn off":
            for i, j in _traverse(lx, ly, rx, ry):
                grids[i][j] = max(0, grids[i][j] - 1)
        elif action == "toggle":
            for i, j in _traverse(lx, ly, rx, ry):
                grids[i][j] += 2
        else:
            raise Exception("Unknown action")

    brightness = 0
    for i, j in _traverse(0, 0, grid_width - 1, grid_height - 1):
        brightness += grids[i][j]
    print("Answer to part two: {}".format(brightness))


if __name__ == '__main__':
    input = load_input()
    part_one(input, 1000, 1000)
    part_two(input, 1000, 1000)
