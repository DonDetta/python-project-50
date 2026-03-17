def format_value(value, depth):
    if isinstance(value, dict):
        indent = '    ' * depth
        closing = '    ' * (depth - 1)
        lines = ['{']
        for k, v in value.items():
            lines.append(f'{indent}{k}: {format_value(v, depth + 1)}')
        lines.append(f'{closing}}}')
        return '\n'.join(lines)
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return str(value)


def render_node(node, depth):
    indent = '    ' * (depth - 1)
    sign_indent = indent + '  '
    key = node['key']

    if node['type'] == 'nested':
        children = '\n'.join(
            render_node(child, depth + 1) for child in node['children']
        )
        return f'{indent}    {key}: {{\n{children}\n{indent}    }}'

    if node['type'] == 'unchanged':
        return f'{indent}    {key}: {format_value(node["value"], depth + 1)}'

    if node['type'] == 'added':
        return f'{sign_indent}+ {key}: {format_value(node["value"], depth + 1)}'

    if node['type'] == 'removed':
        return f'{sign_indent}- {key}: {format_value(node["value"], depth + 1)}'

    if node['type'] == 'changed':
        old = (
            f'{sign_indent}- {key}: '
            f'{format_value(node["old_value"], depth + 1)}'
        )
        new = (
            f'{sign_indent}+ {key}: '
            f'{format_value(node["new_value"], depth + 1)}'
        )
        return f'{old}\n{new}'


def stylish(diff):
    lines = '\n'.join(render_node(node, 1) for node in diff)
    return '{\n' + lines + '\n}'
