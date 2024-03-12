#!/usr/bin/env python3
import argparse


def parser_args(file_path1=None, file_path2=None):
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.',
        add_help=True,
        prog='gendiff'
    )
    parser.add_argument(file_path1)
    parser.add_argument(file_path2)
    parser.add_argument('-f', '--format', help='set format of output')
    arg = parser.parse_args()
    print(arg)
