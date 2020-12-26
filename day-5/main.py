#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path
from collections import Counter


def load_input():
    input_path = Path(__file__).parent / "input.txt"
    with input_path.open("r") as f:
        lines = f.readlines()
    return [ln.strip() for ln in lines]


def part_one(strings):
    def _nice_strings(string):
        vowels = 0
        forbiden = set(["ab", "cd", "pq", "xy"])
        has_doublons = False
        for c1, c2 in zip(string[:-1], string[1:]):
            if c1 in set(["a", "e", "i", "o", "u"]):
                vowels += 1
            if c1 + c2 in forbiden:
                return False
            if c1 == c2:
                has_doublons = True
        if string[-1] in set(["a", "e", "i", "o", "u"]):
            vowels += 1
        return vowels >= 3 and has_doublons

    assert _nice_strings("aaa") == True
    assert _nice_strings("ugknbfddgicrmopn") == True
    assert _nice_strings("jchzalrnumimnmhp") == False
    assert _nice_strings("dvszwmarrgswjxmb") == False
    assert _nice_strings("haegwjzuvuyypxyu") == False
    answer = sum(_nice_strings(s) for s in strings)
    print("Answer to part one: {}".format(answer))


def part_two(strings):
    def _nice_strings(string):
        valid = False
        for i in range(len(string) - 1):
            doublons = string[i] + string[i + 1]
            if doublons in string[i + 2:] or doublons in string[:i]:
                valid = True
                break
        if not valid:
            return False

        valid = False
        for i in range(len(string) - 2):
            if string[i] == string[i + 2]:
                valid = True
                break
        if not valid:
            return False
        return True

    assert _nice_strings("qjhvhtzxzqqjkmpb") == True
    assert _nice_strings("xxyxx") == True
    assert _nice_strings("uurcxstgmygtbstg") == False
    assert _nice_strings("ieodomkazucvgmuy") == False
    answer = sum(_nice_strings(s) for s in strings)
    print("Answer to part two: {}".format(answer))


if __name__ == '__main__':
    input = load_input()
    part_one(input)
    part_two(input)
