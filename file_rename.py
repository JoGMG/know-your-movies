import os
from sys import argv
"""
Rename files within `directory` passed as argument
to lowercase and replaces spaces with `-`.
"""


def file_rename(directory: str):
    """
    Rename files within directory passed as argument.

    Arguments:
        - `directory` (str): Path to the directory containing
                             the files to rename.
    """
    for filename in os.listdir(directory):
        old_name = os.path.join(directory, filename)
        new_name = old_name.lower().replace(' ', '-')
        os.rename(old_name, new_name)


try:
    file_rename(argv[1])
except Exception:
    print('\n*** Path to directory is missing ***')
    print('——————————————————————————————————————————————————')
    print('\nUsage: python3 file_rename.py (path to directory)*')
    print('Example: python3 file_rename.py static/images/\n')
