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
    cur_dir = ''
    parent_directory = Directory('/')
    for line in command_line_history:
        if line[0] == "$":
            if re.search(r"\$\scd\s(.+)",line):
                cur_dir = cur_dir + "/" + re.search(r"\$\scd\s(.+)",line).group(1)
        elif re.search(r"(\d+)\s(\w+\.\w+)",line):





