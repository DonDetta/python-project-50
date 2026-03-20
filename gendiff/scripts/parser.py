import json
import yaml


def parse(file_path):
    if file_path.endswith('.json'):
        return json.load(open(file_path))
    if file_path.endswith(('.yml', '.yaml')):
        return yaml.safe_load(open(file_path))
    raise ValueError(f'Unsupported file format: {file_path}')