def format_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, str):
        return f"'{value}'"
    return str(value)


def render_diff(diff, path=''):
    lines = []
    for node in diff:
        current_path = f'{path}.{node["key"]}' if path else node['key']

        if node['type'] == 'nested':
            lines.extend(render_diff(node['children'], current_path))
        elif node['type'] == 'added':
            lines.append(
                f"Property '{current_path}' was added with value: "
                f"{format_value(node['value'])}"
            )
        elif node['type'] == 'removed':
            lines.append(f"Property '{current_path}' was removed")
        elif node['type'] == 'changed':
            old = format_value(node['old_value'])
            new = format_value(node['new_value'])
            lines.append(
                f"Property '{current_path}' was updated. From {old} to {new}"
            )
    return lines


def plain(diff):
    return '\n'.join(render_diff(diff))