### Hexlet tests and linter status:

[![Actions Status](https://github.com/Xapdina/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Xapdina/python-project-50/actions)

[![Actions Status](https://github.com/Xapdina/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/Xapdina/python-project-50/actions)

[![Maintainability](https://api.codeclimate.com/v1/badges/555598e4b0ddb481a8b8/maintainability)](https://codeclimate.com/github/Xapdina/python-project-50/maintainability)

[![Test Coverage](https://api.codeclimate.com/v1/badges/555598e4b0ddb481a8b8/test_coverage)](https://codeclimate.com/github/Xapdina/python-project-50/test_coverage)

### Project: Difference Calculator

Difference Calculator is a tool for comparing two files of different formats (e.g., JSON or YAML) and
displaying the differences between them in a convenient format. It allows identifying changes in the data structure,
added or deleted elements, as well as modifications in the values of fields. The project supports various output
formatting styles, such as "stylish," "plain," and "JSON," for presenting the comparison results.

```shell
usage: gendiff [-h] [-f FORMAT] file_path1 file_path2

Compares two configuration files and shows a difference.

positional arguments:
  file_path1
  file_path2

options:
  -h, --help            show this help message and exit
  -f FORMAT, --format FORMAT
                        select format of output from [stylish, plain, json]

```

#### Requirements and Tools:

|   Tools    | Version |
|:----------:|:-------:|
|   python   |  ^3.11  |
|   pyyaml   | ^6.0.1  |
|   pytest   | ^7.4.3  |
|   flake8   | ^6.1.0  |
| pytest-cov | ^4.1.0  |

#### To get started, you need to perform the following operations:

| Step |                                                       Instruction                                                        |
|:----:|:------------------------------------------------------------------------------------------------------------------------:|
|  1   |                    Clone he repository to your PC:<br/>`git@github.com:Xapdina/python-project-50.git`                    |
|  2   |                                       Go to repository<br/>`cd python-project-50`                                        |
|  3   |                                        Installation in your PC<br/>`make install`                                        |
|  4   | Or you use command for install:<br/>`python3 -m pip install --user git+https://github.com/Xapdina/python-project-50.git` |
|  5   |                            And this for uninstall:<br/>`python3 -m pip uninstall hexlet-code`                            |

*P.S.* *You must have [Poetry](https://python-poetry.org) installed*

#### You need that commands
___
Download project
```shell
git clone git@github.com:Xapdina/python-project-50.git
```
or
```shell
python3 -m pip install --user git+https://github.com/Xapdina/python-project-50.git
```
___
Install project
```shell
make install
```
___
Main commands
```shell
gendiff -h
```
```shell
gendiff **filepath1** **filepath2** -f **style**
```
```shell
python3 -m pip uninstall hexlet-code
```
___

### How it's work
https://github.com/Xapdina/TRASH/blob/main/help.gif
#### Help command
[![asciicast](https://github.com/Xapdina/TRASH/blob/main/help.gif)](https://github.com/Xapdina/TRASH/blob/main/help.gif)
##### Diff-default or diff-stylish
[![asciicast](https://github.com/Xapdina/TRASH/blob/main/default.gif)](https://github.com/Xapdina/TRASH/blob/main/default.gif)
##### Diff-plain
[![asciicast](https://github.com/Xapdina/TRASH/blob/main/plain.gif)](https://github.com/Xapdina/TRASH/blob/main/plain.gif)
##### Diff-json
[![asciicast](https://github.com/Xapdina/TRASH/blob/main/json.gif)](https://github.com/Xapdina/TRASH/blob/main/json.gif)
