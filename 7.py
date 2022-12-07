#!/usr/bin/env python
import os
import re

dirname = os.path.dirname(__file__)

data = []
with open(os.path.join(dirname, "data/7.txt"), 'r', encoding='utf-8') as file:
    data = [l.strip() for l in file.readlines()]


class Node(object):
    def __init__(self, name):
        self.name = name
        self.children = []
        self.parent = None

class FileNode(Node):
    def __init__(self, name):
        self.type = "file"
        self.size = 0
        super().__init__(name)

    def set_size(self, size):
        self.size = size
    
    def __str__(self):
        return f'File("{self.name}",{self.size})'

class DirNode(Node):
    def __init__(self, name):
        self.type = "dir"
        self.children = []
        self.size = 0
        super().__init__(name)
    
    def add_child(self, obj):
        self.children.append(obj)

    def __str__(self):
        return f'Directory("{self.name}", {self.size}, {self.children})'




changeDir = re.compile(r"^\$ cd (.*)$")
listDir = re.compile(r"^\$ ls$")
isDir = re.compile(r"^dir (\w+)$")
isFile = re.compile(r"^(\d+) (.+)$")

rootNode = None
currentNode = None

# parse file and build node tree
for line in data:
    if changeDir.match(line):
        m = changeDir.match(line)

        if currentNode is None:
            newDir = DirNode(m.group(1))
            print(newDir)
            currentNode = newDir
            if rootNode is None:
                rootNode = newDir
        else:
            if m.group(1) == '..':
                currentNode = currentNode.parent
            else:
                changeTo = next((x for x in currentNode.children if x.name == m.group(1)), None)
                currentNode = changeTo
                if currentNode == None:
                    print(f"Error, no child named {m.group(0)} in current node")
                    exit(1)
    elif isDir.match(line):
        newDir = DirNode(isDir.match(line).group(1))
        newDir.parent = currentNode
        currentNode.add_child(newDir)
    elif isFile.match(line):
        fileNode = FileNode(isFile.match(line).group(2))
        fileNode.set_size(int(isFile.match(line).group(1)))
        fileNode.parent = currentNode
        currentNode.add_child(fileNode)

    elif listDir.match(line):
        pass
    else:
        print(f"no match for line {line}")
        exit(1)

p1 = []

DISKSIZE = 70000000
FREESPACENEEDED = 30000000

# add up disk sizes
def postOrder(node):
    for child in node.children:
        postOrder(child)
        node.size += child.size
    if node.type == "dir" and node.size <= 100000:
        p1.append(node.size)

postOrder(rootNode)
print(f"Part 1 answer: {sum(p1)}")

print(f"Used Space: {rootNode.size}")
print(f"Unused Space: {DISKSIZE - rootNode.size}")
print(f"Need to free up {FREESPACENEEDED - (DISKSIZE - rootNode.size)}")

needed = FREESPACENEEDED - (DISKSIZE - rootNode.size)
candidates = []

def findSmallestDirs(node):
    for child in node.children:
        findSmallestDirs(child)
    if node.type == "dir" and node.size >= needed:
        candidates.append(node)

findSmallestDirs(rootNode)
candidates.sort(key=lambda x: x.size)
print(f"Part 2 answer: {candidates[0].size}")
