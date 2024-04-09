from gendiff.formatters.json import to_json
from gendiff.formatters.plain import to_plain
from gendiff.formatters.stylish import render_stylish
from gendiff.const import STYLE_FORMATS


def format_diff(diff, formatter):
    match formatter:
        case STYLE_FORMATS.STYLISH:
            return render_stylish(diff)
        case STYLE_FORMATS.PLAIN:
            return to_plain(diff)
        case STYLE_FORMATS.JSON:
            return to_json(diff)

    raise ValueError(f'Unsupported formatter: {formatter}')
