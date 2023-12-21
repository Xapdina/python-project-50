#!/usr/bin/env python3
import argparse


def parser_args():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.',
        add_help=True,
        prog='gendiff'
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    arg = parser.parse_args()
    print(arg)


if __name__ == '__main__':
    parser_args()
