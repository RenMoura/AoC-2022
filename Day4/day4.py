"""Space cleaning assignment"""

class ElfAssign():
    def __init__(self, min, max) -> None:
        self.min = min
        self.max = max
        assert self.min <= self.max

    def is_contained_in(self, other_elf):
        if self.min >= other_elf.min and self.max <= other_elf.max:
            return True
        else:
            return False

    def is_overlapping(self, other_elf):
        if self.max < other_elf.min or self.min > other_elf.max:
            return False
        else:
            return True

def parse_assignment(line):
    parsed_list = line.split(",")
    parsed_assigns = []
    for elf in parsed_list:
        parsed_elf = elf.split("-")
        parsed_assigns.append(ElfAssign(int(parsed_elf[0]),int(parsed_elf[1])))
    assert len(parsed_assigns) == 2
    return parsed_assigns


with open("Day4/input.txt","r") as assignments:
    contained_number = 0
    overlap_number = 0
    for assignment in assignments:
        [elf_1_task, elf_2_task] = parse_assignment(assignment)
        if elf_1_task.is_contained_in(elf_2_task) or elf_2_task.is_contained_in(elf_1_task):
            contained_number += 1
        if elf_1_task.is_overlapping(elf_2_task):
            overlap_number += 1

print(contained_number)
print(overlap_number)