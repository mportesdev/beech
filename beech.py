# coding: utf-8

from pathlib import Path
from typing import Union

LINES = (
    (' ', ' '),
    ('│', ' '),
    ('└', '─'),
    ('├', '─'),
)

LINES_THICK = (
    (' ', ' '),
    ('┃', ' '),
    ('┗', '━'),
    ('┣', '━')
)


def tree(path: Union[Path, str], indent=3, add_space=False, thick=False,
         show_root=True) -> None:
    path = Path(path)
    data = _tree_data(path)
    if show_root:
        data = {path.name: data}

    lines = _lines_from_indent(indent, thick)
    _print_tree(data, lines, add_space)


def _tree_data(path: Path) -> dict:
    return {
        item.name: _tree_data(item)
        for item in path.iterdir()
        if item.is_dir()
    }


def _lines_from_indent(indent: int, thick: bool) -> list:
    half_indent = (indent + 1) // 2
    lines = [
        _align(char, half_indent, fill_char=fill_char)
        for char, fill_char in (LINES_THICK if thick else LINES)
    ]

    lines = [_align(string, indent, left=False) for string in lines]
    return lines


def _align(string: str, width: int, left=True, fill_char='') -> str:
    side = '<' if left else '>'
    format_spec = f'{fill_char}{side}{width}'
    return f'{string:{format_spec}}'


def _print_tree(data: dict, lines: list, add_space=False, levels=()) -> None:
    dir_names = sorted(data)
    blank, vertical, corner, branch = lines

    for dir_name in dir_names:
        for level in levels[1:]:
            print(blank if level else vertical, end='')

        is_last = dir_name is dir_names[-1]
        if levels:
            print(corner if is_last else branch, end=' ' if add_space else '')

        print(dir_name)
        _print_tree(data[dir_name], lines, add_space, levels=levels + (is_last,))
