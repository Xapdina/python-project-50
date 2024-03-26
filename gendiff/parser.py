import json
import yaml


def file_parser(file_path, extension):
    if extension == '.json':
        return json.load(file_path)
    if extension == '.yaml' or extension == '.yml':
        return yaml.safe_load(file_path)
    raise ValueError(
        'This extension is unsupported.'
        '\nPlease change extension to json or yaml'
    )
