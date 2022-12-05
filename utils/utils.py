from pathlib import Path
from typing import List


def read_lines_from_file(path: str, blank_lines: bool = False, strip: bool = True) -> List[str]:
    """" Reads in lines from an input text file.

    Args:
        path (str): path to file
        blank_lines (bool): whether blank lines are allowed. Defaults to False.
        strip (bool): whether to remove whitespaces and tabs. Defaults to True.

    Returns:
        List[str]: list of lines
    """
    root = Path(__file__).parent.parent
    path = root.joinpath(path)

    with open(path) as file:
        lines = file.readlines()

        if strip:
            lines = [line.rstrip() for line in lines]

        if not blank_lines:
            lines = [line for line in lines if line != ""]

    return lines


def read_lines_from_comment(comment: str, blank_lines: bool = False, strip: bool = True) -> List[str]:
    """" Splits a multiline comment into a list of lines.

    Args:
        comment (str): multiline comment
        blank_lines (bool): whether blank lines are allowed. Defaults to False.
        strip (bool): whether to remove whitespaces and tabs. Defaults to True.

    Returns:
        List[str]: list of lines
    """

    lines = []

    if comment is not None:
        lines = comment.splitlines()

        if strip:
            lines = [line.strip() for line in lines]

        if not blank_lines:
            lines = [line for line in lines if line != ""]

    return lines
