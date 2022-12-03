from typing import List


def read_lines_from_file(path: str, blank_lines: bool = False) -> List[str]:
    """" Reads in lines from an input text file.

    Args:
        path (str): path to file
        blank_lines (bool): whether blank lines are allowed. Defaults to False.blank_lines

    Returns:
        List[str]: list of lines
    """
    with open(path) as file:
        lines = file.readlines()
        lines = [line.rstrip() for line in lines]

        if not blank_lines:
            lines = [line for line in lines if line != ""]

    return lines


def read_lines_from_comment(comment: str, blank_lines: bool = False) -> List[str]:
    """" Splits a multiline comment into a list of lines.

    Args:
        comment (str): multiline comment
        blank_lines (bool): whether blank lines are allowed. Defaults to False.blank_lines

    Returns:
        List[str]: list of lines
    """

    lines = []

    if comment is not None:
        lines = comment.splitlines()
        lines = [line.strip() for line in lines]

        if not blank_lines:
            lines = [line for line in lines if line != ""]

    return lines
