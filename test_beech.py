# coding: utf-8

from pathlib import Path

import pytest

from beech import tree, _tree_data, _lines_from_indent, _print_tree

TEST_DIR = Path(__file__).parent / 'sample_dir'
DEFAULT_LINES = [
    '   ',
    ' │ ',
    ' └─',
    ' ├─',
]


def test_tree(capsys):
    expected = (
        'sample_dir\n'
        ' ├─.hidden\n'
        ' │  └─.hidden\n'
        ' ├─app\n'
        ' │  ├─app\n'
        ' │  │  └─views\n'
        ' │  └─static\n'
        ' │     └─img\n'
        ' └─library\n'
        '    ├─.pytest_cache\n'
        '    ├─src\n'
        '    │  ├─core\n'
        '    │  └─utils\n'
        '    └─tests\n'
    )
    tree(TEST_DIR)
    std_out = capsys.readouterr().out
    assert std_out == expected


PARAMS = (
    {
        'path': Path(TEST_DIR),
        'dict': {
            '.hidden': {
                '.hidden': {},
            },
            'app': {
                'app': {
                    'views': {},
                },
                'static': {
                    'img': {},
                },
            },
            'library': {
                '.pytest_cache': {},
                'src': {
                    'core': {},
                    'utils': {},
                },
                'tests': {},
            },
        },
        'dict_without_hidden': {
            'app': {
                'app': {
                    'views': {},
                },
                'static': {
                    'img': {},
                },
            },
            'library': {
                'src': {
                    'core': {},
                    'utils': {},
                },
                'tests': {},
            },
        },
        'output': (
            '.hidden\n'
            ' └─.hidden\n'
            'app\n'
            ' ├─app\n'
            ' │  └─views\n'
            ' └─static\n'
            '    └─img\n'
            'library\n'
            ' ├─.pytest_cache\n'
            ' ├─src\n'
            ' │  ├─core\n'
            ' │  └─utils\n'
            ' └─tests\n'
        ),
        'output_spaced': (
            '.hidden\n'
            ' └─ .hidden\n'
            'app\n'
            ' ├─ app\n'
            ' │  └─ views\n'
            ' └─ static\n'
            '    └─ img\n'
            'library\n'
            ' ├─ .pytest_cache\n'
            ' ├─ src\n'
            ' │  ├─ core\n'
            ' │  └─ utils\n'
            ' └─ tests\n'
        ),
    },
    {
        'path': Path(TEST_DIR) / 'app',
        'dict': {
            'app': {
                'views': {},
            },
            'static': {
                'img': {},
            },
        },
        'output': (
            'app\n'
            ' └─views\n'
            'static\n'
            ' └─img\n'
        ),
        'output_spaced': (
            'app\n'
            ' └─ views\n'
            'static\n'
            ' └─ img\n'
        ),
    },
    {
        'path': Path(TEST_DIR) / 'app' / 'static',
        'dict': {
            'img': {},
        },
        'output': 'img\n',
    },
    {
        'path': Path(TEST_DIR) / 'app' / 'static' / 'img',
        'dict': {},
        'output': '',
    },
)


@pytest.mark.parametrize(
    'path, expected',
    [
        (param['path'], param['dict']) for param in PARAMS
    ]
)
def test_tree_data(path, expected):
    assert _tree_data(path) == expected


@pytest.mark.parametrize(
    'path, expected',
    [
        (param['path'], param.get('dict_without_hidden', param['dict']))
        for param in PARAMS
    ]
)
def test_tree_data_skip_hidden(path, expected):
    assert _tree_data(path, skip_hidden=True) == expected


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
    [
        (param['dict'], param['output']) for param in PARAMS
    ]
)
def test_print_tree(capsys, data, expected):
    _print_tree(data, DEFAULT_LINES)
    std_out = capsys.readouterr().out
    assert std_out == expected


@pytest.mark.parametrize(
    'data, expected',
    [
        (param['dict'], param.get('output_spaced', param['output'])) for param in PARAMS
    ]
)
def test_print_tree_with_space(capsys, data, expected):
    _print_tree(data, lines=DEFAULT_LINES, add_space=True)
    std_out = capsys.readouterr().out
    assert std_out == expected
