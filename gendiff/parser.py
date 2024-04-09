import json
import yaml
from gendiff.const import DATA_FORMATS


def parse_data(data, data_format):
    match data_format:
        case DATA_FORMATS.JSON:
            return json.loads(data)
        case DATA_FORMATS.YAML:
            return yaml.safe_load(data)

    ValueError(f'Unsupported extension: {data_format}. '
               f'Supported [{", ".join(DATA_FORMATS)}]')
