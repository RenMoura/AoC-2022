"""Disk space checking"""
import re

class Directory:
    def __init__(self, directory_name):
        self.contents = {}
        self.directory_name = directory_name

    def add_file(self, filename, size):
        self.contents[filename] = size

    def add_directory(self, sub_dir):
        self.contents[sub_dir.directory_name] = sub_dir

    def get_dir_size(self):
        total = 0
        for object in self.contents:
            if type(self.contents[object]) == Directory:
                total += self.contents[object].get_dir_size()
            else:
                total += self.contents[object]
        return total

with open("Day7/input.txt","r") as command_line_history:
    cur_dir = 'home'
    directory_tree = { cur_dir: Directory('home')}
    for line in command_line_history:
        if line[0] == "$":
            if re.search(r"\$\scd\s(\w+)",line):
                #directory_tree[cur_dir].add_directory(cur_dir + "/" + re.search(r"\$\scd\s(.+)",line).group(1))
                cur_dir = cur_dir + "/" + re.search(r"\$\scd\s(.+)",line).group(1)
                #directory_tree[cur_dir] = Directory(cur_dir)
            elif re.search(r"\$\scd\s(\.\.)",line):
                cur_dir = re.sub(r"(.+)\/\w+$",r"\1",cur_dir)
        elif re.search(r"(\d+)\s(.+)",line):
            match_file = re.search(r"(\d+)\s(.+)",line)
            directory_tree[cur_dir].add_file(match_file.group(2),int(match_file.group(1)))
        elif re.search(r"dir\s(.+)",line):
            directory_tree[cur_dir + "/" + re.search(r"dir\s(.+)",line).group(1)] = Directory(cur_dir + "/" + re.search(r"dir\s(.+)",line).group(1))
            directory_tree[cur_dir].add_directory(directory_tree[cur_dir + "/" + re.search(r"dir\s(.+)",line).group(1)])
    size_sum = 0
    total_space = 70000000
    need_space = 30000000
    free_space = total_space - directory_tree['home'].get_dir_size()
    minimum_folder_size = total_space

    for directory in directory_tree:
        dir_size = directory_tree[directory].get_dir_size()
        print(f"directory {directory} = {dir_size}")
        if dir_size <= 100000:
            size_sum += dir_size
        if free_space+dir_size > need_space:
            minimum_folder_size = min(dir_size,minimum_folder_size)    
    
    print(size_sum)
    print(minimum_folder_size)
