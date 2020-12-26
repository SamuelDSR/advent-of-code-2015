#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
from pathlib import Path


def load_input():
    input_path = Path(__file__).parent / "input.txt"
    with input_path.open("r") as f:
        lines = f.readlines()
    pat = re.compile(
        r'(\w+) (OR|AND|RSHIFT|LSHIFT) (\w+) -> (\w+)|NOT (\w+) -> (\w+)|(\d+|\w+) -> (\w+)'
    )
    instructions = []
    for ln in lines:
        t = pat.findall(ln)[0]
        instructions.append((t[0], t[1], t[2], t[3], t[4], t[5], t[6], t[7]))
    dest_to_ins = {}
    for ins in instructions:
        if ins[3] != "":
            dest_to_ins[ins[3]] = ins
        elif ins[5] != "":
            dest_to_ins[ins[5]] = ins
        elif ins[7] != "":
            dest_to_ins[ins[7]] = ins
        else:
            raise Exception("Unknown instructions: {}".format(ins))
    return dest_to_ins


def try_parse_int(s):
    try:
        int(s)
        return True
    except:
        return False


def part_one(dest_to_ins):
    memory = {}

    def run_gate(wire):
        if try_parse_int(wire):
            return int(wire)
        if wire in memory:
            return memory[wire]
        ins = dest_to_ins[wire]
        if ins[1] == "AND":
            value = run_gate(ins[0]) & run_gate(ins[2])
        elif ins[1] == "OR":
            value = run_gate(ins[0]) | run_gate(ins[2])
        elif ins[1] == 'LSHIFT':
            value = run_gate(ins[0]) << int(ins[2])
        elif ins[1] == 'RSHIFT':
            value = run_gate(ins[0]) >> int(ins[2])
        elif ins[4] != "":
            value = ~run_gate(ins[4])
        elif ins[6] != "":
            value = run_gate(ins[6])
        else:
            raise Exception("Unknown instructions: {}".format(ins))
        memory[wire] = value
        return value

    run_gate("a")
    print("Answer to part one: {}".format(memory["a"]))
    return memory["a"]


def part_two(dest_to_ins, aval):
    dest_to_ins["b"] = ("", "", "", "", "", "", str(aval), "b")
    part_one(dest_to_ins)


if __name__ == '__main__':
    dest_to_ins = load_input()
    aval = part_one(dest_to_ins)
    part_two(dest_to_ins, aval)
