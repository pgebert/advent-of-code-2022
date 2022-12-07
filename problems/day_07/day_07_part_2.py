from __future__ import annotations

from typing import List

from problems.day_07.filesystem import Directory, first, File, flatten

"""

https://adventofcode.com/2022/day/7

--- Part Two ---
Now, you're ready to choose a directory to delete.

The total disk space available to the filesystem is 70000000. To run the update, you need unused space of at least 30000000. You need to find a directory you can delete that will free up enough space to run the update.

In the example above, the total size of the outermost directory (and thus the total amount of used space) is 48381165; this means that the size of the unused space must currently be 21618835, which isn't quite the 30000000 required by the update. Therefore, the update still requires a directory with total size of at least 8381165 to be deleted before it can run.

To achieve this, you have the following options:

Delete directory e, which would increase unused space by 584.
Delete directory a, which would increase unused space by 94853.
Delete directory d, which would increase unused space by 24933642.
Delete directory /, which would increase unused space by 48381165.
Directories e and a are both too small; deleting them would not free up enough space. However, directories d and / are both big enough! Between these, choose the smallest: d, increasing unused space by 24933642.

Find the smallest directory that, if deleted, would free up enough space on the filesystem to run the update. What is the total size of that directory?

"""


def solve(input: List[str]):
    root = Directory("/", None)
    cwd = root

    for line in input:

        if line.startswith("$ cd"):
            name = line.removeprefix("$ cd ")

            if name == "/":
                continue

            cwd = cwd.parent if name == ".." else first(filter(lambda child: child.name == name, cwd.children))

        elif line.startswith("dir"):

            name = line.removeprefix("dir ")

            directory = Directory(name, cwd)
            cwd.children.add(directory)

        elif first(line).isdigit():
            size, name = line.split(" ")

            file = File(name, int(size))
            cwd.children.add(file)

    required_space = max(30000000 - (70000000 - root.get_size()), 0)

    return first(sorted(filter(lambda x: x >= required_space, (x.get_size() for x in flatten(root)))))
