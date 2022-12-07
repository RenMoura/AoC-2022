"""Get elf carrying most number of calories"""

current_elf = 0
elfs = []
with open("Day1/input.txt","r") as input_file:
    elfs.append(0)
    for line in input_file:
        line = line.strip("\n")
        if line == '':
            current_elf = current_elf + 1
            elfs.append(0)
        else:
            elfs[current_elf] = elfs[current_elf] + int(line)
    max_elf_1 = max(elfs)
    elfs.remove(max_elf_1)
    max_elf_2 = max(elfs)
    elfs.remove(max_elf_2)
    max_elf_3 = max(elfs)
    elfs.remove(max_elf_3)

    print(max_elf_1+max_elf_2+max_elf_3)



