"""Rucksacks common itens counting"""

items = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

with open("Day3/input.txt","r") as rucksacks:
    total_priority = 0
    """
    for sack in rucksacks:
        sack = sack.strip()
        middle_index = int(len(sack)/2)
        sack_1 = sack[0:middle_index]
        sack_2 = sack[middle_index:]
        add_priority = 0
        for item_1 in sack_1:
            for item_2 in sack_2:
                if item_1 == item_2:
                    add_priority = items.index(item_1)+1
                    find_item = item_1
                    break
            if add_priority != 0:
                break

        total_priority = total_priority + add_priority
    """
    total_priority_group = 0
    elf_group = []
    for sack in rucksacks:
        sack = sack.strip()
        elf_group.append(sack)
        if len(elf_group) == 3:
            add_priority = 0
            for item_1 in elf_group[0]:
                for item_2 in elf_group[1]:
                    for item_3 in elf_group[2]:
                        if item_1 == item_2 and item_1 == item_3:
                            add_priority = items.index(item_1)+1
                            break
                    if add_priority != 0:
                        break
                if add_priority != 0:
                    break
            elf_group = []
            total_priority_group = total_priority_group + add_priority



print(total_priority)
print(total_priority_group)

