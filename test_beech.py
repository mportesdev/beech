# coding: utf-8

from pathlib import Path

import pytest

from beech import tree, _tree_data, _lines_from_indent, _print_tree

TEST_DIR = './sample_dir'
DEFAULT_LINES = ['   ', ' │ ', ' └─', ' ├─']


def test_tree(capsys):
    expected = ('sample_dir\n'
                ' ├─library\n'
                ' │  ├─dist\n'
                ' │  ├─src\n'
                ' │  │  ├─core\n'
                ' │  │  └─utils\n'
                ' │  └─tests\n'
                ' └─web\n'
                '    ├─app\n'
                '    │  ├─templates\n'
                '    │  └─views\n'
                '    └─static\n'
                '       └─img\n')

    tree(TEST_DIR)
    std_out = capsys.readouterr().out

    assert std_out == expected


PARAMS = (
    {
        'path': Path(TEST_DIR),
        'dict': {
            'library': {'dist': {},
                        'src': {'core': {}, 'utils': {}},
                        'tests': {}},
            'web': {'app': {'templates': {}, 'views': {}},
                    'static': {'img': {}}}
        },
        'output': ('library\n'
                   ' ├─dist\n'
                   ' ├─src\n'
                   ' │  ├─core\n'
                   ' │  └─utils\n'
                   ' └─tests\n'
                   'web\n'
                   ' ├─app\n'
                   ' │  ├─templates\n'
                   ' │  └─views\n'
                   ' └─static\n'
                   '    └─img\n'),
        'output_spaced': ('library\n'
                          ' ├─ dist\n'
                          ' ├─ src\n'
                          ' │  ├─ core\n'
                          ' │  └─ utils\n'
                          ' └─ tests\n'
                          'web\n'
                          ' ├─ app\n'
                          ' │  ├─ templates\n'
                          ' │  └─ views\n'
                          ' └─ static\n'
                          '    └─ img\n'),
    },
    {
        'path': Path(TEST_DIR) / 'web',
        'dict': {'app': {'templates': {}, 'views': {}}, 'static': {'img': {}}},
        'output': ('app\n'
                   ' ├─templates\n'
                   ' └─views\n'
                   'static\n'
                   ' └─img\n'),
        'output_spaced': ('app\n'
                          ' ├─ templates\n'
                          ' └─ views\n'
                          'static\n'
                          ' └─ img\n'),
    },
    {
        'path': Path(TEST_DIR) / 'web' / 'static',
        'dict': {'img': {}},
        'output': 'img\n',
    },
    {
        'path': Path(TEST_DIR) / 'web' / 'static' / 'img',
        'dict': {},
        'output': '',
    },
)


@pytest.mark.parametrize(
    'path, expected',
    [(param['path'], param['dict']) for param in PARAMS]
)
def test_tree_data(path, expected):
    assert _tree_data(path) == expected


@pytest.mark.parametrize(
    'indent, thick, expected',
    (
        (3, False, DEFAULT_LINES),
        (6, False, ['      ', '   │  ', '   └──', '   ├──']),
        (1, True, [' ', '┃', '┗', '┣']),
        (6, True, ['      ', '   ┃  ', '   ┗━━', '   ┣━━']),
    )
)
def test_lines_from_indent(indent, thick, expected):
    assert _lines_from_indent(indent, thick) == expected


@pytest.mark.parametrize(
    'data, expected',
    [(param['dict'], param['output']) for param in PARAMS]
)
def test_print_tree(capsys, data, expected):
    _print_tree(data, DEFAULT_LINES)
    std_out = capsys.readouterr().out

    assert std_out == expected


@pytest.mark.parametrize(
    'data, expected',
    [(param['dict'], param.get('output_spaced', param['output']))
     for param in PARAMS]
)
def test_print_tree_with_space(capsys, data, expected):
    _print_tree(data, lines=DEFAULT_LINES, add_space=True)
    std_out = capsys.readouterr().out

    assert std_out == expected
