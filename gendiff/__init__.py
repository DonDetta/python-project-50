from gendiff.scripts.diff import build_diff
from gendiff.formatters.json import to_json
from gendiff.formatters.plain import plain
from gendiff.formatters.stylish import stylish
from gendiff.scripts.parser import parse

FORMATTERS = {
    'stylish': stylish,
    'plain': plain,
    'json': to_json,
}


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = parse(file_path1)
    data2 = parse(file_path2)
    diff = build_diff(data1, data2)
    formatter = FORMATTERS.get(format_name)
    if not formatter:
        raise ValueError(f'Unknown format: {format_name}')
    return formatter(diff)