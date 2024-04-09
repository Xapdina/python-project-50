import argparse
from gendiff.const import STYLE_FORMATS


def parser_args():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.',
        add_help=True,
        prog='gendiff'
    )
    parser.add_argument('file_path1')
    parser.add_argument('file_path2')
    parser.add_argument('-f', '--format',
                        default='stylish',
                        help=f'select format of output from '
                             f'[{", ".join(STYLE_FORMATS)}]')

    return parser.parse_args()
