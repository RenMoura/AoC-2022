"""Playing with thief monkeys"""
import re

class Monkey():
    def __init__(self, items, operation, test_number) -> None:
        self.items = items
        self.operation = operation
        self.test_number = test_number
        self.worry_diminish = 3
        self.group_lcm = 1
        self.inspection_times = 0

    def throw_item(self, monkey_true, monkey_false):
        while len(self.items) != 0:
            item = int(self.items.pop(0))
            if self.group_lcm != 1:
                item = item % self.group_lcm
            item = self.operation(item)
            #print(f"Operation result: {item}")
            item = int(item) // self.worry_diminish
            #print(f"Diminishing result: {item}")
            #print(f"Divisible by {self.test_number}: {item % self.test_number == 0}")
            if item % self.test_number == 0:
                monkey_true.items.append(item)
            else:
                monkey_false.items.append(item)
            self.inspection_times += 1

    def get_inspection_time(self):
        return self.inspection_times

    def update_worry_factor(self, new_worry_factor):
        self.worry_diminish = new_worry_factor

    def update_lcm_factor(self, new_lcm):
        self.group_lcm = new_lcm

with open("Day11/input.txt","r") as monkey_setup:
    all_monkeys = {}
    monkeys_true = {}
    monkeys_false = {}
    part_two_flag = True
    lcm = 1
    for line in monkey_setup:
        if re.search(r"^Monkey\s(\d+)",line):
            cur_monkey = re.search(r"^Monkey\s(\d+)",line).group(1)
        elif re.search(r"Starting\sitems:\s*(.+)",line):
            items_s = re.search(r"Starting\sitems:\s*(.+)",line).group(1)
            items_s = re.sub(r"\s","",items_s)
            items = items_s.split(",")
        elif re.search(r"Operation:\s*(.+)",line):
            operation_s = re.search(r"Operation:\s*((new)\s*=\s*(.+))",line).group(3)
            operation = eval('lambda old: ' + operation_s)
        elif re.search(r"Test:\s*(.+)(\d+)",line):
            test_number = re.search(r"(\d+)",line).group(1)
            # Got single Monkey all information for instaciating
            all_monkeys[cur_monkey] = Monkey(items, operation, int(test_number))
            if part_two_flag:
                lcm = lcm * int(test_number)
                all_monkeys[cur_monkey].update_worry_factor(1)
        elif re.search(r"If true:\s*(.+)(\d+)",line):
            monkey_true = re.search(r"If true:\s*(.+)(\d+)",line).group(2)
            monkeys_true[cur_monkey] = monkey_true
        elif re.search(r"If false:\s*(.+)(\d+)",line):
            monkey_false = re.search(r"If false:\s*(.+)(\d+)",line).group(2)
            monkeys_false[cur_monkey] = monkey_false
    
    if part_two_flag:
        for monkey in sorted(all_monkeys.keys()):
            all_monkeys[monkey].update_lcm_factor(lcm)

    nb_of_rounds = 20
    if part_two_flag:
        nb_of_rounds = 10000
        
    for round in range(nb_of_rounds):
        #print(f"------------> Round {round} <-------------")
        for monkey in sorted(all_monkeys.keys()):
            #print (f"Monkey {monkey} have following items:",all_monkeys[monkey].items)
            all_monkeys[monkey].throw_item(all_monkeys[monkeys_true[monkey]],all_monkeys[monkeys_false[monkey]])
            inspected_times = all_monkeys[monkey].get_inspection_time()
            print (f"Monkey {monkey} has inspected items {inspected_times} times")
        #print("-----------------------")

    inspect_list = []
    for monkey in sorted(all_monkeys.keys()):
        inspected_times = all_monkeys[monkey].get_inspection_time()
        print (f"Monkey {monkey} has inspected items {inspected_times} times")
        inspect_list.append(inspected_times)
    
    monkey_first = max(inspect_list)
    inspect_list.remove(monkey_first)
    monkey_second = max(inspect_list)
    print(f"Monkey business is {monkey_first}*{monkey_second}={monkey_first*monkey_second}")


        



