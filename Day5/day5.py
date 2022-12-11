"""Elfs playing modified Hanoi"""
import re

def order(number_of_crates, origin, destination):
    assert number_of_crates != 0
    while number_of_crates != 0:
        crate = origin.pop()
        destination.append(crate)
        number_of_crates -= 1

def order_9001(number_of_crates, origin, destination):
    assert number_of_crates != 0
    temp_stack = []
    while number_of_crates != 0:
        crate = origin.pop()
        temp_stack[:0] = crate
        number_of_crates -= 1
    destination += temp_stack

with open("Day5/input.txt","r") as crate_puzzle:
    lines = crate_puzzle.readlines()
    stacks = {}
    stacks_index = {"0": 0}
    max_stack = 0
    for line in lines:
        if re.search(r"^(\s*\d)+$",line):
            max_stack = int(re.search(r"^(\s*\d)+\s*(\d+)\s*$",line).group(2))
            for stack in range(1,max_stack+1):
                stacks[str(stack)] = []
                stacks_index[str(stack)] = []
            break
    assert max_stack != 0
    for line in lines:
        if re.search(r"\[\w\]",line):
            for stack in range(1,max_stack+1):
                if 1+4*(stack-1)<len(line) and line[1+4*(stack-1)] != " ":
                    stacks[str(stack)][:0] = line[1+4*(stack-1)]
        elif re.search(r"move",line):
            order_match = re.search(r"move\s(\w+)\sfrom\s(\w+)\sto\s(\w+)",line)
            number_of_crates = int(order_match.group(1))
            origin = order_match.group(2)
            destination = order_match.group(3)
            order_9001(number_of_crates, stacks[origin], stacks[destination])
            for stack in stacks:
                print(f"{stack}: {stacks[stack]}")
            print("-----------------------")
    result_string = ''
    for stack in stacks:
        print(f"{stack}: {stacks[stack]}")
        result_string += stacks[stack][-1]
    print(result_string)



