#!/usr/bin/env python3
from gendiff.cli import parser_args
from gendiff import generate_diff


def main():
    args = parser_args()
    diff = generate_diff(
        args.file_path1,
        args.file_path2,
        args.format
    )
    print(diff)


if __name__ == "__main__":
    main()
