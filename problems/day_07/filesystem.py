from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Set


@dataclass
class File:
    name: str
    size: int

    def get_size(self):
        return self.size

    def __hash__(self):
        return hash(self.name)


@dataclass
class Directory:
    name: str
    parent: Directory
    children: Set[Directory | File] = field(default_factory=set)

    def get_size(self):
        return sum((child.get_size() for child in self.children))

    def __hash__(self):
        return hash(self.name)


def first(iterable):
    return next(iter(iterable))


def flatten(dir: Directory) -> List[Directory]:
    directories = [dir]

    for child in dir.children:
        if isinstance(child, Directory):
            directories.extend(flatten(child))
    return directories
